#
# Conditional build:
%bcond_with	pandoc		# build man pages with pandoc
%bcond_without	tests		# build without tests
#
%ifarch x32
%undefine	with_pandoc
%endif
Summary:	C library to access the HSTS preload list
Name:		libhsts
Version:	0.1.0
Release:	3
License:	BSD
Group:		Libraries
Source0:	https://gitlab.com/rockdaboot/libhsts/uploads/4753f61b5a3c6253acf4934217816e3f/%{name}-%{version}.tar.gz
# Source0-md5:	5599c8b2530df6b26ed5e766a8d9ed3c
URL:		https://gitlab.com/rockdaboot/libhsts
BuildRequires:	doxygen
%{?with_pandoc:BuildRequires:	pandoc}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The HSTS preload list is a list of domains that support HTTPS. The
list is compiled by Google and is utilised by Chrome, Firefox and
others. With this information, a HTTP client may contact a website
without trying a plain-text HTTP connection first. It prevents
interception with redirects that take place over HTTP. None of the
sent data will ever be unencrypted.

%package devel
Summary:	Header files and develpment documentation for libhsts
Summary(es.UTF-8):	Arquivos de cabeçalho e bibliotecas de desenvolvimento para libhsts
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumetacja do libhsts
Summary(pt_BR.UTF-8):	Bibliotecas e arquivos de inclusão para a libhsts
Summary(ru.UTF-8):	Хедеры и библиотеки програмиста для libhsts
Summary(uk.UTF-8):	Хедери та бібліотеки програміста для libhsts
Group:		Development/Libraries
Requires:	%{name} = %{?epoch}:%{version}-%{release}

%description devel
The HSTS preload list is a list of domains that support HTTPS. The
list is compiled by Google and is utilised by Chrome, Firefox and
others. With this information, a HTTP client may contact a website
without trying a plain-text HTTP connection first. It prevents
interception with redirects that take place over HTTP. None of the
sent data will ever be unencrypted.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do libhsts.

%package static
Summary:	Static libhsts library
Summary(es.UTF-8):	Biblioteca estática usada no desenvolvimento de aplicativos com libhsts
Summary(pl.UTF-8):	Biblioteka statyczna libhsts
Summary(pt_BR.UTF-8):	Biblioteca estática de desenvolvimento
Summary(ru.UTF-8):	Статическая библиотека libhsts
Summary(uk.UTF-8):	Статична бібліотека libhsts
Group:		Development/Libraries
Requires:	%{name}-devel = %{?epoch}:%{version}-%{release}

%description static
Static libhsts library.

%description static -l pl.UTF-8
Biblioteka statyczna libhsts.

%description static -l ru.UTF-8
Статическая библиотека, необходимая для программирования с libhsts.

%description static -l uk.UTF-8
Статична бібліотека, необхідна для програмування з libhsts.

%prep
%setup -q

%build
%configure  \
	--disable-silent-rules

%{__make}

%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{without pandoc}
install -d $RPM_BUILD_ROOT%{_mandir}/man{1,3}
cp -p docs/man/man1/hsts*.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp -p docs/man/man3/libhsts.3 $RPM_BUILD_ROOT%{_mandir}/man3
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS
%attr(755,root,root) %{_bindir}/hsts
%attr(755,root,root) %{_libdir}/libhsts.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libhsts.so.0
%{_mandir}/man1/hsts.1*
%{_mandir}/man1/hsts-make-dafsa.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhsts.so
%{_includedir}/libhsts.h
%{_libdir}/libhsts.la
%{_pkgconfigdir}/libhsts.pc
%{_mandir}/man3/libhsts.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libhsts.a

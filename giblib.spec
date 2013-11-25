Summary:	Wrapper library to imlib2
Name:		giblib
Version:	1.2.4
Release:	2
License:	BSD-like
Group:		X11/Libraries
Source0:	http://www.linuxbrit.co.uk/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	c810ef5389baf24882a1caca2954385e
URL:		http://www.linuxbrit.co.uk/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	imlib2-devel
BuildRequires:	libltdl-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
giblib is a utility library used by many of the applications LinuxBrit
writes. It incorporates doubly linked lists, some string functions,
and a wrapper for imlib2. The wrapper does two things. It gives you
access to fontstyles, which can be loaded from files, saved to files
or defined dynamically through the API. It also, and more importantly,
wraps imlib2's context API to simplify calls.

%package devel
Summary:	Header files for giblib
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for giblib.

%prep
%setup -q

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %ghost %{_libdir}/lib*.so.1
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/%{name}
%{_libdir}/lib*.la
%{_pkgconfigdir}/*.pc


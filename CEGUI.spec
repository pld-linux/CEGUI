# TODO:
# - plenty of BRs are missing
# - gcc33 patch only for AC-branch
#
Summary:	CEGUI is a free library providing windowing and widgets
Name:		CEGUI
Version:	0.5.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/crayzedsgui/%{name}-%{version}b.tar.gz
# Source0-md5:	b42322a33c6a06eede76b15f75694a17
Source1:	http://dl.sourceforge.net/crayzedsgui/%{name}-DOCS-%{version}.tar.gz
# Source1-md5:	e268b5812f146ee1ff9ba4c07ff501b7
Patch0:         %{name}-gcc33.patch
URL:		http://www.cegui.org.uk/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pcre-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CEGUI stands for Crazy Eddie's Gui System; a free library providing
windowing and widgets for graphics APIs / engines where such
functionality is not natively available, or severely lacking. The
library is object orientated, written in C++, and targeted at games
developers who should be spending their time creating great games, not
building GUI sub-systems!

%package devel
Summary:	Development files for CEGUI
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
CEGUI headers and documentation.

%prep
%setup -q -b 1
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc documentation
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/%{name}/*
%{_pkgconfigdir}/*

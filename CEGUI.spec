# TODO:
# - gcc33 patch only for AC-branch
# - ogre-renderer (BR: CEGUI-OGRE >= 1.0.0 through pkgconfig)
# - maybe we should make subpackages? For example CEGUI-OPENGL (smc.spec)?
#
Summary:	CEGUI - a free library providing windowing and widgets
Summary(pl.UTF-8):	CEGUI - wolnodostępna biblioteka zapewniającą okienka i widgety
Name:		CEGUI
Version:	0.5.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/crayzedsgui/%{name}-%{version}b.tar.gz
# Source0-md5:	b42322a33c6a06eede76b15f75694a17
Source1:	http://dl.sourceforge.net/crayzedsgui/%{name}-DOCS-%{version}.tar.gz
# Source1-md5:	e268b5812f146ee1ff9ba4c07ff501b7
Patch0:		%{name}-gcc33.patch
Patch1:		%{name}-link.patch
URL:		http://www.cegui.org.uk/
BuildRequires:	DevIL-devel
BuildRequires:	FreeImage-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-glut-devel
BuildRequires:	SILLY-devel >= 0.1.0
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	corona-devel >= 1.0.2
BuildRequires:	expat-devel
BuildRequires:	freetype-devel >= 2.0
BuildRequires:	irrlicht-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libxml2-devel >= 1:2.6
BuildRequires:	lua50-devel >= 5.0
BuildRequires:	pcre-devel >= 5.0
BuildRequires:	pkgconfig
BuildRequires:	xerces-c-devel
# for irrlicht
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CEGUI stands for Crazy Eddie's Gui System; a free library providing
windowing and widgets for graphics APIs / engines where such
functionality is not natively available, or severely lacking. The
library is object orientated, written in C++, and targeted at games
developers who should be spending their time creating great games, not
building GUI sub-systems!

%description -l pl.UTF-8
CEGUI oznacza Crazy Eddie's Gui System - wolnodostępną bibliotekę
zapewniającą okienka i widgety dla graficznych API i silników tam,
gdzie natywnie taka funkcjonalność nie jest dostępna lub ma znaczące
braki. Biblioteka jest zorientowana obiektowo, napisana w C++ i
skierowana dla programistów gier, którzy powinni spędzać czas na
pisaniu świetnych gier, a nie tworzeniu podsystemów GUI!

%package devel
Summary:	Development files for CEGUI
Summary(pl.UTF-8):	Pliki programistyczne dla CEGUI
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	freetype-devel >= 2.0
Requires:	libstdc++-devel
Requires:	pcre-devel >= 5.0

%description devel
CEGUI headers and documentation.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do CEGUI.

%prep
%setup -q -b 1
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-default-image-codec=FreeImageImageCodec \
	--with-default-parser=LibxmlParser

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
%attr(755,root,root) %{_libdir}/libCEGUI*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc documentation
%attr(755,root,root) %{_libdir}/libCEGUI*.so
%{_libdir}/libCEGUI*.la
%{_includedir}/%{name}
%{_pkgconfigdir}/CEGUI.pc
%{_pkgconfigdir}/CEGUI-OPENGL.pc

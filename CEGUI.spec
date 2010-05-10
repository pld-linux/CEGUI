# TODO:
# - external tinyxml
# - external tolua++
# - ogre-renderer (BR: CEGUI-OGRE >= 1.0.0 through pkgconfig)
# - maybe we should make subpackages? For example CEGUI-OPENGL (smc.spec)?
#
# Conditional build:
%bcond_without	xercesc		# build XercesParser
%bcond_with	ogre		# build samples with ogre3d
%bcond_with	samples		# build samples
#
Summary:	CEGUI - a free library providing windowing and widgets
Summary(pl.UTF-8):	CEGUI - wolnodostępna biblioteka zapewniającą okienka i widgety
Name:		CEGUI
Version:	0.7.1
Release:	0.1
License:	LGPL v2.1+ (with MIT parts)
Group:		Libraries
Source0:	http://downloads.sourceforge.net/crayzedsgui/%{name}-%{version}.tar.gz
# Source0-md5:	0a2815d5204e3c5510884ab62285da97
Source1:	http://downloads.sourceforge.net/crayzedsgui/%{name}-DOCS-%{version}.tar.gz
# Source1-md5:	b6c1656d6b004c3dc11bf4b887fd5bd3
Patch0:		%{name}-link.patch
URL:		http://www.cegui.org.uk/
BuildRequires:	DevIL-devel
BuildRequires:	DirectFB-devel
BuildRequires:	FreeImage-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-glut-devel
BuildRequires:	SILLY-devel >= 0.1.0
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	corona-devel >= 1.0.2
BuildRequires:	expat-devel
BuildRequires:	freetype-devel >= 2.0
BuildRequires:	glew-devel
BuildRequires:	irrlicht-devel >= 1.4
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libxml2-devel >= 1:2.6
BuildRequires:	lua51-devel >= 5.1
%if %{with ogre}
BuildRequires:	ogre-devel >= 1.0.0
BuildRequires:	ois-devel
%endif
BuildRequires:	pcre-devel >= 5.0
BuildRequires:	pkgconfig
# for irrlicht renderer
BuildRequires:	xorg-lib-libXxf86vm-devel
%if %{with xercesc}
BuildRequires:	xerces-c-devel
%endif
Requires:	irrlicht >= 1.4
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
CEGUI headers.

%description devel -l pl.UTF-8
Pliki nagłówkowe CEGUI.

%package docs
Summary:	Documentation files for CEGUI
Summary(pl.UTF-8):	Pliki dokumentacji CEGUI
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description docs
CEGUI documentation.

%description docs -l pl.UTF-8
Dokumentacja CEGUI.


%prep
%setup -q -a 1
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-default-image-codec=FreeImageImageCodec \
	--with-default-xml-parser=LibxmlParser \
	%{!?with_samples:--disable-samples} \
	%{!?with_ogre:--without-ogre-renderer} \
	--%{?with_xercesc:en}%{!?with_xercesc:dis}able-xerces-c

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
%doc doc/README
# libs
%attr(755,root,root) %{_libdir}/libCEGUIBase-%{version}.so
%attr(755,root,root) %{_libdir}/libCEGUIOpenGLRenderer-%{version}.so
# plugins
%attr(755,root,root) %{_libdir}/libCEGUICoronaImageCodec-%{version}.so
%attr(755,root,root) %{_libdir}/libCEGUICoronaImageCodec.so
%attr(755,root,root) %{_libdir}/libCEGUIDevILImageCodec-%{version}.so
%attr(755,root,root) %{_libdir}/libCEGUIDevILImageCodec.so
%attr(755,root,root) %{_libdir}/libCEGUIExpatParser-%{version}.so
%attr(755,root,root) %{_libdir}/libCEGUIExpatParser.so
%attr(755,root,root) %{_libdir}/libCEGUIFalagardWRBase-%{version}.so
%attr(755,root,root) %{_libdir}/libCEGUIFalagardWRBase.so
%attr(755,root,root) %{_libdir}/libCEGUIFreeImageImageCodec-%{version}.so
%attr(755,root,root) %{_libdir}/libCEGUIFreeImageImageCodec.so
%attr(755,root,root) %{_libdir}/libCEGUIIrrlichtRenderer-%{version}.so
%attr(755,root,root) %{_libdir}/libCEGUIIrrlichtRenderer.so
%attr(755,root,root) %{_libdir}/libCEGUILibxmlParser-%{version}.so
%attr(755,root,root) %{_libdir}/libCEGUILibxmlParser.so
%attr(755,root,root) %{_libdir}/libCEGUILuaScriptModule-%{version}.so
%attr(755,root,root) %{_libdir}/libCEGUILuaScriptModule.so
%attr(755,root,root) %{_libdir}/libCEGUISILLYImageCodec-%{version}.so
%attr(755,root,root) %{_libdir}/libCEGUISILLYImageCodec.so
%attr(755,root,root) %{_libdir}/libCEGUITGAImageCodec-%{version}.so
%attr(755,root,root) %{_libdir}/libCEGUITGAImageCodec.so
%attr(755,root,root) %{_libdir}/libCEGUITinyXMLParser-%{version}.so
%attr(755,root,root) %{_libdir}/libCEGUITinyXMLParser.so
%attr(755,root,root) %{_libdir}/libCEGUIXercesParser-%{version}.so
%attr(755,root,root) %{_libdir}/libCEGUIXercesParser.so
%attr(755,root,root) %{_libdir}/libCEGUItoluapp-%{version}.so
%attr(755,root,root) %{_libdir}/libCEGUItoluapp.so

%files docs
%defattr(644,root,root,755)
%doc docs/CEGUI-DOCS-%{version}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/xml_schemas
%{_datadir}/%{name}/xml_schemas/*.xsd

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libCEGUIBase.so
%attr(755,root,root) %{_libdir}/libCEGUIOpenGLRenderer.so
%{_libdir}/libCEGUIBase.la
%{_libdir}/libCEGUIOpenGLRenderer.la
# plugins - but as their headers are included...
%{_libdir}/libCEGUICoronaImageCodec.la
%{_libdir}/libCEGUIDevILImageCodec.la
%{_libdir}/libCEGUIExpatParser.la
%{_libdir}/libCEGUIFalagardWRBase.la
%{_libdir}/libCEGUIFreeImageImageCodec.la
%{_libdir}/libCEGUIIrrlichtRenderer.la
%{_libdir}/libCEGUILibxmlParser.la
%{_libdir}/libCEGUILuaScriptModule.la
%{_libdir}/libCEGUISILLYImageCodec.la
%{_libdir}/libCEGUITGAImageCodec.la
%{_libdir}/libCEGUITinyXMLParser.la
%{_libdir}/libCEGUIXercesParser.la
%{_libdir}/libCEGUItoluapp.la
%{_includedir}/%{name}
%{_pkgconfigdir}/CEGUI.pc
%{_pkgconfigdir}/CEGUI-OPENGL.pc

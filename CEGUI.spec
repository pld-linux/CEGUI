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
Version:	0.6.2
Release:	1
License:	LGPL v2.1+ (with MIT parts)
Group:		Libraries
Source0:	http://dl.sourceforge.net/crayzedsgui/%{name}-%{version}b.tar.gz
# Source0-md5:	4fbd95e5a2ac1c7acf2a8f5df3ac6b93
Source1:	http://dl.sourceforge.net/crayzedsgui/%{name}-%{version}-DOCS.tar.gz
# Source1-md5:	5c6b54b9472ffaefc27ed4a9b8fefe25
Patch0:		%{name}-link.patch
Patch1:		%{name}-gcc43.patch
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
%doc AUTHORS ChangeLog README
# libs
%attr(755,root,root) %{_libdir}/libCEGUIBase.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libCEGUIBase.so.1
%attr(755,root,root) %{_libdir}/libCEGUIOpenGLRenderer.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libCEGUIOpenGLRenderer.so.0
# plugins
%attr(755,root,root) %{_libdir}/libCEGUICoronaImageCodec.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libCEGUICoronaImageCodec.so.0
%attr(755,root,root) %{_libdir}/libCEGUICoronaImageCodec.so
%attr(755,root,root) %{_libdir}/libCEGUIDevILImageCodec.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libCEGUIDevILImageCodec.so.0
%attr(755,root,root) %{_libdir}/libCEGUIDevILImageCodec.so
%attr(755,root,root) %{_libdir}/libCEGUIExpatParser.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libCEGUIExpatParser.so.0
%attr(755,root,root) %{_libdir}/libCEGUIExpatParser.so
%attr(755,root,root) %{_libdir}/libCEGUIFalagardWRBase.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libCEGUIFalagardWRBase.so.1
%attr(755,root,root) %{_libdir}/libCEGUIFalagardWRBase.so
%attr(755,root,root) %{_libdir}/libCEGUIFreeImageImageCodec.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libCEGUIFreeImageImageCodec.so.0
%attr(755,root,root) %{_libdir}/libCEGUIFreeImageImageCodec.so
%attr(755,root,root) %{_libdir}/libCEGUIIrrlichtRenderer.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libCEGUIIrrlichtRenderer.so.0
%attr(755,root,root) %{_libdir}/libCEGUIIrrlichtRenderer.so
%attr(755,root,root) %{_libdir}/libCEGUILibxmlParser.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libCEGUILibxmlParser.so.0
%attr(755,root,root) %{_libdir}/libCEGUILibxmlParser.so
%attr(755,root,root) %{_libdir}/libCEGUILuaScriptModule.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libCEGUILuaScriptModule.so.1
%attr(755,root,root) %{_libdir}/libCEGUILuaScriptModule.so
%attr(755,root,root) %{_libdir}/libCEGUISILLYImageCodec.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libCEGUISILLYImageCodec.so.0
%attr(755,root,root) %{_libdir}/libCEGUISILLYImageCodec.so
%attr(755,root,root) %{_libdir}/libCEGUITGAImageCodec.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libCEGUITGAImageCodec.so.0
%attr(755,root,root) %{_libdir}/libCEGUITGAImageCodec.so
%attr(755,root,root) %{_libdir}/libCEGUITinyXMLParser.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libCEGUITinyXMLParser.so.0
%attr(755,root,root) %{_libdir}/libCEGUITinyXMLParser.so
%attr(755,root,root) %{_libdir}/libCEGUIXercesParser.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libCEGUIXercesParser.so.0
%attr(755,root,root) %{_libdir}/libCEGUIXercesParser.so
%attr(755,root,root) %{_libdir}/libCEGUItoluapp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libCEGUItoluapp.so.1
%attr(755,root,root) %{_libdir}/libCEGUItoluapp.so

%files docs
%defattr(644,root,root,755)
%doc documentation
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/XMLRefSchema
%{_datadir}/%{name}/XMLRefSchema/*.xsd
%{_datadir}/%{name}/XMLRefSchema/Readme.txt

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

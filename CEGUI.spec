# TODO:
# - python
# - separate packages for plugins
#
# Conditional build:
%bcond_without	xercesc		# build XercesParser
%bcond_without	ogre		# build without Ogre renderer
%bcond_without	opengl		# build without OpenGL renderer
%bcond_with	samples		# build samples
#
Summary:	CEGUI - a free library providing windowing and widgets
Summary(pl.UTF-8):	CEGUI - wolnodostępna biblioteka zapewniającą okienka i widgety
Name:		CEGUI
Version:	0.7.5
Release:	9
License:	LGPL v2.1+ (with MIT parts)
Group:		Libraries
Source0:	http://downloads.sourceforge.net/crayzedsgui/%{name}-%{version}.tar.gz
# Source0-md5:	38c79d1fdfaaa10f481c99a2ac479516
Source1:	http://downloads.sourceforge.net/crayzedsgui/%{name}-DOCS-%{version}.tar.gz
# Source1-md5:	cdf59df7503f752a70eea4081eaac6ef
Patch0:		%{name}-new-tinyxml.patch
Patch1:		%{name}-gcc.patch
URL:		http://www.cegui.org.uk/
BuildRequires:	DevIL-devel
BuildRequires:	DirectFB-devel >= 1.2.0
BuildRequires:	FreeImage-devel
BuildRequires:	SILLY-devel >= 0.1.0
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	corona-devel
BuildRequires:	expat-devel
BuildRequires:	freetype-devel >= 2.0
BuildRequires:	gtk+2-devel >= 2:2.4
BuildRequires:	irrlicht-devel >= 1.4
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libxml2-devel >= 1:2.6
BuildRequires:	lua51-devel >= 5.1
%if %{with ogre}
BuildRequires:	ogre-devel >= 1.6.0
BuildRequires:	ois-devel
%endif
BuildRequires:	pcre-devel >= 5.0
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRequires:	tinyxml-devel
BuildRequires:	tolua++-devel
# for irrlicht renderer
BuildRequires:	xorg-lib-libXxf86vm-devel
%if %{with opengl}
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-glut-devel
BuildRequires:	glew-devel
%endif
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

%package Ogre
Summary:	OgreRenderer library for CEGUI
Summary(pl.UTF-8):	Biblioteka OgreRenderer dla CEGUI
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description Ogre
OgreRenderer library for CEGUI.

%description Ogre -l pl.UTF-8
Biblioteka OgreRenderer dla CEGUI

%package Ogre-devel
Summary:	Header files for CEGUI OgreRenderer library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki CEGUI OgreRenderer
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	ogre-devel >= 1.6.0

%description Ogre-devel
Header files for CEGUI OgreRenderer library.

%description Ogre-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki CEGUI OgreRenderer.

%package OpenGL
Summary:	OpenGLRenderer library for CEGUI
Summary(pl.UTF-8):	Biblioteka OpenGLRenderer dla CEGUI
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description OpenGL
OpenGLRenderer library for CEGUI.

%description OpenGL -l pl.UTF-8
Biblioteka OpenGLRenderer dla CEGUI.

%package OpenGL-devel
Summary:	Header files for CEGUI OpenGLRenderer library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki CEGUI OpenGLRenderer
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenGL-GLU-devel
Requires:	OpenGL-glut-devel
Requires:	glew-devel

%description OpenGL-devel
Header files for CEGUI OpenGLRenderer library.

%description OpenGL-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki CEGUI OpenGLRenderer.

%prep
%setup -q -a 1
%patch0 -p1
%patch1 -p1

sed -i -e 's/lua5\.1/lua51/' acinclude.m4

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	cegui_corona_config=/usr/bin/corona-config \
	--with-default-image-codec=FreeImageImageCodec \
	--with-default-xml-parser=LibxmlParser \
	%{!?with_samples:--disable-samples} \
	--enable-ogre-renderer%{!?with_ogre:=no} \
	--enable-opengl-renderer%{!?with_opengl:=no} \
	--enable-xerces-c%{!?with_xercesc:=no}

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
%attr(755,root,root) %{_libdir}/libCEGUIBase-%{version}.so
# plugins
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
%attr(755,root,root) %{_libdir}/libCEGUISTBImageCodec-%{version}.so
%attr(755,root,root) %{_libdir}/libCEGUISTBImageCodec.so
%attr(755,root,root) %{_libdir}/libCEGUITGAImageCodec-%{version}.so
%attr(755,root,root) %{_libdir}/libCEGUITGAImageCodec.so
%attr(755,root,root) %{_libdir}/libCEGUITinyXMLParser-%{version}.so
%attr(755,root,root) %{_libdir}/libCEGUITinyXMLParser.so
%attr(755,root,root) %{_libdir}/libCEGUIXercesParser-%{version}.so
%attr(755,root,root) %{_libdir}/libCEGUIXercesParser.so

%files docs
%defattr(644,root,root,755)
%doc docs
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/xml_schemas
%{_datadir}/%{name}/xml_schemas/*.xsd

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libCEGUIBase.so
%{_libdir}/libCEGUIBase.la
# plugins - but as their headers are included...
%{_libdir}/libCEGUIDevILImageCodec.la
%{_libdir}/libCEGUIExpatParser.la
%{_libdir}/libCEGUIFalagardWRBase.la
%{_libdir}/libCEGUIFreeImageImageCodec.la
%{_libdir}/libCEGUIIrrlichtRenderer.la
%{_libdir}/libCEGUILibxmlParser.la
%{_libdir}/libCEGUILuaScriptModule.la
%{_libdir}/libCEGUISILLYImageCodec.la
%{_libdir}/libCEGUISTBImageCodec.la
%{_libdir}/libCEGUITGAImageCodec.la
%{_libdir}/libCEGUITinyXMLParser.la
%{_libdir}/libCEGUIXercesParser.la
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/CEGUI*.h
%{_includedir}/%{name}/ImageCodecModules
%dir %{_includedir}/%{name}/RendererModules
%{_includedir}/%{name}/RendererModules/Irrlicht
%{_includedir}/%{name}/ScriptingModules
%{_includedir}/%{name}/WindowRendererSets
%{_includedir}/%{name}/XMLParserModules
%{_includedir}/%{name}/elements
%{_includedir}/%{name}/falagard
%{_pkgconfigdir}/CEGUI.pc

%if %{with ogre}
%files Ogre
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libCEGUIOgreRenderer-%{version}.so

%files Ogre-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libCEGUIOgreRenderer.so
%{_libdir}/libCEGUIOgreRenderer.la
%{_includedir}/%{name}/RendererModules/Ogre
%{_pkgconfigdir}/CEGUI-OGRE.pc
%endif

%if %{with opengl}
%files OpenGL
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libCEGUIOpenGLRenderer-%{version}.so

%files OpenGL-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libCEGUIOpenGLRenderer.so
%{_libdir}/libCEGUIOpenGLRenderer.la
%{_includedir}/%{name}/RendererModules/OpenGL
%{_pkgconfigdir}/CEGUI-OPENGL.pc
%endif

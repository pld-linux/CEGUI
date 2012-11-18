# TODO:
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
Version:	0.7.7
Release:	1
License:	LGPL v2.1+ (with MIT parts)
Group:		Libraries
Source0:	http://downloads.sourceforge.net/crayzedsgui/%{name}-%{version}.tar.gz
# Source0-md5:	8b83577f86eaa1581765dd155c7c8f24
Source1:	http://downloads.sourceforge.net/crayzedsgui/%{name}-DOCS-%{version}.tar.gz
# Source1-md5:	4d011b7e262222a4c0129ccb19014686
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
BuildRequires:	ois-devel >= 1.0.0
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

%package ImageCodec-Corona
Summary:	CoronaImageCodec library for CEGUI
Summary(pl.UTF-8):	Biblioteka CoronaImageCodec dla CEGUI
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description ImageCodec-Corona
CoronaImageCodec library for CEGUI.

%description ImageCodec-Corona -l pl.UTF-8
Biblioteka CoronaImageCodec dla CEGUI

%package ImageCodec-Corona-devel
Summary:	Header files for CEGUI CoronaImageCodec library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki CEGUI CoronaImageCodec
Group:		Development/Libraries
Requires:	%{name}-ImageCodec-Corona = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	corona-devel

%description ImageCodec-Corona-devel
Header files for CEGUI CoronaImageCodec library.

%description ImageCodec-Corona-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki CEGUI CoronaImageCodec.

%package ImageCodec-DevIL
Summary:	DevILImageCodec library for CEGUI
Summary(pl.UTF-8):	Biblioteka DevILImageCodec dla CEGUI
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description ImageCodec-DevIL
DevILImageCodec library for CEGUI.

%description ImageCodec-DevIL -l pl.UTF-8
Biblioteka DevILImageCodec dla CEGUI

%package ImageCodec-DevIL-devel
Summary:	Header files for CEGUI DevILImageCodec library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki CEGUI DevILImageCodec
Group:		Development/Libraries
Requires:	%{name}-ImageCodec-DevIL = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	DevIL-devel

%description ImageCodec-DevIL-devel
Header files for CEGUI DevILImageCodec library.

%description ImageCodec-DevIL-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki CEGUI DevILImageCodec.

%package ImageCodec-FreeImage
Summary:	FreeImageImageCodec library for CEGUI
Summary(pl.UTF-8):	Biblioteka FreeImageImageCodec dla CEGUI
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description ImageCodec-FreeImage
FreeImageImageCodec library for CEGUI.

%description ImageCodec-FreeImage -l pl.UTF-8
Biblioteka FreeImageImageCodec dla CEGUI

%package ImageCodec-FreeImage-devel
Summary:	Header files for CEGUI FreeImageImageCodec library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki CEGUI FreeImageImageCodec
Group:		Development/Libraries
Requires:	%{name}-ImageCodec-FreeImage = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	FreeImage-devel

%description ImageCodec-FreeImage-devel
Header files for CEGUI FreeImageImageCodec library.

%description ImageCodec-FreeImage-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki CEGUI FreeImageImageCodec.

%package ImageCodec-SILLY
Summary:	SILLYImageCodec library for CEGUI
Summary(pl.UTF-8):	Biblioteka SILLYImageCodec dla CEGUI
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	SILLY >= 0.1.0

%description ImageCodec-SILLY
SILLYImageCodec library for CEGUI.

%description ImageCodec-SILLY -l pl.UTF-8
Biblioteka SILLYImageCodec dla CEGUI

%package ImageCodec-SILLY-devel
Summary:	Header files for CEGUI SILLYImageCodec library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki CEGUI SILLYImageCodec
Group:		Development/Libraries
Requires:	%{name}-ImageCodec-SILLY = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	SILLY-devel >= 0.1.0

%description ImageCodec-SILLY-devel
Header files for CEGUI SILLYImageCodec library.

%description ImageCodec-SILLY-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki CEGUI SILLYImageCodec.

%package Renderer-Irrlicht
Summary:	IrrlichtRenderer library for CEGUI
Summary(pl.UTF-8):	Biblioteka IrrlichtRenderer dla CEGUI
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	irrlicht >= 1.4

%description Renderer-Irrlicht
IrrlichtRenderer library for CEGUI.

%description Renderer-Irrlicht -l pl.UTF-8
Biblioteka IrrlichtRenderer dla CEGUI

%package Renderer-Irrlicht-devel
Summary:	Header files for CEGUI IrrlichtRenderer library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki CEGUI IrrlichtRenderer
Group:		Development/Libraries
Requires:	%{name}-Renderer-Irrlicht = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	irrlicht-devel >= 1.4

%description Renderer-Irrlicht-devel
Header files for CEGUI IrrlichtRenderer library.

%description Renderer-Irrlicht-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki CEGUI IrrlichtRenderer.

%package Renderer-Ogre
Summary:	OgreRenderer library for CEGUI
Summary(pl.UTF-8):	Biblioteka OgreRenderer dla CEGUI
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	CEGUI-Ogre

%description Renderer-Ogre
OgreRenderer library for CEGUI.

%description Renderer-Ogre -l pl.UTF-8
Biblioteka OgreRenderer dla CEGUI

%package Renderer-Ogre-devel
Summary:	Header files for CEGUI OgreRenderer library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki CEGUI OgreRenderer
Group:		Development/Libraries
Requires:	%{name}-Renderer-Ogre = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	ogre-devel >= 1.6.0
Obsoletes:	CEGUI-Ogre-devel

%description Renderer-Ogre-devel
Header files for CEGUI OgreRenderer library.

%description Renderer-Ogre-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki CEGUI OgreRenderer.

%package Renderer-OpenGL
Summary:	OpenGLRenderer library for CEGUI
Summary(pl.UTF-8):	Biblioteka OpenGLRenderer dla CEGUI
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	CEGUI-OpenGL

%description Renderer-OpenGL
OpenGLRenderer library for CEGUI.

%description Renderer-OpenGL -l pl.UTF-8
Biblioteka OpenGLRenderer dla CEGUI.

%package Renderer-OpenGL-devel
Summary:	Header files for CEGUI OpenGLRenderer library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki CEGUI OpenGLRenderer
Group:		Development/Libraries
Requires:	%{name}-Renderer-OpenGL = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	OpenGL-GLU-devel
Requires:	OpenGL-glut-devel
Requires:	glew-devel
Obsoletes:	CEGUI-OpenGL-devel

%description Renderer-OpenGL-devel
Header files for CEGUI OpenGLRenderer library.

%description Renderer-OpenGL-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki CEGUI OpenGLRenderer.

%package -n python-CEGUI
Summary:	Python binding for CEGUI
Summary(pl.UTF-8):	Wiązania Pythona do CEGUI
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description -n python-CEGUI
Python binding for CEGUI.

%description -n python-CEGUI -l pl.UTF-8
Wiązania Pythona do CEGUI.

%package -n python-CEGUI-Renderer-Ogre
Summary:	Python binding for CEGUI OgreRenderer library
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki CEGUI OgreRenderer
Group:		Libraries/Python
Requires:	%{name}-Renderer-Ogre = %{version}-%{release}
Requires:	python-CEGUI = %{version}-%{release}

%description -n python-CEGUI-Renderer-Ogre
Python binding for CEGUI OgreRenderer library.

%description -n python-CEGUI-Renderer-Ogre -l pl.UTF-8
Wiązania Pythona do biblioteki CEGUI OgreRenderer.

%package -n python-CEGUI-Renderer-OpenGL
Summary:	Python binding for CEGUI OpenGLRenderer library
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki CEGUI OpenGLRenderer
Group:		Libraries/Python
Requires:	%{name}-Renderer-OpenGL = %{version}-%{release}
Requires:	python-CEGUI = %{version}-%{release}

%description -n python-CEGUI-Renderer-OpenGL
Python binding for CEGUI OpenGLRenderer library.

%description -n python-CEGUI-Renderer-OpenGL -l pl.UTF-8
Wiązania Pythona do biblioteki CEGUI OpenGLRenderer.

%prep
%setup -q -a 1

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

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/*.la

%if %{without samples}
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/CEGUI/{animations,fonts,imagesets,layouts,looknfeel,lua_scripts,schemes,xml_schemas}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	ImageCodec-Corona -p /sbin/ldconfig
%postun	ImageCodec-Corona -p /sbin/ldconfig
%post	ImageCodec-DevIL -p /sbin/ldconfig
%postun	ImageCodec-DevIL -p /sbin/ldconfig
%post	ImageCodec-FreeImage -p /sbin/ldconfig
%postun	ImageCodec-FreeImage -p /sbin/ldconfig
%post	ImageCodec-SILLY -p /sbin/ldconfig
%postun	ImageCodec-SILLY -p /sbin/ldconfig

%post	Renderer-Irrlicht -p /sbin/ldconfig
%postun	Renderer-Irrlicht -p /sbin/ldconfig
%post	Renderer-Ogre -p /sbin/ldconfig
%postun	Renderer-Ogre -p /sbin/ldconfig
%post	Renderer-OpenGL -p /sbin/ldconfig
%postun	Renderer-OpenGL -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc doc/README
%attr(755,root,root) %{_libdir}/libCEGUIBase-%{version}.so
# plugins
%attr(755,root,root) %{_libdir}/libCEGUIExpatParser-%{version}.so
%attr(755,root,root) %{_libdir}/libCEGUIExpatParser.so
%attr(755,root,root) %{_libdir}/libCEGUIFalagardWRBase-%{version}.so
%attr(755,root,root) %{_libdir}/libCEGUIFalagardWRBase.so
%attr(755,root,root) %{_libdir}/libCEGUILibxmlParser-%{version}.so
%attr(755,root,root) %{_libdir}/libCEGUILibxmlParser.so
%attr(755,root,root) %{_libdir}/libCEGUILuaScriptModule-%{version}.so
%attr(755,root,root) %{_libdir}/libCEGUILuaScriptModule.so
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

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libCEGUIBase.so
%{_libdir}/libCEGUIBase.la
# plugins - but as their headers are included...
%{_libdir}/libCEGUIExpatParser.la
%{_libdir}/libCEGUIFalagardWRBase.la
%{_libdir}/libCEGUILibxmlParser.la
%{_libdir}/libCEGUILuaScriptModule.la
%{_libdir}/libCEGUISTBImageCodec.la
%{_libdir}/libCEGUITGAImageCodec.la
%{_libdir}/libCEGUITinyXMLParser.la
%{_libdir}/libCEGUIXercesParser.la
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/CEGUI*.h
%dir %{_includedir}/%{name}/ImageCodecModules
%{_includedir}/%{name}/ImageCodecModules/STBImageCodec
%{_includedir}/%{name}/ImageCodecModules/TGAImageCodec
%dir %{_includedir}/%{name}/RendererModules
%{_includedir}/%{name}/ScriptingModules
%{_includedir}/%{name}/WindowRendererSets
%{_includedir}/%{name}/XMLParserModules
%{_includedir}/%{name}/elements
%{_includedir}/%{name}/falagard
%{_pkgconfigdir}/CEGUI.pc

%files ImageCodec-Corona
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libCEGUICoronaImageCodec-%{version}.so
%attr(755,root,root) %{_libdir}/libCEGUICoronaImageCodec.so

%files ImageCodec-Corona-devel
%defattr(644,root,root,755)
%{_libdir}/libCEGUICoronaImageCodec.la
%{_includedir}/%{name}/ImageCodecModules/CoronaImageCodec

%files ImageCodec-DevIL
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libCEGUIDevILImageCodec-%{version}.so
%attr(755,root,root) %{_libdir}/libCEGUIDevILImageCodec.so

%files ImageCodec-DevIL-devel
%defattr(644,root,root,755)
%{_libdir}/libCEGUIDevILImageCodec.la
%{_includedir}/%{name}/ImageCodecModules/DevILImageCodec

%files ImageCodec-FreeImage
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libCEGUIFreeImageImageCodec-%{version}.so
%attr(755,root,root) %{_libdir}/libCEGUIFreeImageImageCodec.so

%files ImageCodec-FreeImage-devel
%defattr(644,root,root,755)
%{_libdir}/libCEGUIFreeImageImageCodec.la
%{_includedir}/%{name}/ImageCodecModules/FreeImageImageCodec

%files ImageCodec-SILLY
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libCEGUISILLYImageCodec-%{version}.so
%attr(755,root,root) %{_libdir}/libCEGUISILLYImageCodec.so

%files ImageCodec-SILLY-devel
%defattr(644,root,root,755)
%{_libdir}/libCEGUISILLYImageCodec.la
%{_includedir}/%{name}/ImageCodecModules/SILLYImageCodec

%files Renderer-Irrlicht
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libCEGUIIrrlichtRenderer-%{version}.so
%attr(755,root,root) %{_libdir}/libCEGUIIrrlichtRenderer.so

%files Renderer-Irrlicht-devel
%defattr(644,root,root,755)
%{_libdir}/libCEGUIIrrlichtRenderer.la
%{_includedir}/%{name}/RendererModules/Irrlicht

%if %{with ogre}
%files Renderer-Ogre
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libCEGUIOgreRenderer-%{version}.so
%attr(755,root,root) %{_libdir}/libCEGUIOgreRenderer.so

%files Renderer-Ogre-devel
%defattr(644,root,root,755)
%{_libdir}/libCEGUIOgreRenderer.la
%{_includedir}/%{name}/RendererModules/Ogre
%{_pkgconfigdir}/CEGUI-OGRE.pc
%endif

%if %{with opengl}
%files Renderer-OpenGL
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libCEGUIOpenGLRenderer-%{version}.so

%files Renderer-OpenGL-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libCEGUIOpenGLRenderer.so
%{_libdir}/libCEGUIOpenGLRenderer.la
%{_includedir}/%{name}/RendererModules/OpenGL
%{_pkgconfigdir}/CEGUI-OPENGL.pc
%endif

%files -n python-CEGUI
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/PyCEGUI.so

%if %{with ogre}
%files -n python-CEGUI-Renderer-Ogre
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/PyCEGUIOgreRenderer.so
%endif

%if %{with opengl}
%files -n python-CEGUI-Renderer-OpenGL
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/PyCEGUIOpenGLRenderer.so
%endif

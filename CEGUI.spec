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
Version:	0.8.3
Release:	1
License:	LGPL v2.1+ (with MIT parts)
Group:		Libraries
Source0:	http://downloads.sourceforge.net/crayzedsgui/cegui-%{version}.tar.gz
# Source0-md5:	142cca3648cee034e04d0f61bd9863ce
Source1:	http://downloads.sourceforge.net/crayzedsgui/cegui-docs-%{version}.tar.gz
# Source1-md5:	af2931622f9222a6d945c76a84059d70
Patch0:		pthread.patch
Patch1:		python-sitedir.patch
Patch2:		%{name}-glfw3.patch
URL:		http://www.cegui.org.uk/
BuildRequires:	DevIL-devel
BuildRequires:	DirectFB-devel >= 1.2.0
BuildRequires:	FreeImage-devel
BuildRequires:	SILLY-devel >= 0.1.0
BuildRequires:	boost-devel >= 1.36.0
BuildRequires:	boost-python-devel >= 1.36.0
BuildRequires:	cmake >= 2.8
BuildRequires:	corona-devel
BuildRequires:	doxygen
BuildRequires:	expat-devel
BuildRequires:	fribidi-devel
BuildRequires:	freetype-devel >= 2.0
BuildRequires:	glfw-devel
BuildRequires:	gtk+2-devel >= 2:2.4
BuildRequires:	irrlicht-devel >= 1.4
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libxml2-devel >= 1:2.6
BuildRequires:	lua51-devel >= 5.1
BuildRequires:	minizip-devel
%if %{with ogre}
BuildRequires:	ogre-devel >= 1.6.0
BuildRequires:	ois-devel >= 1.0.0
%endif
BuildRequires:	pcre-devel >= 5.0
BuildRequires:	pkgconfig
BuildRequires:	python-devel
BuildRequires:	rapidxml
BuildRequires:	sed >= 4.0
BuildRequires:	tinyxml-devel
BuildRequires:	tolua++-devel
%{?with_xercesc:BuildRequires:	xerces-c-devel}
# for irrlicht renderer
BuildRequires:	xorg-lib-libXxf86vm-devel
%if %{with opengl}
BuildRequires:	GLM
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	glew-devel
BuildRequires:	glfw-devel
%endif
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

%package Parser-Expat
Summary:	Expat-based XML parser module
Summary(pl.UTF-8):	Moduł analizatora XML oparty na bibliotece Expat
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description Parser-Expat
Expat-based XML parser module.

%description Parser-Expat -l pl.UTF-8
Moduł analizatora XML oparty na bibliotece Expat.

%package Parser-LibXML
Summary:	LibXML-based XML parser module
Summary(pl.UTF-8):	Moduł analizatora XML oparty na bibliotece LibXML
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libxml2 >= 1:2.6

%description Parser-LibXML
LibXML-based XML parser module.

%description Parser-LibXML -l pl.UTF-8
Moduł analizatora XML oparty na bibliotece LibXML.

%package Parser-RapidXML
Summary:	RapidXML-based XML parser module
Summary(pl.UTF-8):	Moduł analizatora XML oparty na bibliotece RapidXML
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description Parser-RapidXML
RapidXML-based XML parser module.

%description Parser-RapidXML -l pl.UTF-8
Moduł analizatora XML oparty na bibliotece RapidXML.

%package Parser-TinyXML
Summary:	TinyXML-based XML parser module
Summary(pl.UTF-8):	Moduł analizatora XML oparty na bibliotece TinyXML
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description Parser-TinyXML
TinyXML-based XML parser module.

%description Parser-TinyXML -l pl.UTF-8
Moduł analizatora XML oparty na bibliotece TinyXML.

%package Parser-Xerces
Summary:	Xerces-based XML parser module
Summary(pl.UTF-8):	Moduł analizatora XML oparty na bibliotece Xerces
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description Parser-Xerces
Xerces-based XML parser module.

%description Parser-Xerces -l pl.UTF-8
Moduł analizatora XML oparty na bibliotece Xerces.

%package Renderer-DirectFB
Summary:	DirectFBRenderer library for CEGUI
Summary(pl.UTF-8):	Biblioteka DirectFBRenderer dla CEGUI
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	DirectFB >= 1.2.0

%description Renderer-DirectFB
DirectFBRenderer library for CEGUI.

%description Renderer-DirectFB -l pl.UTF-8
Biblioteka DirectFBRenderer dla CEGUI

%package Renderer-DirectFB-devel
Summary:	Header files for CEGUI DirectFBRenderer library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki CEGUI DirectFBRenderer
Group:		Development/Libraries
Requires:	%{name}-Renderer-DirectFB = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	DirectFB-devel >= 1.2.0

%description Renderer-DirectFB-devel
Header files for CEGUI DirectFBRenderer library.

%description Renderer-DirectFB-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki CEGUI DirectFBRenderer.

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
%setup -q -a 1 -n cegui-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
install -d build
cd build
%cmake .. \
	-DCEGUI_SAMPLES_ENABLED:BOOL=%{?with_samples:ON}%{!?with_samples:OFF} \
	-DCEGUI_BUILD_RENDERER_OPENGL:BOOL=%{?with_opengl:ON}%{!?with_opengl:OFF} \
	-DCEGUI_BUILD_RENDERER_OGRE:BOOL=%{?with_ogre:ON}%{!?with_ogre:OFF} \
	-DCEGUI_BUILD_XMLPARSER_XERCES:BOOL=%{?with_xercesc:ON}%{!?with_xercesc:OFF} \
	-DCEGUI_OPTION_DEFAULT_IMAGECODEC:STRING=FreeImageImageCodec \
	-DCEGUI_OPTION_DEFAULT_XMLPARSER:STRING=LibxmlParser \
	-DCEGUI_PYTHON_INSTALL_DIR=%{py_sitedir}

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install/fast \
	DESTDIR=$RPM_BUILD_ROOT

%if %{without samples}
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/cegui-0/{animations,fonts,imagesets,layouts,looknfeel,lua_scripts,schemes,xml_schemas}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	Renderer-Irrlicht -p /sbin/ldconfig
%postun	Renderer-Irrlicht -p /sbin/ldconfig
%post	Renderer-Ogre -p /sbin/ldconfig
%postun	Renderer-Ogre -p /sbin/ldconfig
%post	Renderer-OpenGL -p /sbin/ldconfig
%postun	Renderer-OpenGL -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc doc/README
%attr(755,root,root) %{_libdir}/libCEGUIBase-0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libCEGUIBase-0.so.2
%attr(755,root,root) %{_libdir}/libCEGUICommonDialogs-0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libCEGUICommonDialogs-0.so.2
%attr(755,root,root) %{_libdir}/libCEGUINullRenderer-0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libCEGUINullRenderer-0.so.2
%attr(755,root,root) %{_libdir}/libCEGUILuaScriptModule-0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libCEGUILuaScriptModule-0.so.2
# plugins
%dir %{_libdir}/cegui-0.8
%attr(755,root,root) %{_libdir}/cegui-0.8/libCEGUICoreWindowRendererSet.so
%attr(755,root,root) %{_libdir}/cegui-0.8/libCEGUISTBImageCodec.so
%attr(755,root,root) %{_libdir}/cegui-0.8/libCEGUITGAImageCodec.so

%files docs
%defattr(644,root,root,755)
%doc cegui-docs-0.8.3/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/toluappcegui-0.8
%attr(755,root,root) %{_libdir}/libCEGUIBase-0.so
%attr(755,root,root) %{_libdir}/libCEGUICommonDialogs-0.so
%attr(755,root,root) %{_libdir}/libCEGUILuaScriptModule-0.so
%attr(755,root,root) %{_libdir}/libCEGUINullRenderer-0.so
%dir %{_includedir}/cegui-0
%dir %{_includedir}/cegui-0/%{name}
%{_includedir}/cegui-0/%{name}/*.h
%{_includedir}/cegui-0/%{name}/CommonDialogs
%dir %{_includedir}/cegui-0/%{name}/ImageCodecModules
%{_includedir}/cegui-0/%{name}/ImageCodecModules/STB
%{_includedir}/cegui-0/%{name}/ImageCodecModules/TGA
%dir %{_includedir}/cegui-0/%{name}/RendererModules
%{_includedir}/cegui-0/%{name}/RendererModules/Null
%{_includedir}/cegui-0/%{name}/ScriptModules
%{_includedir}/cegui-0/%{name}/WindowRendererSets
%{_includedir}/cegui-0/%{name}/XMLParserModules
%{_includedir}/cegui-0/%{name}/falagard
%{_includedir}/cegui-0/%{name}/widgets
%{_pkgconfigdir}/CEGUI-0.pc
%{_pkgconfigdir}/CEGUI-0-LUA.pc
%{_pkgconfigdir}/CEGUI-0-NULL.pc

%files ImageCodec-Corona
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/cegui-0.8/libCEGUICoronaImageCodec.so

%files ImageCodec-Corona-devel
%defattr(644,root,root,755)
%{_includedir}/cegui-0/%{name}/ImageCodecModules/Corona

%files ImageCodec-DevIL
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/cegui-0.8/libCEGUIDevILImageCodec.so

%files ImageCodec-DevIL-devel
%defattr(644,root,root,755)
%{_includedir}/cegui-0/%{name}/ImageCodecModules/DevIL

%files ImageCodec-FreeImage
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/cegui-0.8/libCEGUIFreeImageImageCodec.so

%files ImageCodec-FreeImage-devel
%defattr(644,root,root,755)
%{_includedir}/cegui-0/%{name}/ImageCodecModules/FreeImage

%files ImageCodec-SILLY
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/cegui-0.8/libCEGUISILLYImageCodec.so

%files ImageCodec-SILLY-devel
%defattr(644,root,root,755)
%{_includedir}/cegui-0/%{name}/ImageCodecModules/SILLY

%files Parser-Expat
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/cegui-0.8/libCEGUIExpatParser.so

%files Parser-LibXML
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/cegui-0.8/libCEGUILibXMLParser.so

%files Parser-RapidXML
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/cegui-0.8/libCEGUIRapidXMLParser.so

%files Parser-TinyXML
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/cegui-0.8/libCEGUITinyXMLParser.so

%files Parser-Xerces
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/cegui-0.8/libCEGUIXercesParser.so

%files Renderer-DirectFB
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libCEGUIDirectFBRenderer-0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libCEGUIDirectFBRenderer-0.so.2

%files Renderer-DirectFB-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libCEGUIDirectFBRenderer-0.so
%{_includedir}/cegui-0/%{name}/RendererModules/DirectFB

%files Renderer-Irrlicht
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libCEGUIIrrlichtRenderer-0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libCEGUIIrrlichtRenderer-0.so.2

%files Renderer-Irrlicht-devel
%defattr(644,root,root,755)
%{_includedir}/cegui-0/%{name}/RendererModules/Irrlicht
%attr(755,root,root) %{_libdir}/libCEGUIIrrlichtRenderer-0.so
%{_pkgconfigdir}/CEGUI-0-IRRLICHT.pc

%if %{with ogre}
%files Renderer-Ogre
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libCEGUIOgreRenderer-0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libCEGUIOgreRenderer-0.so.2

%files Renderer-Ogre-devel
%defattr(644,root,root,755)
%{_includedir}/cegui-0/%{name}/RendererModules/Ogre
%attr(755,root,root) %{_libdir}/libCEGUIOgreRenderer-0.so
%{_pkgconfigdir}/CEGUI-0-OGRE.pc
%endif

%if %{with opengl}
%files Renderer-OpenGL
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libCEGUIOpenGLRenderer-0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libCEGUIOpenGLRenderer-0.so.2

%files Renderer-OpenGL-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libCEGUIOpenGLRenderer-0.so
%{_includedir}/cegui-0/%{name}/RendererModules/OpenGL
%{_pkgconfigdir}/CEGUI-0-OPENGL.pc
%{_pkgconfigdir}/CEGUI-0-OPENGL3.pc
%endif

%files -n python-CEGUI
%defattr(644,root,root,755)
%dir %{py_sitedir}/cegui-0.8
%attr(755,root,root) %{py_sitedir}/cegui-0.8/PyCEGUI.so
%attr(755,root,root) %{py_sitedir}/cegui-0.8/PyCEGUINullRenderer.so

%if %{with ogre}
%files -n python-CEGUI-Renderer-Ogre
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/cegui-0.8/PyCEGUIOgreRenderer.so
%endif

%if %{with opengl}
%files -n python-CEGUI-Renderer-OpenGL
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/cegui-0.8/PyCEGUIOpenGLRenderer.so
%endif

# Conditional build:
%bcond_without	ada	# don't build with ada
#
%define		_state		stable
%define		_kdever		3.5.10
%define		_minbaseevr	9:%{_kdever}
%define		_minkdesdkevr	3:%{_kdever}

Summary:	KDE Integrated Development Environment
Summary(de.UTF-8):	KDevelop ist eine grafische Entwicklungsumgebung für KDE
Summary(pl.UTF-8):	Zintegrowane środowisko programisty dla KDE
Summary(pt_BR.UTF-8):	Ambiente Integrado de Desenvolvimento para o KDE
Summary(zh_CN.UTF-8):	KDE C/C++集成开发环境
Name:		kdevelop
Version:	3.5.4
Release:	1
Epoch:		7
License:	GPL
Group:		X11/Development/Tools
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{_kdever}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	06aa12a89b2c09968a92e1d8b575819c
Patch100:	%{name}-branch.diff
Patch0:		kde-common-PLD-nopython.patch
Patch1:		%{name}-am.patch
Patch2:		kde-ac260-lt.patch
Patch3:		%{name}-ncurses.patch
URL:		http://www.kdevelop.org/
# disabled, breaks with this new antlr
# BuildRequires:	antlr >= 2.7.3
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	db-devel
BuildRequires:	doxygen
BuildRequires:	flex
%{?with_ada:BuildRequires:gcc-ada}
BuildRequires:	gettext-tools
BuildRequires:	kdelibs-devel >= %{_minbaseevr}
BuildRequires:	kdesdk-libcvsservice-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pcre-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	subversion-devel >= 1.2.0-4
BuildRequires:	zlib-devel
BuildConflicts:	star
Requires:	kdebase-core >= %{_minbaseevr}
Requires:	kdesdk-libcvsservice >= %{_minkdesdkevr}
Requires:	kdoc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The KDevelop Integrated Development Environment provides many features
that developers need as well as providing a unified interface to
programs like gdb, the C/C++ compiler, and make.

KDevelop manages or provides: all development tools needed for C++
programming like Compiler, Linker, automake and autoconf; KAppWizard,
which generates complete, ready-to-go sample applications;
Classgenerator, for creating new classes and integrating them into the
current project; File management for sources, headers, documentation
etc. to be included in the project; The creation of User-Handbooks
written with SGML and the automatic generation of HTML-output with the
KDE look and feel; Automatic HTML-based API-documentation for your
project's classes with cross-references to the used libraries;
Internationalization support for your application, allowing
translators to easily add their target language to a project;

KDevelop also includes WYSIWYG (What you see is what you get)-creation
of user interfaces with a built-in dialog editor; Debugging your
application by integrating KDbg; Editing of project-specific pixmaps
with KIconEdit; The inclusion of any other program you need for
development by adding it to the "Tools"-menu according to your
individual needs.

%description -l de.UTF-8
KDevelop ist eine grafische Entwicklungsumgebung für KDE.

Das KDevelop-Projekt wurde 1998 begonnen, um eine einfach zu
bedienende grafische (integrierte) Entwicklungsumgebung für C++ und C
auf Unix-basierten Betriebssystemen bereitzustellen. Seit damals ist
die KDevelop-IDE öffentlich unter der GPL erhältlich und unterstützt
u. a. Qt-, KDE-, GNOME-, C++- und C-Projekte.

%description -l pl.UTF-8
KDevelop to zintegrowane środowisko programistyczne dla KDE, dające
wiele możliwości przydatnych programistom oraz zunifikowany interfejs
do programów typu gdb, kompilator C/C++ oraz make.

KDevelop obsługuje lub zawiera: wszystkie narzędzia programistyczne
potrzebne do programowania w C++ jak kompilator, linker, automake,
autoconf; KAppWizard, generujący kompletne, gotowe do uruchomienia,
proste aplikacje; Classgenerator do tworzenia nowych klas i włączania
ich do projektu; zarządzanie plikami źródłowymi, nagłówkowymi,
dokumentacją itp.; tworzenie podręczników użytkownika pisanych w SGML
i automatyczne generowanie wyjścia HTML pasującego do KDE;
automatyczne tworzenie dokumentacji API w HTML do klas projektu z
odniesieniami do używanych bibliotek; wsparcie dla
internacjonalizacji, pozwalające tłumaczom łatwo dodawać pliki z
tłumaczeniami do projektu.

KDevelop ma także tworzenie interfejsów użytkownika przy użyciu
edytora dialogów WYSIWYG; odpluskwianie aplikacji poprzez integrację z
KDbg; edycję ikon przy pomocy KIconEdit; dołączanie innych programów
potrzebnych do programowania przez dodanie ich do menu Tools według
własnych potrzeb.

%prep
%setup -q
%patch100 -p0
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%{__sed} -i -e 's/Terminal=0/Terminal=false/' \
	-e 's/\(^Categories=.*$\)/\1;/' \
	kdevelop.desktop

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs
%configure \
	--disable-rpath \
	--with-qt-libraries=%{_libdir} \
	%{!?with_ada:--disable-ada} \
	--disable-final \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--with-apr-config=%{_bindir}/apr-1-config \
	--with-apu-config=%{_bindir}/apu-1-config \
	--with-svn-include=%{_includedir}/subversion-1 \
	--with-svn-lib=%{_libdir} \
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full}

# disabled, breaks with new antlr
# %{?with_ada:%{__make} -C languages/ada genparser}

%{__make}

rm -f makeinstall.stamp

%install
if [ ! -f makeinstall.stamp -o ! -d $RPM_BUILD_ROOT ]; then
	rm -rf makeinstall.stamp installed.stamp $RPM_BUILD_ROOT

	%{__make} install \
		DESTDIR=$RPM_BUILD_ROOT \
		kde_libs_htmldir=%{_kdedocdir} \
		kde_htmldir=%{_kdedocdir}

	touch makeinstall.stamp
fi

if [ ! -f installed.stamp ]; then
	mv $RPM_BUILD_ROOT%{_iconsdir}/{lo,hi}color/16x16/actions/kdevelop_tip.png
	mv $RPM_BUILD_ROOT%{_iconsdir}/{lo,hi}color/32x32/actions/kdevelop_tip.png

	rm -f $RPM_BUILD_ROOT%{_libdir}/kde3/*.la
	rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

	touch installed.stamp
fi

%find_lang %{name} --with-kde --all-name


%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdevassistant
%attr(755,root,root) %{_bindir}/kdevdesigner
%attr(755,root,root) %{_bindir}/kdevelop
%attr(755,root,root) %{_bindir}/kdevelop-htdig
%attr(755,root,root) %{_bindir}/kdevprj2kdevelop
%attr(755,root,root) %{_bindir}/kdevprofileeditor
%attr(755,root,root) %{_libdir}/*.so
%attr(755,root,root) %{_libdir}/*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libd.so.0
%attr(755,root,root) %ghost %{_libdir}/libdesignerintegration.so.0
%attr(755,root,root) %ghost %{_libdir}/libdocumentation_interfaces.so.0
%attr(755,root,root) %ghost %{_libdir}/libgdbmi_parser.so.0
%attr(755,root,root) %ghost %{_libdir}/libkdevbuildbase.so.0
%attr(755,root,root) %ghost %{_libdir}/libkdevbuildtoolswidgets.so.0
%attr(755,root,root) %ghost %{_libdir}/libkdevcatalog.so.0
%attr(755,root,root) %ghost %{_libdir}/libkdevcppparser.so.0
%attr(755,root,root) %ghost %{_libdir}/libkdevelop.so.1
%attr(755,root,root) %ghost %{_libdir}/libkdevextras.so.0
%attr(755,root,root) %ghost %{_libdir}/libkdevpropertyeditor.so.0
%attr(755,root,root) %ghost %{_libdir}/libkdevqmakeparser.so.0
%attr(755,root,root) %ghost %{_libdir}/libkdevshell.so.0
%attr(755,root,root) %ghost %{_libdir}/libkdevwidgets.so.0
%attr(755,root,root) %ghost %{_libdir}/libkinterfacedesigner.so.0
%attr(755,root,root) %ghost %{_libdir}/liblang_debugger.so.0
%attr(755,root,root) %ghost %{_libdir}/liblang_interfaces.so.0
%attr(755,root,root) %ghost %{_libdir}/libprofileengine.so.0
%attr(755,root,root) %{_libdir}/kde3/*.so
%attr(755,root,root) %{_libdir}/kconf_update_bin/kdev-gen-settings-kconf_update
%{_datadir}/apps/kconf_update/kdev-gen-settings.upd
%{_datadir}/apps/kdevabbrev
%if %{with ada}
%{_datadir}/apps/kdevadaproject
%{_datadir}/apps/kdevadasupport
%endif
%{_datadir}/apps/kdevantproject
%{_datadir}/apps/kdevappoutputview
%{_datadir}/apps/kdevappwizard
%{_datadir}/apps/kdevassistant
%{_datadir}/apps/kdevastyle
%{_datadir}/apps/kdevautoproject
%{_datadir}/apps/kdevbashsupport
%{_datadir}/apps/kdevclassview
%{_datadir}/apps/kdevcppsupport
%{_datadir}/apps/kdevcsharpsupport
%{_datadir}/apps/kdevctags2
%{_datadir}/apps/kdevcustomproject
%{_datadir}/apps/kdevcvsservice
%{_datadir}/apps/kdevdebugger
%{_datadir}/apps/kdevdesigner
%{_datadir}/apps/kdevdesignerpart
%{_datadir}/apps/kdevdiff
%{_datadir}/apps/kdevdistpart
%{_datadir}/apps/kdevdocumentation
%{_datadir}/apps/kdevdoxygen
%{_datadir}/apps/kdevelop
%{_datadir}/apps/kdevfilecreate
%{_datadir}/apps/kdevfilelist
%{_datadir}/apps/kdevfilter
%{_datadir}/apps/kdevfortransupport
%{_datadir}/apps/kdevfullscreen
%{_datadir}/apps/kdevgrepview
%{_datadir}/apps/kdevjavasupport
%{_datadir}/apps/kdevmakeview
%{_datadir}/apps/kdevpartexplorer
%{_datadir}/apps/kdevpascalproject
%{_datadir}/apps/kdevpascalsupport
%{_datadir}/apps/kdevperlsupport
%{_datadir}/apps/kdevphpsupport
%{_datadir}/apps/kdevpythonsupport
%{_datadir}/apps/kdevquickopen
%{_datadir}/apps/kdevrbdebugger
%{_datadir}/apps/kdevregexptest
%{_datadir}/apps/kdevreplace
%{_datadir}/apps/kdevrubysupport
%{_datadir}/apps/kdevscripting
%{_datadir}/apps/kdevscriptproject
%{_datadir}/apps/kdevsnippet
%{_datadir}/apps/kdevsqlsupport
%{_datadir}/apps/kdevtipofday
%{_datadir}/apps/kdevtools
%{_datadir}/apps/kdevtrollproject
%{_datadir}/apps/kdevvalgrind
%{_datadir}/apps/kio_pydoc
%{_datadir}/config/kdevassistantrc
%{_datadir}/config/kdeveloprc
%{_datadir}/desktop-directories/kde-development-kdevelop.directory
%{_datadir}/mimelnk/application/x-kdevelop.desktop
%{_datadir}/mimelnk/text/x-fortran.desktop
%{_datadir}/services/*.desktop
%{_datadir}/services/*.protocol
%{_datadir}/services/kded/kdevsvnd.desktop
%{_datadir}/servicetypes/*.desktop
%{_desktopdir}/kde/*.desktop
%{_iconsdir}/hicolor/*/actions/breakpoint_add.png
%{_iconsdir}/hicolor/*/actions/breakpoint_delete.png
%{_iconsdir}/hicolor/*/actions/breakpoint_delete_all.png
%{_iconsdir}/hicolor/*/actions/breakpoint_edit.png
%{_iconsdir}/hicolor/*/actions/kdevelop_tip.png
%{_iconsdir}/hicolor/*/actions/ktip.png
%{_iconsdir}/hicolor/*/apps/kdevassistant.png
%{_iconsdir}/hicolor/*/apps/kdevdesigner.png
%{_iconsdir}/hicolor/*/apps/kdevelop.png

%{_includedir}/kdevelop
%{_includedir}/kinterfacedesigner

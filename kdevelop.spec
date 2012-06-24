#
# Conditional build:
%bcond_without	ada	# don't build with ada
#
%define		_state		stable
%define		_kdever		3.5

Summary:	KDE Integrated Development Environment
Summary(pl):	Zintegrowane �rodowisko programisty dla KDE
Summary(pt_BR):	Ambiente Integrado de Desenvolvimento para o KDE
Summary(zh_CN):	KDE C/C++���ɿ�������
Summary(de):	KDevelop ist eine grafische Entwicklungsumgebung f�r KDE
Name:		kdevelop
Version:	3.3.0
Release:	0.2
Epoch:		7
License:	GPL
Group:		X11/Development/Tools
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_kdever}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	0a8fc5efb3fa27d346fed5bd2b2a8f05
Patch0:		kde-common-PLD.patch
Patch1:		%{name}-am.patch
URL:		http://www.kdevelop.org/
# disabled, breaks with this new antlr
# BuildRequires:	antlr >= 2.7.3
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	db-devel
BuildRequires:	doxygen
BuildRequires:	flex
%{?with_ada:BuildRequires:gcc-ada}
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel >= 9:%{_kdever}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pcre-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	subversion-devel >= 1.2.0-4
#BuildRequires:	unsermake >= 040511
BuildRequires:	zlib-devel
BuildConflicts:	star
Requires:	kdebase-core >= 9:%{_kdever}
Requires:	kdesdk-libcvsservice >= 3:%{_kdever}
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

%description -l pl
KDevelop to zintegrowane �rodowisko programistyczne dla KDE, daj�ce
wiele mo�liwo�ci przydatnych programistom oraz zunifikowany interfejs
do program�w typu gdb, kompilator C/C++ oraz make.

KDevelop obs�uguje lub zawiera: wszystkie narz�dzia programistyczne
potrzebne do programowania w C++ jak kompilator, linker, automake,
autoconf; KAppWizard, generuj�cy kompletne, gotowe do uruchomienia,
proste aplikacje; Classgenerator do tworzenia nowych klas i w��czania
ich do projektu; zarz�dzanie plikami �r�d�owymi, nag��wkowymi,
dokumentacj� itp.; tworzenie podr�cznik�w u�ytkownika pisanych w SGML
i automatyczne generowanie wyj�cia HTML pasuj�cego do KDE;
automatyczne tworzenie dokumentacji API w HTML do klas projektu z
odniesieniami do u�ywanych bibliotek; wsparcie dla
internacjonalizacji, pozwalaj�ce t�umaczom �atwo dodawa� pliki z
t�umaczeniami do projektu.

KDevelop ma tak�e tworzenie interfejs�w u�ytkownika przy u�yciu
edytora dialog�w WYSIWYG; odpluskwianie aplikacji poprzez integracj� z
KDbg; edycj� ikon przy pomocy KIconEdit; do��czanie innych program�w
potrzebnych do programowania przez dodanie ich do menu Tools wed�ug
w�asnych potrzeb.

%description -l de
KDevelop ist eine grafische Entwicklungsumgebung f�r KDE.

Das KDevelop-Projekt wurde 1998 begonnen, um eine einfach zu
bedienende grafische (integrierte Entwicklungsumgebung) f�r C++ und C
auf Unix-basierten Betriebssystemen bereitzustellen. Seit damals ist
die KDevelop-IDE �ffentlich unter der GPL erh�ltlich und unterst�tzt
u. a. Qt-, KDE-, GNOME-, C++- und C-Projekte.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%{__sed} -i -e 's/Terminal=0/Terminal=false/' \
	-e 's/\(^Categories=.*$\)/\1;/' \
	kdevelop.desktop

%build
cp -f /usr/share/automake/config.sub admin
#export UNSERMAKE=%{_datadir}/unsermake/unsermake
%{__make} -f admin/Makefile.common cvs

%configure \
	--disable-rpath \
	--with-qt-libraries=%{_libdir} \
	%{!?with_ada:--disable-ada} \
	--enable-final \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--with-apr-config=%{_bindir}/apr-1-config \
	--with-apu-config=%{_bindir}/apu-1-config \
	--with-svn-include=%{_includedir}/subversion \
	--with-svn-lib=%{_libdir} \
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full}

# disabled, breaks with new antlr
# %{?with_ada:%{__make} -C languages/ada genparser}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_libs_htmldir=%{_kdedocdir} \
	kde_htmldir=%{_kdedocdir}

cd $RPM_BUILD_ROOT%{_iconsdir}
mv {lo,hi}color/16x16/actions/kdevelop_tip.png
mv {lo,hi}color/32x32/actions/kdevelop_tip.png
cd -

%find_lang %{name} --with-kde --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_libdir}/*.la
%attr(755,root,root) %{_libdir}/*.so
%attr(755,root,root) %{_libdir}/*.so.*.*.*
%{_libdir}/kde3/*.la
%attr(755,root,root) %{_libdir}/kde3/*.so*
%{_libdir}/kconf_update_bin/kdev-gen-settings-kconf_update
%{_datadir}/apps/*
%{_datadir}/config/*
%{_datadir}/desktop-directories/kde-development-kdevelop.directory
%{_datadir}/mimelnk/application/*
%{_datadir}/mimelnk/text/x-fortran.desktop
%{_datadir}/services/*
%{_datadir}/servicetypes/*
%{_desktopdir}/kde/*
%{_iconsdir}/hicolor/*/*/*
%{_includedir}/kdevelop
%{_includedir}/kinterfacedesigner

#
# Conditional build:
%define		_ver		3.0.4
%define		_state		stable
%define		_kde_ver	3.2.3

Summary:	KDE Integrated Development Environment
Summary(pl):	Zintegrowane 秗odowisko programisty dla KDE
Summary(pt_BR):	Ambiente Integrado de Desenvolvimento para o KDE
Summary(zh_CN):	KDE C/C++集成开发环境
Name:		kdevelop
Version:	%{_ver}
Release:	1
Epoch:		7
License:	GPL
Group:		X11/Development/Tools
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_kde_ver}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	c4a84b34927e6f1c7fb2bfb9a74b5b34
#Source0:	http://ep09.pld-linux.org/~djurban/kde/%{name}-%{version}.tar.bz2
URL:		http://www.kdevelop.org/
BuildRequires:	antlr >= 2.7.3
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	db-devel
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel  >= 9:3.2.0
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pcre-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	zlib-devel
BuildRequires:	unsermake >= 040511
Requires:	kdebase-core >= 9:3.2.0
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
KDevelop to zintegrowane 秗odowisko programistyczne dla KDE, daj眂e
wiele mo縧iwo禼i przydatnych programistom oraz zunifikowany interfejs
do program體 typu gdb, kompilator C/C++ oraz make.

KDevelop obs硊guje lub zawiera: wszystkie narz阣zia programistyczne
potrzebne do programowania w C++ jak kompilator, linker, automake,
autoconf; KAppWizard, generuj眂y kompletne, gotowe do uruchomienia,
proste aplikacje; Classgenerator do tworzenia nowych klas i w潮czania
ich do projektu; zarz眃zanie plikami 紃骴硂wymi, nag丑wkowymi,
dokumentacj� itp.; tworzenie podr阠znik體 u縴tkownika pisanych w SGML
i automatyczne generowanie wyj禼ia HTML pasuj眂ego do KDE;
automatyczne tworzenie dokumentacji API w HTML do klas projektu z
odniesieniami do u縴wanych bibliotek; wsparcie dla internacjonalizacji,
 pozwalaj眂e t硊maczom 砤two dodawa� pliki z t硊maczeniami do projektu.

KDevelop ma tak縠 tworzenie interfejs體 u縴tkownika przy u縴ciu
edytora dialog體 WYSIWYG; odpluskwianie aplikacji poprzez integracj� z
KDbg; edycj� ikon przy pomocy KIconEdit; do潮czanie innych program體
potrzebnych do programowania przez dodanie ich do menu Tools wed硊g
w砤snych potrzeb.


%prep
%setup -q

%build
cp %{_datadir}/automake/config.sub admin
export kde_htmldir=%{_kdedocdir}
export kde_libs_htmldir=%{_kdedocdir}
export UNSERMAKE=%{_datadir}/unsermake/unsermake
%{__make} -f admin/Makefile.common cvs

%configure \
	--disable-rpath \
	--with-qt-libraries=%{_libdir} \
	--enable-final

%{__make} -C languages/ada genparser

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_libs_htmldir=%{_kdedocdir} \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT%{_desktopdir}/kde

mv $RPM_BUILD_ROOT{%{_datadir}/applnk/Development/*,%{_desktopdir}/kde}

cd $RPM_BUILD_ROOT%{_iconsdir}
mv {lo,hi}color/16x16/actions/kdevelop_tip.png
mv {lo,hi}color/32x32/actions/kdevelop_tip.png
cd -

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files 
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*.*.*
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/kde3/*.la
%attr(755,root,root) %{_libdir}/kde3/*.so
%{_includedir}/kdevelop
%{_datadir}/apps/*
%{_datadir}/config/*
%{_datadir}/mimelnk/application/*
%{_datadir}/mimelnk/text/x-fortran.desktop
# Conflicts with kdelibs
#%{_datadir}/mimelnk/text/x-pascal.desktop
%{_datadir}/services/*
%{_datadir}/servicetypes/*
%{_desktopdir}/kde/*
%{_iconsdir}/*/*/*/*
%{_kdedocdir}/*

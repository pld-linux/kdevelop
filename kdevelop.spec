
%define 	snap 	030602

Summary:	KDE Integrated Development Environment
Summary(pl):	Zintegrowane 秗odowisko programisty dla KDE
Summary(pt_BR):	Ambiente Integrado de Desenvolvimento para o KDE
Summary(zh_CN):	KDE C/C++集成开发环境
Name:		kdevelop
Version:	3.0
Release:	0.%{snap}.1
Epoch:		7
License:	GPL
Group:		X11/Development/Tools
# Source0-md5:	d1691519fcd00f16dfdc1a738be8584b
Source0:        http://www.kernel.pl/~adgor/kde/%{name}-%{snap}.tar.bz2
URL:		http://www.kdevelop.org/
Requires:	kdoc
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel >= 3.1 
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel
BuildRequires:	fam-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _htmldir        %{_docdir}/kde/HTML
%define         no_install_post_chrpath         1

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
KDbg; edycj� ikon przy pomocy KIconEdit; do潮cznie innych program體
potrzebnych do programowania przez dodanie ich do menu Tools wed硊g
w砤snych potrzeb.

%prep 
%setup -q -n %{name}-%{snap}

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
kde_appsdir="%{_applnkdir}"; export kde_appsdir

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

install -d $RPM_BUILD_ROOT%{_desktopdir}

mv $RPM_BUILD_ROOT{%{_applnkdir}/Development/*,%{_desktopdir}}

cd $RPM_BUILD_ROOT%{_pixmapsdir}
mv {lo,hi}color/16x16/actions/kdevelop_tip.png
mv {lo,hi}color/32x32/actions/kdevelop_tip.png
cd -

%find_lang	%{name}		--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_includedir}/*
%{_libdir}/*.so
%attr(755,root,root) %{_libdir}/*.so.*.*.*
%{_libdir}/kde3/*.la
%attr(755,root,root) %{_libdir}/kde3/*.so
%{_datadir}/apps/*
%{_datadir}/config/*
%{_datadir}/mimelnk/application/*
%{_datadir}/services/*
%{_datadir}/servicetypes/*
%{_desktopdir}/*
%{_pixmapsdir}/*/*/*/*

Summary:	KDE Integrated Development Environment
Summary(pl):	Zintegrowane ¶rodowisko programisty dla KDE
Summary(pt_BR):	Ambiente Integrado de Desenvolvimento para o KDE
Name:		kdevelop
%define		_kde_ver	3.0.3
Version:	2.1.3
Release:	0.1
Epoch:		7
License:	GPL
Vendor:		Sandy Meier <smeier@rz.uni-potsdam.de>
Group:		X11/Development/Tools
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{_kde_ver}/src/%{name}-%{version}_for_KDE_3.0.tar.bz2
URL:		http://www.kdevelop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel = %{_kde_ver}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	openssl-devel
BuildRequires:	qt-devel >= 3
BuildRequires:	zlib-devel
Requires:	kdoc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define         _htmldir        /usr/share/doc/kde/HTML

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
KDevelop to zintegrowane ¶rodowisko programistyczne dla KDE, daj±ce
wiele mo¿liwo¶ci przydatnych programistom oraz zunifikowany interfejs
do programów typu gdb, kompilator C/C++ oraz make.

KDevelop obs³uguje lub zawiera: wszystkie narzêdzia programistyczne
potrzebne do programowania w C++ jak kompilator, linker, automake,
autoconf; KAppWizard, generuj±cy kompletne, gotowe do uruchomienia,
proste aplikacje; Classgenerator do tworzenia nowych klas i w³±czania
ich do projektu; zarz±dzanie plikami ¼ród³owymi, nag³ówkowymi,
dokumentacj± itp.; tworzenie podrêczników u¿ytkownika pisanych w SGML
i automatyczne generowanie wyj¶cia HTML pasuj±cego do KDE;
automatyczne tworzenie dokumentacji API w HTML do klas projektu z
odniesieniami do u¿ywanych bibliotek; wsparcie dla
internacjonalizacji, pozwalaj±ce t³umaczom ³atwo dodawaæ pliki z
t³umaczeniami do projektu.

KDevelop ma tak¿e tworzenie interfejsów u¿ytkownika przy u¿yciu
edytora dialogów WYSIWYG; odpluskwianie aplikacji poprzez integracjê z
KDbg; edycjê ikon przy pomocy KIconEdit; do³±cznie innych programów
potrzebnych do programowania przez dodanie ich do menu Tools wed³ug
w³asnych potrzeb.

#%description -l pt_BR
#KDevelop é um IDE (ou Ambiente Integrado de Desenvolvimento) para o
#KDE.

%prep
%setup -q -n %{name}-%{version}_for_KDE_3.0

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

#aclocal
#autoconf
%configure \
	--enable-final
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*
%{_applnkdir}/Development/*
%{_datadir}/apps/kconf_update/*
%{_datadir}/apps/kdevelop
%{_datadir}/mimelnk/application/*
%{_pixmapsdir}/*/*/*/*

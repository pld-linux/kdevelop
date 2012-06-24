
%define		_ver		3.0.0
%define 	_snap 		031006

Summary:	KDE Integrated Development Environment
Summary(pl):	Zintegrowane �rodowisko programisty dla KDE
Summary(pt_BR):	Ambiente Integrado de Desenvolvimento para o KDE
Summary(zh_CN):	KDE C/C++���ɿ�������
Name:		kdevelop
Version:	%{_ver}
Release:	0.%{_snap}.0.1
Epoch:		7
License:	GPL
Group:		X11/Development/Tools
Source0:        http://www.kernel.pl/~adgor/kde/%{name}-%{_snap}.tar.bz2
# Source0-md5:	2e392c3e4314b0bbfea47eedd00a0ae7
URL:		http://www.kdevelop.org/
Requires:	kdoc
Requires:	kdebase-core >= 9:3.1.92.%{_snap}
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel >= 9:3.1.92.%{_snap} 
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel
BuildRequires:	fam-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
odniesieniami do u�ywanych bibliotek; wsparcie dla internacjonalizacji,
 pozwalaj�ce t�umaczom �atwo dodawa� pliki z t�umaczeniami do projektu.

KDevelop ma tak�e tworzenie interfejs�w u�ytkownika przy u�yciu
edytora dialog�w WYSIWYG; odpluskwianie aplikacji poprzez integracj� z
KDbg; edycj� ikon przy pomocy KIconEdit; do��cznie innych program�w
potrzebnych do programowania przez dodanie ich do menu Tools wed�ug
w�asnych potrzeb.

%prep 
%setup -q -n %{name}-%{_snap}

%build

%{__make} -f admin/Makefile.common cvs

%configure --enable-final --with-pythondir=%{_usr}
sed -i -e "s,CVSSERVICE_SUBDIR\ =,\#CVSSERVICE_SUBDIR\ =," parts/Makefile
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_appsdir=%{_applnkdir} \
	kde_htmldir=%{_docdir}/kde/HTML

install -d $RPM_BUILD_ROOT%{_desktopdir}/kde

mv $RPM_BUILD_ROOT{%{_applnkdir}/Development/*,%{_desktopdir}/kde}

cd $RPM_BUILD_ROOT%{_iconsdir}
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
%{_datadir}/mimelnk/text/x-fortran.desktop
# Conflicts with kdelibs
#%{_datadir}/mimelnk/text/x-pascal.desktop
%{_datadir}/services/*
%{_datadir}/servicetypes/*
%{_desktopdir}/kde/*
%{_iconsdir}/*/*/*/*

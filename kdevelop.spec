#
# Conditional build:
%bcond_without	i18n	# don't build i18n subpackage
#
%define		_state		snapshots
%define		_ver		3.0.1
%define 	_snap 		040220

Summary:	KDE Integrated Development Environment
Summary(pl):	Zintegrowane ¶rodowisko programisty dla KDE
Summary(pt_BR):	Ambiente Integrado de Desenvolvimento para o KDE
Summary(zh_CN):	KDE C/C++¼¯³É¿ª·¢»·¾³
Name:		kdevelop
Version:	%{_ver}.%{_snap}
Release:	1
Epoch:		7
License:	GPL
Group:		X11/Development/Tools
#Source0:	http://www.kdevelop.org/3.0/%{name}-%{version}.tar.bz2
##%% Source0-md5:	918a463159a78b5a13c574dfe2c4e3c7
Source0:	http://ep09.pld-linux.org/~adgor/kde/%{name}.tar.bz2
#Source1:        http://ep09.pld-linux.org/~djurban/kde/i18n/kde-i18n-%{name}-3.2.0.tar.bz2
##%% Source1-md5:	a82df9d4aee85107766b0b8db6abeaec
URL:		http://www.kdevelop.org/
BuildRequires:	antlr >= 2.7.3
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	db-devel
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel >= 9:3.1.94.%{_snap}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	openssl-devel
BuildRequires:	pcre-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	unsermake
BuildRequires:	zlib-devel
Requires:	kdebase-core >= 9:3.1.94.%{_snap}
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
odniesieniami do u¿ywanych bibliotek; wsparcie dla internacjonalizacji,
 pozwalaj±ce t³umaczom ³atwo dodawaæ pliki z t³umaczeniami do projektu.

KDevelop ma tak¿e tworzenie interfejsów u¿ytkownika przy u¿yciu
edytora dialogów WYSIWYG; odpluskwianie aplikacji poprzez integracjê z
KDbg; edycjê ikon przy pomocy KIconEdit; do³±czanie innych programów
potrzebnych do programowania przez dodanie ich do menu Tools wed³ug
w³asnych potrzeb.

%package i18n
Summary:	Internationalization and localization files for kdevelop
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kdevelopa
Group:  	X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdelibs-i18n >= 9:%{version}

%description i18n
Internationalization and localization files for kdevelop.

%description i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kdevelopa.

%prep
%setup -q -n %{name}

%build
cp /usr/share/automake/config.sub admin

export UNSERMAKE=/usr/share/unsermake/unsermake

%{__make} -f admin/Makefile.common cvs

%configure \
	--disable-rpath \
	--enable-final \
	--with-qt-libraries=%{_libdir}

%{__make} -C languages/ada genparser

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_appsdir=%{_applnkdir} \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT%{_desktopdir}/kde

mv $RPM_BUILD_ROOT{%{_applnkdir}/Development/*,%{_desktopdir}/kde}

cd $RPM_BUILD_ROOT%{_iconsdir}
mv {lo,hi}color/16x16/actions/kdevelop_tip.png
mv {lo,hi}color/32x32/actions/kdevelop_tip.png
cd -

%if %{with i18n}
if [ -f "%{SOURCE1}" ] ; then
	bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT
	for f in $RPM_BUILD_ROOT%{_datadir}/locale/*/LC_MESSAGES/*.mo; do
		if [ "`file $f | sed -e 's/.*,//' -e 's/message.*//'`" -le 1 ] ; then
			rm -f $f
		fi
	done
else
	echo "No i18n sources found and building --with i18n. FIXIT!"
	exit 1
fi
%endif

%find_lang	%{name}		--with-kde
%find_lang	kde_app_devel	--with-kde

cat kde_app_devel.lang >> %{name}.lang

%if %{with i18n}
plikes="kdevtipofday \
qeditor \
desktop_kdevelop"
for i in $plikes;
do
	%find_lang $i	--with-kde
	cat $i.lang >> %{name}.lang
done
%endif

##for i in $files; do
i="%{name}"

	> ${i}_en.lang
	echo "%defattr(644,root,root,755)" > ${i}_en.lang
	grep en\/ ${i}.lang|grep -v apidocs >> ${i}_en.lang
	grep -v apidocs $i.lang|grep -v en\/ > ${i}.lang.1
	mv ${i}.lang.1 ${i}.lang
##done

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%if %{with i18n}
%files i18n -f %{name}.lang
%endif

%files -f %{name}_en.lang
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

Summary:	KDE Integrated Development Environment
Summary(pt_BR):	Ambiente Integrado de Desenvolvimento para o KDE
Name:		kdevelop
%define		_kde_ver	2.2.2
Version:	2.0.2
Release:	1
Epoch:		7
License:	GPL
Vendor:		Sandy Meier <smeier@rz.uni-potsdam.de>
Group:		X11/Development/Tools
Group(de):	X11/Entwicklung/Werkzeuge
Group(fr):	X11/Development/Outils
Group(pl):	X11/Programowanie/Narzêdzia
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{_kde_ver}/src/%{name}-%{version}.tar.bz2
URL:		http://www.kdevelop.org/
BuildRequires:	kdelibs-devel >= 2.1
BuildRequires:	openssl-devel
BuildRequires:	qt-devel >= 2.2
BuildRequires:	zlib-devel
BuildRequires:	libpng-devel
BuildRequires:	libjpeg-devel
BuildRequires:	gettext-devel
BuildRequires:	flex
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
Requires:	kdoc
Requires:	kdbg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_htmldir	%{_datadir}/doc/kde/HTML

%description
The KDevelop Integrated Development Environment provides many features
that developers need as well as providing a unified interface to
programs like gdb, the C/C++ compiler, and make. KDevelop manages or
provides:

All development tools needed for C++ programming like Compiler,
Linker, automake and autoconf; KAppWizard, which generates complete,
ready-to-go sample applications; Classgenerator, for creating new
classes and integrating them into the current project; File management
for sources, headers, documentation etc. to be included in the
project; The creation of User-Handbooks written with SGML and the
automatic generation of HTML-output with the KDE look and feel;
Automatic HTML-based API-documentation for your project's classes with
cross-references to the used libraries; Internationalization support
for your application, allowing translators to easily add their target
language to a project;

KDevelop also includes WYSIWYG (What you see is what you get)-creation
of user interfaces with a built-in dialog editor; Debugging your
application by integrating KDbg; Editing of project-specific pixmaps
with KIconEdit; The inclusion of any other program you need for
development by adding it to the "Tools"-menu according to your
individual needs.

%description -l pt_BR
KDevelop é um IDE (ou Ambiente Integrado de Desenvolvimento) para o
KDE.

%prep
%setup -q

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

aclocal
autoconf
%configure \
	--enable-final
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%find_lang %{name} --with-kde

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*
%{_applnkdir}/Development/*
%{_datadir}/apps/*
%{_datadir}/mimelnk/application/*
%{_pixmapsdir}/*/*/*/*

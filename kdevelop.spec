Summary:	KDE Integrated Development Environment
Name:		kdevelop
Version:	1.4.1
Release:	1
Epoch:		7
License:	GPL
Vendor:		Sandy Meier <smeier@rz.uni-potsdam.de>
Group:		X11/KDE/Development
Group(de):	X11/KDE/Entwicklung
Group(pl):	X11/KDE/Programowanie
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/distribution/tar/generic/src/KDevelop/%{name}-%{version}.tar.bz2
URL:		http://www.kdevelop.org/
BuildRequires:	kdelibs-devel >= 2.1
BuildRequires:	openssl-devel
BuildRequires:	qt-devel >= 2.2
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

%prep
%setup -q

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure \
	--with-final
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Development/*
%{_datadir}/apps/*
%{_datadir}/mimelnk/application/*
%{_pixmapsdir}/*/*/*/*

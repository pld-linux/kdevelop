Summary:	KDE Integrated Development Environment
Name:		kdevelop
Version:	1.4.1
Release:	1
License:	GPL
Vendor:		Sandy Meier <smeier@rz.uni-potsdam.de>
Group:		X11/KDE/Development
Group(de):	X11/KDE/Entwicklung
Group(pl):	X11/KDE/Programowanie
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/distribution/tar/generic/src/KDevelop/%{name}-%{version}.tar.bz2
URL:		http://www.kdevelop.org
BuildRequires:	kdelibs-devel >= 2.1
BuildRequires:	openssl-devel
BuildRequires:	qt-devel >= 2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_htmldir	%{_datadir}/doc/kde/HTML

%description
KDevelop is an easy to use IDE (Intergrated Development Enviroment)
for KDE.

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

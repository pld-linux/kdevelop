Summary:	KDE Integrated Development Environment
Name:		kdevelop
Version:	1.4.1
Release:	1
Group:		X11/KDE/Development
Copyright:	GPL
Vendor:		Sandy Meier <smeier@rz.uni-potsdam.de>
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/distribution/tar/generic/src/KDevelop/%{name}-%{version}.tar.bz2
URL:		http://www.kdevelop.org
BuildRequires:	qt-devel >= 2.2
BuildRequires:	kdelibs >= 2.1
Requires:	kdelibs >= 2.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_htmldir	%{_datadir}/doc/kde/HTML

%description
KDevelop is an easy to use IDE (Intergrated Development Enviroment) for KDE.

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
%defattr (644,root,root,755)
%attr(755,root,root) %{_bindir}
%{_applnkdir}
%{_datadir}/apps
%{_datadir}/mimelnk
%{_pixmapsdir}

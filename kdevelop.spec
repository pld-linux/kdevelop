Summary:	KDE Integrated Development Environment
Name:		kdevelop
Version:	0.4
Release:	1
Group:		X11/KDE/Development
Copyright:	GPL
Vendor:		Sandy Meier <smeier@rz.uni-potsdam.de>
Source:		%{name}-%{version}.tar.gz
Patch:		%{name}-%{version}.patch
URL:		http://www.cs.uni-potsdam.de/~smeier/kdevelop/
BuildRequires:	qt-devel >= 1.30
BuildRequires:	kdelibs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDevelop is an easy to use IDE (Intergrated Development Enviroment) for
KDE/Unix/X11. At the moment there are only unstable alpha-versions.

%prep
%setup -q
%patch -p1

%build
if [ -z "$KDEDIR" ]; then
	export KDEDIR=%{prefix}
fi
CXXFLAGS="$RPM_OPT_FLAGS" CFLAGS="$RPM_OPT_FLAGS" ./configure \
	--prefix=$KDEDIR --with-install-root=$RPM_BUILD_ROOT
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install

cd $RPM_BUILD_ROOT
find . -type d | sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' > $RPM_BUILD_DIR/file.list.%{name}
find . -type f | sed 's,^\.,\%attr(-\,root\,root) ,' >> $RPM_BUILD_DIR/file.list.%{name}
find . -type l | sed 's,^\.,\%attr(-\,root\,root) ,' >> $RPM_BUILD_DIR/file.list.%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f ../file.list.%{name}

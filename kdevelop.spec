%define name kdevelop
%define version 0.4
%define release 1
%define prefix /opt/kde

%define builddir $RPM_BUILD_DIR/%{name}-%{version}

Summary: KDE Integrated Development Environment
Name: %{name}
Version: %{version}
Release: %{release}
Prefix: %{prefix}
Group: X11/KDE/Development
Copyright: GPL
Vendor: Sandy Meier <smeier@rz.uni-potsdam.de>
Packager: Troy Engel <tengel@sonic.net>
Source: %{name}-%{version}.tar.gz
URL: http://www.cs.uni-potsdam.de/~smeier/kdevelop/
Requires: qt >= 1.30 kdelibs
BuildRoot: /tmp/build-%{name}-%{version}
Patch: %{name}-%{version}.patch

%description
KDevelop is an easy to use IDE (Intergrated Development Enviroment) for
KDE/Unix/X11. At the moment there are only unstable alpha-versions.

%prep
rm -rf %{builddir}

%setup
%patch -p1
touch `find . -type f`

%build
if [ -z "$KDEDIR" ]; then
	export KDEDIR=%{prefix}
fi
CXXFLAGS="$RPM_OPT_FLAGS" CFLAGS="$RPM_OPT_FLAGS" ./configure \
	--prefix=$KDEDIR --with-install-root=$RPM_BUILD_ROOT
make

%install
rm -rf $RPM_BUILD_ROOT
make install

cd $RPM_BUILD_ROOT
find . -type d | sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' > $RPM_BUILD_DIR/file.list.%{name}
find . -type f | sed 's,^\.,\%attr(-\,root\,root) ,' >> $RPM_BUILD_DIR/file.list.%{name}
find . -type l | sed 's,^\.,\%attr(-\,root\,root) ,' >> $RPM_BUILD_DIR/file.list.%{name}

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf %{builddir}
rm -f $RPM_BUILD_DIR/file.list.%{name}

%files -f ../file.list.%{name}

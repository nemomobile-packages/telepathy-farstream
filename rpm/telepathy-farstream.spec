Name:           telepathy-farstream
Version:        0.4.0
Release:        1
Summary:        Telepathy client library to handle Call channels
Group:          System/Libraries
License:        LGPLv2+
URL:            http://www.freedesktop.org/wiki/Software/Farstream
Source0:        http://telepathy.freedesktop.org/releases/telepathy-farstream/%{name}-%{version}.tar.gz
Patch0:         disable-gtkdoc.patch
BuildRequires:  python
BuildRequires:  pkgconfig(telepathy-glib)
BuildRequires:  pkgconfig(farstream-0.2)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gobject-introspection-1.0)

Obsoletes: telepathy-farsight

%description
Telepathy client libraries for video conferencing applications

%package        devel
Summary:        Development files for telepathy based video conferencing applications
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Obsoletes:      telepathy-farsight-devel

%description    devel
Telepathy client libraries for video conferencing applications

%prep
%setup -q -n %{name}-%{version}/telepathy-farstream

# disable-gtkdoc.patch
%patch0 -p1

%build
%autogen --disable-python --enable-static=no --disable-gtk-doc --disable-introspection
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc NEWS README COPYING
%{_libdir}/libtelepathy-farstream*.so.*

%files devel
%defattr(-,root,root,-)
#%doc %{_datadir}/gtk-doc/html/%{name}/
%{_libdir}/libtelepathy-farstream.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/telepathy-1.0/%{name}/

# This is work in progress!

%define snapshot r1084746
%define srcname networkmanagement
%define major 4
%define libname %mklibname nm %{major}
%define develname %mklibname -d nm

Name:           knetworkmanager
Summary:        KDE NetworkManager
Version:        4.4
Release:        %mkrel 0.%{snapshot}.1
Group:          System/Configuration/Networking
License:        GPLv2+
URL:            http://www.kde.org
#svn co svn://anonsvn.kde.org/home/kde/trunk/kdereview/networkmanagement/
Source0:        %{srcname}-%{snapshot}.tar.xz
BuildRequires:  libnm-util-devel
BuildRequires:  kdebase4-workspace-devel
Requires:       networkmanager
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
TODO

%package -n  %{libname}
Summary: Shared libraries used by %{name}

%description -n %{libname}
Shared libraries used by %{name}

%package -n %{develname}
Summary: Developmentn files for %{name}

%description -n %{develname}
Development files for %{name}

%prep
%setup -q -n %{srcname}

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_kde_bindir}/knetworkmanager
%{_kde_iconsdir}/oxygen/*/devices/*.png
%{_kde_iconsdir}/hicolor/*/apps/*.png
%{_kde_libdir}/kde4/*.so
%{_kde_libdir}/kde4/libexec/networkmanagement_configshell
%{_kde_libdir}/libsolidcontrolfuture.so
%{_kde_datadir}/applications/kde4/*.desktop
%{_kde_datadir}/apps/networkmanagement/networkmanagement.notifyrc
%{_kde_datadir}/autostart/kde4-knetworkmanager-autostart.desktop
%{_kde_datadir}/kde4/services/*.desktop
%{_kde_datadir}/kde4/services/kded/networkmanagement.desktop
%{_kde_datadir}/kde4/servicetypes/*.desktop


%files -n %{libname}
%{_kde_libdir}/libknm*.so.%{major}*

%files -n %{develname}
%{_kde_libdir}/libknm*.so

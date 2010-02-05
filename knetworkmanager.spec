# This is work in progress!

%define snapshot r1084746
%define srcname networkmanagement
%define major 4
%define libname %mklibname knm %{major}
%define develname %mklibname -d knm
%define novellvpn 0

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

%package -n plasma-applet-networkmanagement
Summary:	NetworkManager plasma applet
Group:		System/Configuration/Networking	
Requires:	networkmanager

%description -n plasma-applet-networkmanagement
%{summary}

%package -n  %{libname}
Summary: Shared libraries used by %{name}

%description -n %{libname}
Shared libraries used by %{name}

%package -n %{develname}
Summary: Development files for %{name}

%description -n %{develname}
Development files for %{name}

%package -n knetworkmanager-openvpn
Summary:        OpenVPN support for knetworkmanager
Group:          System/Configuration/Networking
Requires:       knetworkmanager = %{?epoch:%{epoch}:}%{version}
Requires:       NetworkManager-openvpn

%description -n knetworkmanager-openvpn
%{summary}.
%if %{novellvpn}

%package -n knetworkmanager-novellvpn
Summary:        Vpnc support for knetworkmanager
Group:          System/Configuration/Networking
Requires:       knetworkmanager = %{?epoch:%{epoch}:}%{version}-%{release}
# Does not exist in Mandriva
#Requires:       NetworkManager-novellvpn 

%description -n knetworkmanager-novellvpn
%{summary}.
%endif

%package -n knetworkmanager-vpnc
Summary:        Vpnc support for knetworkmanager
Group:          System/Configuration/Networking
Requires:       knetworkmanager = %{?epoch:%{epoch}:}%{version}-%{release} 
Requires:       NetworkManager-vpnc

%description -n knetworkmanager-vpnc
%{summary}.


%prep
%setup -q -n %{srcname}

%build
%cmake_kde4 -DDBUS_SYSTEM_POLICY_DIR=%{_sysconfdir}/dbus-1/system.d 
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%if ! %{novellvpn}
rm %{buildroot}%{_kde_libdir}/kde4/networkmanagement_novellvpnui.so
rm %{buildroot}%{_kde_datadir}/kde4/services/networkmanagement_novellvpnui.desktop
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc TODO DESIGN COPYING COPYING.LIB
%{_sysconfdir}/dbus-1/system.d/NetworkManager-kde4.conf
%{_kde_libdir}/kde4/kcm_networkmanagement.so
%{_kde_libdir}/kde4/networkmanagement_pptpui.so
%{_kde_libdir}/kde4/libexec/networkmanagement_configshell
%{_kde_iconsdir}/hicolor/*/*/*
%{_kde_iconsdir}/oxygen/*/*/*
%{_kde_appsdir}/networkmanagement/
%{_kde_datadir}/kde4/services/kcm_networkmanagement.desktop
%{_kde_datadir}/kde4/services/networkmanagement_pptpui.desktop
%{_kde_datadir}/kde4/servicetypes/networkmanagement_vpnuiplugin.desktop
%{_kde_bindir}/knetworkmanager
%{_kde_datadir}/autostart/kde4-knetworkmanager-autostart.desktop
%{_kde_datadir}/applications/kde4/knetworkmanager.desktop
# TODO: probably needs to be in a %lib packge, but cannot be in %libname because no major
%{_kde_libdir}/libsolidcontrolfuture.so

%files -n %{libname}
%defattr(-,root,root,-)
%{_kde_libdir}/libknm*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root,-)
%{_kde_libdir}/libknm*.so

%files -n knetworkmanager-openvpn
%defattr(-,root,root,-)
%{_kde_libdir}/kde4/networkmanagement_openvpnui.so
%{_kde_datadir}/kde4/services/networkmanagement_openvpnui.desktop

%if %{novellvpn}
%files -n knetworkmanager-novellvpn
%defattr(-,root,root,-)
%{_kde_libdir}/kde4/networkmanagement_novellvpnui.so
%{_kde_datadir}/kde4/services/networkmanagement_novellvpnui.desktop
%endif

%files -n knetworkmanager-vpnc
%defattr(-,root,root,-)
%{_kde_libdir}/kde4/networkmanagement_vpncui.so
%{_kde_datadir}/kde4/services/networkmanagement_vpncui.desktop

%files -n plasma-applet-networkmanagement
%defattr(-,root,root,-)
%{_kde_datadir}/kde4/services/plasma-applet-networkmanagement.desktop
%{_kde_datadir}/kde4/services/kcm_networkmanagement_tray.desktop
%{_kde_datadir}/kde4/services/kded/networkmanagement.desktop
%{_kde_libdir}/kde4/plasma_applet_networkmanagement.so
%{_kde_libdir}/kde4/kded_networkmanagement.so
%{_kde_libdir}/kde4/kcm_networkmanagement_tray.so


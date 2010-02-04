# This is work in progress!

%define snapshot r1084746
%define srcname networkmanagement
%define major 4
%define libname %mklibname knm %{major}
%define develname %mklibname -d knm

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

%package -n plasma-networkmanagement
Summary:	NetworkManager plasma applet
Group:		System/Configuration/Networking	
Requires:	networkmanager

%description -n plasma-networkmanagement
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

%package -n knetworkmanager-novellvpn
Summary:        Vpnc support for knetworkmanager
Group:          System/Configuration/Networking
Requires:       knetworkmanager = %{?epoch:%{epoch}:}%{version}-%{release}
# TODO
#Requires:       NetworkManager-

%description -n knetworkmanager-novellvpn
%{summary}.


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
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc TODO DESIGN COPYING COPYING.LIB
#TODO: check why this file does not exist
#%{_sysconfdir}/dbus-1/system.d/NetworkManager-kde4.conf
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

%files -n knetworkmanager-novellvpn
%defattr(-,root,root,-)
%{_kde_libdir}/kde4/networkmanagement_novellvpnui.so
%{_kde_datadir}/kde4/services/networkmanagement_novellvpnui.desktop

%files -n knetworkmanager-vpnc
%defattr(-,root,root,-)
%{_kde_libdir}/kde4/networkmanagement_vpncui.so
%{_kde_datadir}/kde4/services/networkmanagement_vpncui.desktop

%files -n plasma-networkmanagement
%defattr(-,root,root,-)
%{_kde_datadir}/kde4/services/plasma-applet-networkmanagement.desktop
%{_kde_datadir}/kde4/services/kcm_networkmanagement_tray.desktop
%{_kde_datadir}/kde4/services/kded/networkmanagement.desktop
%{_kde_libdir}/kde4/plasma_applet_networkmanagement.so
%{_kde_libdir}/kde4/kded_networkmanagement.so
%{_kde_libdir}/kde4/kcm_networkmanagement_tray.so


# This is work in progress!

%define snapshot r1084746
%define srcname networkmanagement

%define client_major 4
%define internals_major 4
%define service_major 4
%define ui_major 4
%define client_libname %mklibname knmclient %{client_major}
%define internals_libname %mklibname knminternals %{internals_major}
%define service_libname %mklibname knmservice %{service_major}
%define ui_libname %mklibname knmui %{ui_major}
%define develname %mklibname -d knetworkmanager
%define novellvpn 0


Name:           knetworkmanager
Summary:        KDE NetworkManager
Version:        4.4
Release:        %mkrel 0.%{snapshot}.1
Group:          Graphical desktop/KDE 
License:        GPLv2+
URL:            http://www.kde.org
#svn co svn://anonsvn.kde.org/home/kde/trunk/kdereview/networkmanagement/
Source0:        %{srcname}-%{snapshot}.tar.xz
BuildRequires:  libnm-util-devel
BuildRequires:  kdebase4-workspace-devel
Requires:       networkmanager
# TODO: probably a requires on solid networkmanager back-end is required too
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
KNetworkManager is a system tray applet for controlling network
connections on systems that use the NetworkManager daemon.

%package -n plasma-applet-networkmanagement
Summary:	NetworkManager plasma applet
Group:		Graphical desktop/KDE
Requires:	networkmanager

%description -n plasma-applet-networkmanagement
%{summary}

# TODO: fix summaries and descriptions
%package -n  %{client_libname}
Summary:	Shared libraries used by %{name}
Group:		System/Libraries 

%description -n %{client_libname}
Shared libraries used by %{name}

%package -n  %{internals_libname}
Summary:        Shared libraries used by %{name}
Group:          System/Libraries

%description -n %{internals_libname}
Shared libraries used by %{name}

%package -n  %{service_libname}
Summary:        Shared libraries used by %{name}
Group:          System/Libraries

%description -n %{service_libname}
Shared libraries used by %{name}

%package -n  %{ui_libname}
Summary:        Shared libraries used by %{name}
Group:          System/Libraries

%description -n %{ui_libname}
Shared libraries used by %{name}


%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/KDE and Qt 
Requires:	%{client_libname} = %{?epoch:%{epoch}:}%{version}
Requires:	%{internals_libname} = %{?epoch:%{epoch}:}%{version}
Requires:	%{service_libname} = %{?epoch:%{epoch}:}%{version}
Requires:	%{ui_libname} = %{?epoch:%{epoch}:}%{version}
Provides:	knetworkmanager-devel =  %{?epoch:%{epoch}:}%{version}-%{release}

%description -n %{develname}
Development files for %{name}

%package -n knetworkmanager-openvpn
Summary:        OpenVPN support for knetworkmanager
Group:          Graphical desktop/KDE 
Requires:       knetworkmanager = %{?epoch:%{epoch}:}%{version}
Requires:       networkmanager-openvpn

%description -n knetworkmanager-openvpn
%{summary}.
%if %{novellvpn}

%package -n knetworkmanager-novellvpn
Summary:        Vpnc support for knetworkmanager
Group:          Graphical desktop/KDE
Requires:       knetworkmanager = %{?epoch:%{epoch}:}%{version}
# Does not exist in Mandriva
#Requires:       networkmanager-novellvpn 

%description -n knetworkmanager-novellvpn
%{summary}.
%endif

%package -n knetworkmanager-vpnc
Summary:        Vpnc support for knetworkmanager
Group:          Graphical desktop/KDE 
Requires:       knetworkmanager = %{?epoch:%{epoch}:}%{version}
Requires:       networkmanager-vpnc

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

%files -n %{client_libname}
%defattr(-,root,root,-)
%{_kde_libdir}/libknmclient.so.%{client_major}*

%files -n %{internals_libname}
%defattr(-,root,root,-)
%{_kde_libdir}/libknminternals.so.%{internals_major}*

%files -n %{service_libname}
%defattr(-,root,root,-)
%{_kde_libdir}/libknmservice.so.%{service_major}*

%files -n %{ui_libname}
%defattr(-,root,root,-)
%{_kde_libdir}/libknmui.so.%{ui_major}*

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


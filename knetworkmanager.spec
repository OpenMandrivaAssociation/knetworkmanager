%define gitrev 90ed76441bc0a9946d653312c53a94cd683e1bc7
%define datetime 20110607
#define svnrev 
%define srcname networkmanagement

%define develname %mklibname -d knetworkmanager
%define novellvpn 0
%define pptp 1
%define strongswan 0

Name:           knetworkmanager
Summary:        KDE NetworkManager
Version:        0.9
Release:        0.%{datetime}.1
Epoch:		1
Group:          Graphical desktop/KDE
License:        (GPLv2 or GPLv3) and GPLv2+ and LGPLv2+ and LGPLv2 
URL:            http://www.kde.org
# The following needs modified create_tarball.rb with GIT
# support and corresponding config.ini entry; both are available
# at http://kenobi.mandriva.com/~bor/knetworkmanager/
#
# ./create_tarball.rb -n -a networkmanagement -c GITREV
# 
Source0:        %{srcname}-%{version}.tar.bz2

# upstream/review board patches

BuildRequires:  libnm-util-devel
BuildRequires:  kdebase4-workspace-devel
Requires:	%{name}-common
# plasmoid crashes if knetworkmanager is running
Conflicts:	plasma-applet-networkmanagement

%description
KNetworkManager is a system tray applet for controlling network
connections on systems that use the NetworkManager daemon.

#--------------------------------------------------------------------

%package -n %{name}-common
Summary:	Common files used by knetworkmanager
Group:		System/Configuration/Networking
Requires:	kdebase4-workspace
Requires:	networkmanager

%description -n %{name}-common
Common files used by knetworkmanager and plasma-applet-networkmanagement.

%files -n %{name}-common -f %{name}.lang
%{_sysconfdir}/dbus-1/system.d/NetworkManager-kde4.conf
%{_kde_libdir}/kde4/kcm_networkmanagement.so
%{_kde_libdir}/kde4/libexec/networkmanagement_configshell
%{_kde_datadir}/kde4/services/kcm_networkmanagement.desktop
%{_kde_datadir}/kde4/servicetypes/networkmanagement_vpnuiplugin.desktop
%{_kde_iconsdir}/oxygen/*/*/*
%{_kde_appsdir}/networkmanagement/

#--------------------------------------------------------------------

%package -n plasma-applet-networkmanagement
Summary:	NetworkManager plasma applet
Group:		Graphical desktop/KDE
Requires:	%{name}-common
Conflicts:	knetworkmanager
Obsoletes:      %name < 1:0.9-0.20110607.1

%description -n plasma-applet-networkmanagement
Network Management Plasma applet for controlling network
connections on systems that use the NetworkManager service.

%files -n plasma-applet-networkmanagement
%{_kde_datadir}/kde4/services/plasma-applet-networkmanagement.desktop
%{_kde_datadir}/kde4/services/plasma-engine-networkmanagement.desktop
%{_kde_datadir}/kde4/services/kcm_networkmanagement_tray.desktop
%{_kde_datadir}/kde4/services/kded/networkmanagement.desktop
%{_kde_libdir}/kde4/plasma_applet_networkmanagement.so
%{_kde_libdir}/kde4/plasma_engine_networkmanagement.so
%{_kde_libdir}/kde4/kded_networkmanagement.so
%{_kde_libdir}/kde4/kcm_networkmanagement_tray.so

#--------------------------------------------------------------------

%define knmclient_major 4
%define libknmclient %mklibname knmclient %{knmclient_major}

%package -n %{libknmclient}
Summary:	libknclient library used by %{name}
Group:		System/Libraries 

%description -n %{libknmclient}
libknclient library used by %{name}.

%files -n %{libknmclient}
%{_kde_libdir}/libknmclient.so.%{knmclient_major}*

#--------------------------------------------------------------------

%define libkinternals_major 4
%define libknminternals %mklibname knminternals %{libkinternals_major}

%package -n %{libknminternals}
Summary:        libkninternals library used by %{name}
Group:          System/Libraries

%description -n %{libknminternals}
libkninternals library used by %{name}

%files -n %{libknminternals}
%{_kde_libdir}/libknminternals.so.%{libkinternals_major}*

#--------------------------------------------------------------------

%define libservice_major 4
%define libknmservice %mklibname knmservice %{libservice_major}

%package -n %{libknmservice}
Summary:        libknservice library used by %{name}
Group:          System/Libraries

%description -n %{libknmservice}
libknservice library used by %{name}.

%files -n %{libknmservice}
%{_kde_libdir}/libknmservice.so.%{libservice_major}*

#--------------------------------------------------------------------
%define libknmui_major 4
%define libknmui %mklibname knmui %{libknmui_major}

%package -n %{libknmui}
Summary:        libknui library used by %{name}
Group:          System/Libraries

%description -n %{libknmui}
libknui library used by %{name}.

%files -n %{libknmui}
%{_kde_libdir}/libknmui.so.%{libknmui_major}*

#--------------------------------------------------------------------
%define libsolidcontrolfuture %mklibname solidcontrolfuture

%package -n %{libsolidcontrolfuture}
Summary:        solidcontrolfuture library used by %{name}
Group:          System/Libraries

%description -n %{libsolidcontrolfuture}
libsolidcontrolfuture library used by %{name}.

%files -n %{libsolidcontrolfuture}
%{_kde_libdir}/libsolidcontrolfuture.so

#--------------------------------------------------------------------
%define libknm_nm %mklibname knm_nm

%package -n %{libknm_nm}
Summary:	NetworkManager back-end for %{name}
Group:		System/Libraries

%description -n %{libknm_nm}
NetworkManager back-end for %{name}.

%files -n %{libknm_nm}
%{_kde_libdir}/libknm_nm.so

#--------------------------------------------------------------------

%package -n %{develname}
Summary:       Development files for %{name}                                             
Group:         Development/KDE and Qt                                                    
Requires:      %{libknmclient} = %{version}                         
Requires:      %{libknminternals} = %{version}                      
Requires:      %{libknmservice} = %{version}                        
Requires:      %{libknmui} = %{version}                             
Provides:      knetworkmanager-devel =  %{version}-%{release} 

%description -n %{develname}                                                             
Development files for %{name}   

%files -n %{develname}
%{_kde_libdir}/libknmclient.so
%{_kde_libdir}/libknminternals.so
%{_kde_libdir}/libknmservice.so
%{_kde_libdir}/libknmui.so

#--------------------------------------------------------------------

%package -n knetworkmanager-openvpn
Summary:        OpenVPN support for knetworkmanager
Group:          Graphical desktop/KDE 
Requires:       networkmanager-openvpn

%description -n knetworkmanager-openvpn
%{summary}.

%files -n knetworkmanager-openvpn
%{_kde_libdir}/kde4/networkmanagement_openvpnui.so
%{_kde_datadir}/kde4/services/networkmanagement_openvpnui.desktop

#--------------------------------------------------------------------

%if %{novellvpn}

%package -n knetworkmanager-novellvpn
Summary:        Vpnc support for knetworkmanager
Group:          Graphical desktop/KDE

%description -n knetworkmanager-novellvpn
%{summary}.

%files -n knetworkmanager-novellvpn
%{_kde_libdir}/kde4/networkmanagement_novellvpnui.so
%{_kde_datadir}/kde4/services/networkmanagement_novellvpnui.desktop

%endif

#--------------------------------------------------------------------

%if %{pptp}

%package -n knetworkmanager-pptp
Summary:        Pptp support for knetworkmanager
Group:          Graphical desktop/KDE
Requires:       networkmanager-pptp 

%description -n knetworkmanager-pptp
%{summary}.

%files -n knetworkmanager-pptp
%{_kde_libdir}/kde4/networkmanagement_pptpui.so
%{_kde_datadir}/kde4/services/networkmanagement_pptpui.desktop

%endif

#--------------------------------------------------------------------

%if %{strongswan}

%package -n knetworkmanager-strongswan
Summary:        strongSwan support for knetworkmanager
Group:          Graphical desktop/KDE 

%description -n knetworkmanager-strongswan
%{summary}.

%files -n knetworkmanager-strongswan
%{_kde_libdir}/kde4/networkmanagement_strongswanui.so
%{_kde_datadir}/kde4/services/networkmanagement_strongswanui.desktop
%endif

#--------------------------------------------------------------------


%package -n knetworkmanager-vpnc
Summary:        Vpnc support for knetworkmanager
Group:          Graphical desktop/KDE 
Requires:       networkmanager-vpnc

%description -n knetworkmanager-vpnc
%{summary}.

%files -n knetworkmanager-vpnc
%{_kde_libdir}/kde4/networkmanagement_vpncui.so
%{_kde_datadir}/kde4/services/networkmanagement_vpncui.desktop

#--------------------------------------------------------------------


%prep
%setup -q -n %{srcname}-%{version}
%apply_patches

%build
%cmake_kde4 \
	-DDBUS_SYSTEM_POLICY_DIR=%{_sysconfdir}/dbus-1/system.d \
	-DINSTALL_KNM_AUTOSTART=ON
%make

%install
%makeinstall_std -C build

%if ! %{novellvpn}
rm %{buildroot}%{_kde_libdir}/kde4/networkmanagement_novellvpnui.so
rm %{buildroot}%{_kde_datadir}/kde4/services/networkmanagement_novellvpnui.desktop
%endif

%if ! %{pptp}
rm %{buildroot}%{_kde_libdir}/kde4/networkmanagement_pptpui.so
rm %{buildroot}%{_kde_datadir}/kde4/services/networkmanagement_pptpui.desktop
%endif

%if ! %{strongswan}
rm %{buildroot}%{_kde_libdir}/kde4/networkmanagement_strongswanui.so
rm %{buildroot}%{_kde_datadir}/kde4/services/networkmanagement_strongswanui.desktop
%endif

%find_lang %{name} %{name} lib%{name} plasma_applet_networkmanagement


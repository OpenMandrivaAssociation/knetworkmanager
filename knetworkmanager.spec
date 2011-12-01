%define gitrev aa2e2a7f61234f9790d046cfd761e110bb2750a2
%define datetime 20111130
#define svnrev 
%define srcname networkmanagement

%define develname %mklibname -d knetworkmanager
%define novellvpn 0
%define pptp 1
%define strongswan 0
%define openvn 1
%define vpnc 1
%define openconnect 1

Name:           knetworkmanager
Summary:        KDE NetworkManager
Version:        0.9
Release:        1.%{datetime}.1
Epoch:		1
Group:          Graphical desktop/KDE
License:        (GPLv2 or GPLv3) and GPLv2+ and LGPLv2+ and LGPLv2 
URL:            http://www.kde.org
#Source get from git
# git clone git://anongit.kde.org/networkmanagement 
# git archive --format=tar --prefix=networkmanagement/ --remote=git://anongit.kde.org/networkmanagement v0.9.0_rc3 | xz -9 >  networkmanagement-20111022.tar.xz                                                                            
Source0:        %{srcname}-%{datetime}.tar.xz
Source1:        %{srcname}-l10n.tar.xz
Patch0:		networkmanagement-0.9-useversion.patch
Patch1:		networkmanagement-0.9-compile-po-files.patch

BuildRequires:  pkgconfig(libnm-util) >= 0.9
BuildRequires:  mobile-broadband-provider-info
BuildRequires:  kdebase4-workspace-devel
%if %{openconnect}
BuildRequires:	pkgconfig(openconnect) >= 3.10
%endif
Requires:	%{name}-common
# plasmoid crashes if knetworkmanager is running
Requires:	plasma-applet-networkmanagement

%description
KNetworkManager is a system tray applet for controlling network
connections on systems that use the NetworkManager daemon.

%files
%doc TODO DESIGN COPYING COPYING.LIB README.install.urpmi

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

%description -n plasma-applet-networkmanagement
Network Management Plasma applet for controlling network
connections on systems that use the NetworkManager service.

%files -n plasma-applet-networkmanagement -f plasma_applet_networkmanagement.lang
%{_kde_libdir}/kde4/plasma_applet_networkmanagement.so
%{_kde_libdir}/kde4/plasma_engine_networkmanagement.so
%{_kde_libdir}/kde4/kded_networkmanagement.so
%{_kde_libdir}/kde4/solid_networkmanager09.so
%{_kde_libdir}/kde4/kcm_networkmanagement_tray.so
%{_kde_services}/solidbackends/solid_networkmanager09.desktop
%{_kde_services}/plasma-applet-networkmanagement.desktop
%{_kde_services}/plasma-engine-networkmanagement.desktop
%{_kde_services}/kcm_networkmanagement_tray.desktop
%{_kde_services}/kded/networkmanagement.desktop
%{_kde_servicetypes}/solidnetworkmanagernm09.desktop
%{_kde_appsdir}/desktoptheme/default/icons/network2.svgz


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

%define libsolidcontrolnm_major 4
%define libsolidcontrolnm %mklibname solidcontrolnm %{libsolidcontrolnm_major}

%package -n %{libsolidcontrolnm}
Summary:	libsolidcontrol library for networkmanager 0.9
Group:		System/Libraries

%description -n %{libsolidcontrolnm}
libsolidcontrol library for networkmanager 0.9

%files -n %{libsolidcontrolnm}
%{_kde_libdir}/libsolidcontrolnm09.so.%{libsolidcontrolnm_major}*

#-------------------------------------------------------------------------

%define libsolidcontrolnm_ifaces_major 4
%define libsolidcontrolnm_ifaces %mklibname solidcontrolnmifaces %{libsolidcontrolnm_ifaces_major}

%package -n %{libsolidcontrolnm_ifaces}
Summary:	libsolidcontrol library for networkmanager 0.9
Group:		System/Libraries

%description -n %{libsolidcontrolnm_ifaces}
libsolidcontrol library for networkmanager 0.9

%files -n %{libsolidcontrolnm_ifaces}
%{_kde_libdir}/libsolidcontrolnm09ifaces.so.%{libsolidcontrolnm_ifaces_major}*


#-------------------------------------------------------------------------

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
%define libsolidcontrolfuture_major 4
%define libsolidcontrolfuture %mklibname solidcontrolfuture %{libsolidcontrolfuture_major}

%package -n %{libsolidcontrolfuture}
Summary:        solidcontrolfuture library used by %{name}
Group:          System/Libraries

%description -n %{libsolidcontrolfuture}
libsolidcontrolfuture library used by %{name}.

%files -n %{libsolidcontrolfuture}
%{_kde_libdir}/libsolidcontrolfuture.so.%{libsolidcontrolfuture_major}*

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
Requires:      %{libknmclient} = %{EVRD}                         
Requires:      %{libknminternals} = %{EVRD}
Requires:      %{libknmservice} = %{EVRD}
Requires:      %{libknmui} = %{EVRD}                             
Requires:	%{libsolidcontrolfuture} = %{EVRD}
Provides:      knetworkmanager-devel = %{EVRD}

%description -n %{develname}                                                             
Development files for %{name}   

%files -n %{develname}
%{_kde_libdir}/libknmclient.so
%{_kde_libdir}/libknminternals.so
%{_kde_libdir}/libknmservice.so
%{_kde_libdir}/libknmui.so
%{_kde_libdir}/libsolidcontrolfuture.so
%{_kde_includedir}/solid/controlnm09/
%{_kde_libdir}/libsolidcontrolnm09.so
%{_kde_libdir}/libsolidcontrolnm09ifaces.so

#--------------------------------------------------------------------

%if %{openvn}

%package -n knetworkmanager-openvpn
Summary:        OpenVPN support for knetworkmanager
Group:          Graphical desktop/KDE 
Requires:       networkmanager-openvpn

%description -n knetworkmanager-openvpn
%{summary}.

%files -n knetworkmanager-openvpn
%{_kde_libdir}/kde4/networkmanagement_openvpnui.so
%{_kde_datadir}/kde4/services/networkmanagement_openvpnui.desktop

%endif
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

%if %{vpnc}

%package -n knetworkmanager-vpnc
Summary:        Vpnc support for knetworkmanager
Group:          Graphical desktop/KDE 
Requires:       networkmanager-vpnc

%description -n knetworkmanager-vpnc
%{summary}.

%files -n knetworkmanager-vpnc
%{_kde_libdir}/kde4/networkmanagement_vpncui.so
%{_kde_datadir}/kde4/services/networkmanagement_vpncui.desktop
%endif
#-------------------------------------------------------------------
%if %{openconnect}
%package openconnect
Summary: Openconnect support for %name
Group: Graphical desktop/KDE
Requires: openconnect

%description openconnect
Openconnect plugin for %name

%files openconnect
%_kde_libdir/kde4/networkmanagement_openconnectui.so
%_kde_services/networkmanagement_openconnectui.desktop

%endif
#--------------------------------------------------------------------


%prep
%setup -q -n %{srcname} -a1
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

%if ! %{openvn}
rm %{buildroot}%{_kde_libdir}/kde4/networkmanagement_openvpnui.so
rm %{buildroot}%{_kde_datadir}/kde4/services/networkmanagement_openvpnui.desktop
%endif

%if ! %{vpnc}
rm %{buildroot}%{_kde_libdir}/kde4/networkmanagement_vpncui.so
rm %{buildroot}%{_kde_datadir}/kde4/services/networkmanagement_vpncui.desktop
%endif

%find_lang %{name} lib%{name} %{name}.lang
%find_lang plasma_applet_networkmanagement

cat > README.install.urpmi << EOF
The monolithic client is not built anymore by upstream.
You need to use now the plasma applet.

Regards,

EOF

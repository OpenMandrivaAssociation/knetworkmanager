#define gitrev aa2e2a7f61234f9790d046cfd761e110bb2750a2
#define datetime 20120122
#define svnrev 
%define srcname networkmanagement

%define develname %mklibname -d knetworkmanager
%define novellvpn 0
%define pptp 1
%define strongswan 0
%define openvn 1
%define vpnc 1
%define openconnect 0

Name:           knetworkmanager
Summary:        KDE NetworkManager
Version:        0.9.0.5
Release:        2
Epoch:		2
Group:          Graphical desktop/KDE
License:        (GPLv2 or GPLv3) and GPLv2+ and LGPLv2+ and LGPLv2 
URL:            http://www.kde.org
#http://lamarque-lvs.blogspot.ru/
#Source get from git
# git clone git://anongit.kde.org/networkmanagement 
# git archive --format=tar --prefix=networkmanagement/ --remote=git://anongit.kde.org/networkmanagement v0.9.0_rc3 | xz -9 >  networkmanagement-20111022.tar.xz                                                                            
Source0:        http://download.kde.org/unstable/networkmanagement/0.9.0.5/src/%{srcname}-%{version}.tar.bz2
Source100:	knetworkmanager.rpmlintrc
#Source1:	networkmanagement-l10n.tar.bz2
Patch0:		networkmanagement-0.9-useversion.patch
Patch1:		networkmanagement-0.9-compile-po-files.patch
#Patch2:		networkmanagement-0.9.0.2-applet.desktop.patch
#Patch3:		networkmanagement-0.9.0.2-kcm.desktop.patch
Patch4:		networkmanagement-0.9.0.2-ui-fix.patch
BuildRequires:  pkgconfig(libnm-util) >= 0.9
BuildRequires:  pkgconfig(libnm-glib) >= 0.9
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
%{_kde_libdir}/kde4/kcm_networkmanagement.so
%{_kde_libdir}/kde4/libexec/networkmanagement_configshell
%{_kde_services}/kcm_networkmanagement.desktop
%{_kde_servicetypes}/networkmanagement_vpnuiplugin.desktop
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
%{_datadir}/locale/*/*/solidcontrolnm09*

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
%find_lang solidcontrolnm09

cat > README.install.urpmi << EOF
The monolithic client is not built anymore by upstream.
You need to use now the plasma applet.

Regards,

EOF


%changelog
* Sun May 29 2012 thesaint <thesaint> 2:0.9.0.2-3
- network-applet: fixed network checkboxs' text color

* Sun May 27 2012 akdengi <akdengi> 2:0.9.0.2-2
- new version 0.9.0.2
- update l10n source
- fix source URL
- add russian description to .desktop file

* Thu Dec 01 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 1:0.9-1.20111130.2
+ Revision: 737053
- bump to move to main

* Thu Dec 01 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 1:0.9-1.20111130.1
+ Revision: 735870
- update to latest and sync most of spec with mageia

* Tue Jun 07 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:0.9-0.20110607.1
+ Revision: 683062
- New snapshot
  Remove merged patches
  monolithic gui is no more

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1:0.9-0.20110314.2
+ Revision: 666032
- mass rebuild

* Tue Mar 15 2011 Andrey Borzenkov <arvidjaar@mandriva.org> 1:0.9-0.20110314.1
+ Revision: 644855
- new GIT snapshot (11645bb)
- P100: vpnc secrets were stored even when set to "ask aways"
- P101: do not store plain text secrets when DontStore is requested

* Fri Mar 11 2011 Andrey Borzenkov <arvidjaar@mandriva.org> 1:0.9-0.20110311.1
+ Revision: 643813
- GIT e14fea: fixes wireless permanently disabled after rfkill

* Fri Mar 04 2011 Andrey Borzenkov <arvidjaar@mandriva.org> 1:0.9-0.20110304.1
+ Revision: 641588
- networkmanagement switched to GIT. Use date of latest commit in
  release string for lack of anything better (suggested by Thomas
  Backlund)
- increase Epoch to ensure update from previous release scheme
- latest GIT snapshot eaf856
- P0: drop, intergrated upstream

* Tue Feb 01 2011 Eugeni Dodonov <eugeni@mandriva.com> 0.9-0.r1201724.3
+ Revision: 634844
- Networkmanager-pptp is among us now, rebuilding.

* Fri Dec 31 2010 Funda Wang <fwang@mandriva.org> 0.9-0.r1201724.2mdv2011.0
+ Revision: 626778
- fix requires

* Sun Nov 28 2010 Andrey Borzenkov <arvidjaar@mandriva.org> 0.9-0.r1201724.1mdv2011.0
+ Revision: 602509
- new snapshot - fix system connection display

* Sat Nov 20 2010 Andrey Borzenkov <arvidjaar@mandriva.org> 0.9-0.r1198724.1mdv2011.0
+ Revision: 599185
- new snapshot - yet another attempt to fix crash on NM restart
- allow build on relases before 2011.0

  + Eugeni Dodonov <eugeni@mandriva.com>
    - Fix file conflict on 2010.1.

* Thu Nov 04 2010 Andrey Borzenkov <arvidjaar@mandriva.org> 0.9-0.r1192577.2mdv2011.0
+ Revision: 593205
- pptp does not belong to -common and does not exist in Mandriva currently

* Thu Nov 04 2010 Andrey Borzenkov <arvidjaar@mandriva.org> 0.9-0.r1192577.1mdv2011.0
+ Revision: 593188
- update to new snapshot in attempt to fix crash on NM restart
  package translations too

* Thu Jul 15 2010 Andrey Borzenkov <arvidjaar@mandriva.org> 0.9-0.r1148396.1mdv2011.0
+ Revision: 553701
- plasma applet really works (and is preferred) now so remove requires
  on monolithic knetworkmanager from VPN plugins
- patch0: support vpnc always_ask secrets (KDE #244416)
- new snapshot

* Sat Feb 06 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.9-0.r1084746.1mdv2010.1
+ Revision: 501439
- Change to fit kde specs layout

  + Frederik Himpe <fhimpe@mandriva.org>
    - Use version 0.9, as indicated insource code (thanks Anssi)
    - No need for versioned conflicts
    - Use versioned conflicts
    - Use Fedora's license tag
    - Make knetworkmanager and plasma-applet-networkmanagement conflict
      because they cannot be run together. Put common files in
      knetworkmanager-common.
    - Add Requires: kde-solid-networkmanager
    - Put shared libraries which don't have major also in separate packages
    - Split libraries in separate packages
    - Fix groups and requires
    - Fix name of plasma applet package
    - Don't package novellvpn stuff because we don't have
      networkmanager-novellvpn
    - Fix installation of dbus system policy file
    - Split package
    - Many other SPEC file fixes
    - import knetworkmanager



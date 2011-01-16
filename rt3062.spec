%define SourceName DPO_RT3562_3592_3062_LinuxSTA_V2.4.1.1_20101217

Name:		rt3062
Version:	2.4.1.1
Release:	1%{?dist}
Summary:	Common files for RaLink RT3062 PCI/mPCI/CB/PCIe (RT3060/RT3062/RT3562/RT3592) kernel driver
Group:		System Environment/Kernel
License:	GPLv2+
URL:		http://www.ralinktech.com/support.php?s=2
# No direct links anymore. The sources are downloaded from the above page.
Source0:	%{SourceName}.tgz
Source2:	suspend.sh
# Blacklist the module shipped with kernel
Source3:	blacklist-rt2800usb.conf
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:	noarch
Provides:	%{name}-kmod-common = %{version}
Requires:	%{name}-kmod >= %{version}

%description
This package contains the linux kernel module files for the Ralink RT3062 PCI/mPCI/CB/PCIe 
(RT3060/RT3062/RT3562/RT3592) driver for WiFi, a linux device driver for 
USB 802.11a/b/g universal NIC cards that use Ralink RT3062 PCI/mPCI/CB/PCIe 
(RT3060/RT3062/RT3562/RT3592) chipsets.

%prep
%setup -q -n %{SourceName}

sed 's|\r||' sta_ate_iwpriv_usage.txt > tmpfile
iconv -f JOHAB -t UTF8 tmpfile -o tmpfile2
touch -r sta_ate_iwpriv_usage.txt tmpfile2
mv -f tmpfile2 sta_ate_iwpriv_usage.txt

iconv -f JOHAB -t UTF8 README_STA_pci > tmpfile
touch -r README_STA_pci tmpfile
mv -f tmpfile README_STA_pci

chmod -x *.txt README_STA_pci

%build
sleep 5s

%install
rm -rf $RPM_BUILD_ROOT
install -dm 755 $RPM_BUILD_ROOT/%{_sysconfdir}/Wireless/RT3062STA/
install -pm 0644 RT2860STA.dat $RPM_BUILD_ROOT/%{_sysconfdir}/Wireless/RT3062STA/RT3062STA.dat
install -pm 0644 RT2860STACard.dat $RPM_BUILD_ROOT/%{_sysconfdir}/Wireless/RT3062STA/RT3062STACard.dat
cp -a %{SOURCE2} .
%if 0%{fedora} < 14
install -dm 755 $RPM_BUILD_ROOT/%{_sysconfdir}/modprobe.d/
cp -a %{SOURCE3} $RPM_BUILD_ROOT/%{_sysconfdir}/modprobe.d/
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_STA_pci *.txt suspend.sh
%dir %{_sysconfdir}/Wireless
%dir %{_sysconfdir}/Wireless/RT3062STA
%config(noreplace) %{_sysconfdir}/Wireless/RT3062STA/RT3062STA*.dat
%if 0%{fedora} < 14
%config(noreplace) %{_sysconfdir}/modprobe.d/blacklist-rt2800usb.conf
%endif

%changelog
* Sun Jan 16 2011 Alexei Panov <elemc [AT] atisserv [DOT] ru> - 2.4.1.1-1
- changed for RT3062 sources from rt2870 package

* Sat Jul 10 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 2.4.0.1-1
- Update to 2.4.0.1

* Sat Jun 26 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 2.4.0.0-1
- Update to 2.4.0.0

* Fri Dec 04 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 2.1.2.0-2.1
- Blacklist kernel's rt2800usb module

* Wed Jun 17 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 2.1.2.0-2
- Modify RT2870STA.dat to support WPA2 (RFBZ #664)

* Fri May 22 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 2.1.2.0-1
- version update (2.1.2.0)

* Sat Apr 24 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 2.1.1.0-1
- version update (2.1.1.0)

* Thu Mar 26 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 2.1.0.0-1
- Rebuild for 2.1.0.0
- Move suspend.sh to %%doc
- Fix description: rt2870 is USB only

* Tue Mar 10 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.4.0.0-3
- Add suspend script (RPMFusion BZ#199)

* Tue Oct 07 2008 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.4.0.0-2
- Re-own %%{_sysconfdir}/Wireless/

* Tue Oct 07 2008 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.4.0.0-1.1
- Install RT2870STA.dat at the "right" place

* Sat Oct 04 2008 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.4.0.0-1
- Rebuild for 1.4.0.0
- Added iwpriv_usage.txt into package

* Sat Oct 04 2008 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 1.3.1.0-4
- Various small adjustments

* Sat Sep 27 2008 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.3.1.0-3
- Re-wrote the description, removed supported hardware info.
- Fixed the defattr.
- Added the /etc/Wireless/RT2870STA.dat file that comes with the source to the rpm.
- Rename SourceDir to SourceName

* Thu Sep 22 2008 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.3.1.0-2
- Some cleanup in the SPEC file to match standards
- Fix rpmlint's encoding complaints with doc files
- License is GPLv2+

* Thu Sep 20 2008 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.3.1.0-1
- Initial build.

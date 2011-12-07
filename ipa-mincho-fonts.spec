%global		priority	65-2
%global		fontname	ipa-mincho
%global		fontconf	%{priority}-%{fontname}.conf
%global		archiveversion	00302
%global		archivename	ipam%{archiveversion}

Name:		%{fontname}-fonts
Version:	003.02
Release:	3.1%{?dist}
Summary:	Japanese Mincho-typeface OpenType font by IPA

Group:		User Interface/X
License:	IPA
URL:		http://ossipedia.ipa.go.jp/ipafont/
Source0:	http://info.openlab.ipa.go.jp/ipafont/fontdata/%{archivename}.zip
Source1:	%{name}-fontconfig.conf
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildArch:	noarch
BuildRequires:	fontpackages-devel
Requires:	fontpackages-filesystem

%description
IPA Font is a Japanese OpenType fonts that is JIS X 0213:2004
compliant, provided by Information-technology Promotion Agency, Japan.

This package contains Mincho style font.

%prep
%setup -q -n %{archivename}


%build

%install
rm -rf $RPM_BUILD_ROOT

install -m 0755 -d $RPM_BUILD_ROOT%{_fontdir}
install -m 0644 -p *.ttf $RPM_BUILD_ROOT%{_fontdir}

install -m 0755 -d	$RPM_BUILD_ROOT%{_fontconfig_templatedir}	\
			$RPM_BUILD_ROOT%{_fontconfig_confdir}
install -m 0644 -p	%{SOURCE1}	\
			$RPM_BUILD_ROOT%{_fontconfig_templatedir}/%{fontconf}

ln -s	%{_fontconfig_templatedir}/%{fontconf}	\
	$RPM_BUILD_ROOT%{_fontconfig_confdir}/%{fontconf}

%clean
rm -rf $RPM_BUILD_ROOT


%_font_pkg -f %{fontconf} *.ttf

%doc Readme_%{archivename}.txt IPA_Font_License_Agreement_v1.0.txt


%changelog
* Thu May 20 2010 Akira TAGOH <tagoh@redhat.com> - 003.02-3.1
- Backport from Fedora.
- Improve the fontconfig config file to match ja as well. (#586840)

* Mon Apr 19 2010 Akira TAGOH <tagoh@redhat.com> - 003.02-3
- Get rid of compare="contains".

* Fri Apr 16 2010 Akira TAGOH <tagoh@redhat.com> - 003.02-2
- Get rid of binding="same" from the fontconfig config file. (#578021)

* Wed Feb 17 2010 Akira TAGOH <tagoh@redhat.com> - 003.02-1
- New upstream release.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 003.01-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun  5 2009 Akira TAGOH <tagoh@redhat.com> - 003.01-3
- Disable hinting.

* Wed Apr 22 2009 Akira TAGOH <tagoh@redhat.com> - 003.01-2
- Correct the source URL.

* Tue Apr 21 2009 Akira TAGOH <tagoh@redhat.com> - 003.01-1
- Initial package.


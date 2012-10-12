Summary:	Interest Calculator
Name:		cashflo
Version:	001
Release:	1.otl%{?dist}
Group:		Applications/Productivity
License:	GPLv2
URL:		https://github.com/opentechlabs/cashflo
Vendor:		OpenTech Labs
Packager:	Andrew Clayton <andrew@opentechlabs.co.uk>
Source0:	cashflo-%{version}.tar
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:	gtk3-devel
Requires:	gtk3

%description
A simple application to tell whether it's better to pay interest on
overdraft or to pay the merchant service charge.

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -Dp -m0755 cashflo $RPM_BUILD_ROOT/%{_bindir}/cashflo
install -Dp -m0644 cashflo.desktop $RPM_BUILD_ROOT/%{_datadir}/applications/cashflo.desktop
install -Dp -m0644 cashflo.png $RPM_BUILD_ROOT/%{_datadir}/pixmaps/cashflo.png
install -Dp -m0644 cashflo.glade $RPM_BUILD_ROOT/%{_datadir}/cashflo/cashflo.glade

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/cashflo
%{_datadir}/applications/cashflo.desktop
%{_datadir}/pixmaps/cashflo.png
%{_datadir}/cashflo/cashflo.glade
%doc README COPYING

%changelog
* Fri Oct 12 2012 Andrew Clayton <andrew@opentechlabs.co.uk> - 001-1.otl
- Initial release

Summary:	Binflash (NEC version) - universal firmware flasher for binary firmwares
Name:		binflash
Version:	1.02
Release:	0.1
License:	? (closed source)
Group:		Applications/System
Source0:	necflash_linux.tgz
# Source0-md5:	ffa1d581d6bea339b3806cd40d83648d
URL:		http://binflash.cdfreaks.com
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Binflash is a collection of tools you may use in order to flash your
DVD burner with a binary firmware file (some executable flashers are
also supported) or to dump the Flash ROM of your burner back to disc.
You should be able to work with all devices that are currently
accessible in your operating system, even if the drives are attached
via Firewire or USB.

Disclaimer:

By using this program and accepting the disclaimer you accept that
neither the authors of this programs nor CDFreaks.com can be held
responsible for any damages caused by using Binflash. If you damage
your drive by using this flasher or any experimental firmwares, do not
RMA your drive but buy a new one!

%prep
%setup -qcn binflash

%install
rm -rf $RPM_BUILD_ROOT

install -D necflash \
	$RPM_BUILD_ROOT%{_sbindir}/necflash

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/necflash

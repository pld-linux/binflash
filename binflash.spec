#
# NOTE:
#		- firmwares available at http://liggydee.cdfreaks.com/page/
#
Summary:	Binflash (NEC version) - universal firmware flasher for binary firmwares
Summary(pl.UTF-8):	Binflash (wersja NEC) - uniwersalne narzędzie do uaktualniania binarnych firmware
Name:		binflash
Version:	1.38
Release:	2
License:	Freeware
Group:		Applications/System
Source0:	necflash_linux.tgz
# Source0-md5:	e9912abe254b697d2511c0a23f27b7cb
URL:		http://binflash.cdfreaks.com/
ExclusiveArch:	%{ix86} %{x8664}
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
neither the authors of these programs nor CDFreaks.com can be held
responsible for any damages caused by using Binflash. If you damage
your drive by using this flasher or any experimental firmwares, do not
RMA your drive but buy a new one!

%description -l pl.UTF-8
Binflash to zestaw narzędzi do uaktualnienia pamięci flash w
nagrywarkach DVD za pomocą pliku binarnego z firmware (obsługiwane są
także niektóre wykonywalne pliki z firmware) oraz zrzucania zawartości
Flash ROM-u nagrywarki z powrotem na dysk. Narzędzia powinny działać
ze wszystkimi urządzeniami aktualnie dostępnymi w systemie
operacyjnym, nawet tymi podłączonymi poprzez Firewire lub USB.

Uwaga:

Używając ten program i przyjmując to oświadczenie akceptujemy, że ani
autorzy tych programów ani CDFreaks.com nie są odpowiedzialni za
żadne uszkodzenia spowodowane używaniem Binflasha. W przypadku
uszkodzenia urządzenia poprzez użycie tego narzędzia lub jakiegoś
eksperymentalnego firmware pozostaje tylko zakup nowego napędu.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT

install -D necflash \
	$RPM_BUILD_ROOT%{_sbindir}/necflash

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/necflash

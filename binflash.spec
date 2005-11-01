Summary:	Binflash (NEC version) - universal firmware flasher for binary firmwares
Summary(pl):	Binflash (wersja NEC) - uniwersalne narzêdzie do uaktualniania binarnych firmware
Name:		binflash
Version:	1.22
Release:	0.1
License:	? (closed source)
Group:		Applications/System
Source0:	http://binflash.cdfreaks.com/download/1/2/necflash_linux.tgz
# NoSource0-md5:	2f7d6ad41faa3087fe25cbb32f4ce278
URL:		http://binflash.cdfreaks.com/
ExclusiveArch:	%{ix86}
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

%description -l pl
Binflash to zestaw narzêdzi do uaktualnienia pamiêci flash w
nagrywarkach DVD za pomoc± pliku binarnego z firmware (obs³ugiwane s±
tak¿e niektóre wykonywalne pliki z firmware) oraz zrzucania zawarto¶ci
Flash ROM-u nagrywarki z powrotem na dysk. Narzêdzia powinny dzia³aæ
ze wszystkimi urz±dzeniami aktualnie dostêpnymi w systemie
operacyjnym, nawet tymi pod³±czonymi poprzez Firewire lub USB.

Uwaga:

U¿ywaj±c ten program i przyjmuj±c to o¶wiadczenie akceptujemy, ¿e ani
autorzy tych programów ani CDFreaks.com nie s± odpowiedzialni za
¿adne uszkodzenia spowodowane u¿ywaniem Binflasha. W przypadku
uszkodzenia urz±dzenia poprzez u¿ycie tego narzêdzia lub jakiego¶
eksperymentalnego firmware pozostaje tylko zakup nowego napêdu.

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

# MULTube

* Předmět: MUL
* Zadání: Databáze videozáznamů
* Řešitelé:
	* Zdeněk Biberle, xbiber00
	* Josef Řídký, xridky00
* Datum vypracování: 12. 05. 2015

## Zadání

Vytvořte webové rozhraní pro sdílení souborů s videozáznamy. Rozhraní by mělo umožnit třídění souborů podle kategorií, zobrazení náhledů a případně dalších informací o nahrávkách. Aplikace by měla mít dvě varianty rozhraní, jedno pro administraci a druhé pro prohlížení/stahování záznamů.

## Řešení

Aplikace je koncipována jako webová aplikace podobná známé službě YouTube. Pro implementaci byl zvolen framework Django. Pro zpracování video souborů byly zvoleny nástroje `ffmpeg` a `ffprobe`.

### Schopnosti aplikace

Aplikace obsahuje následující funkcionalitu:
* Registrace a přihlašování uživatelů
* Nahrávání videí s doplňujícími informacemi jako jsou název, popis a tagy
* Editace popisu a názvu videí
* Prohlížení nejnovějších videí
* Prohlížení nejčastějších tagů a videí označených těmito tagy
* Vyhledávání videí dle názvu
* Stahování a přehrávání videí
* Komentování videí
* Prohlížení profilů uživatelů (tj. nahraných videí a komentářů)

Administrační rozhraní pak používá vestavěnou administrační funkcionalitu frameworku Django a umožňuje libovolnou manipulaci s objekty videí, tagů a komentářů.

### Zpracování nahraných videí

Aby bylo možné videa prezentovat v jednotné formě, přehrávat je na široké škále webových prohlížečů a nemít je založené na licenčně zatížených kodecích, tak jsou všechna nahraná videa nejprve zpracována.

Toto zpracování je prováděno pomocí nástrojů `ffmpeg` a `ffprobe`. Toto zpracování má tři cíle:
* Dekódování informací o nahraném souboru (tj. zda se vůbec jedná o video a jak je dlouhé) - k tomuto účelu je použit nástroj `ffprobe` s JSON výstupem, který je následně přečten aplikací.
* Vygenerování náhledů pro video - k tomuto účelu je použit parametr `-vframes` nástroje `ffmpeg`. Náhledy jsou v současnosti generovány tři, postupně v prvné, druhé a třetí čtvrtině nahraného videa. Aplikace ovšem v současnosti využívá pouze prvního náhledu. Další dva jsou dostupné pro budoucí rozšíření (například pro volbu zobrazovaného náhledu uživatelem).
* Překódování videa do formátu WebM - překódování je opět provedeno nástrojem `ffmpeg`. Parametry kvality byly experimentálně zvoleny tak, aby videa neztrácela příliš na kvalitě a přitom bylo možné je bez obtíží přenášet přes počítačové sítě.

## Postup instalace

Vytvoření databáze a superuživatele proběhne následujícím způsobem:

    $ python manage.py migrate
    $ python manage.py createsuperuser

### Django

Pokud na cílovém stroji není nainstalován framework Django a není možné jej získat běžným zůsobem (tj. balíčkovací systém nebo pip), tak je možné použít následující postup:

    $ wget -O django.tar.gz https://www.djangoproject.com/download/1.8.1/tarball/
    $ tar xzf django.tar.gz
    $ cd Django-*
    $ python setup.py install --user


## Spuštění aplikace

Pro spuštění vestavěného web serveru lze použít příkaz:

    $ python manage.py runserver <ip>:<port>

Pro přístup k aplikaci z libovolného počítače je možné použít IP 0.0.0.0.

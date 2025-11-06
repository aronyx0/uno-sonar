# Logboek Arduino

**2025/sep/12**:
> Idee bedacht voor project: SONAR met interface

**2025/okt/16**:
> Serial reading met Python getest
> * Geeft schijnbaar bytestring, opgelost met `eval()`

**2025/okt/23**:
> Gestart met grafiek van GUI met matplotlib
> * Documentatie gelezen, is een erg ingewikkelde library

**2025/okt/24**:
> Grafiek werkend gekregen, laat nu een statische polar plot zien
> * Internet laat voor alles meerdere opties zien om iets te doen, daarom eerst achterkomen waarom en hoe het werkt

**2025/okt/26**:
> Aan het uitzoeken hoe je de grafiek kan laten veranderen (door `matplitlib.animation.FuncAnimation`)
> Betere manier gemaakt voor serial-data aflezen, met een self-updating class

**2025/okt/31**:
> Begonnen aan `tkinter`-interface, nu tijdelijk nog een lege window

**2025/nov/02**:
> Logboek geüpdate vanaf locaal bestand
> Grafiek laat nu gaten zien door lage updatetijd, dat aan het fixen

**2025/nov/05**:
> Grafiek rendert nu sneller, en met markers i.p.v. een lijn, zodat "stray" punten niet meer zo significant zijn
> Grafiek heeft nu ook kleurenverdeling voor afstand; punten ver weg zijn blauw, en punten dicht bij zijn rood

**2025/nov/06**:
> Grote bug gefixt die ervoor zorgde dat het programma soms niet werkte
> * `eval()` moest toch `.decode()` zijn bij `monitor.readline()`
> Oude frame update-functie verwijderd
> Start gemaakt met `tkinter` in main.py te verwerken
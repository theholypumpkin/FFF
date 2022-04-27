# Digitales Fridays For Future Demoschild
Dieser Python Skript stellt diverse Bilder sowie live gemessende CO2, Temperatur, Luftfeuchtigkeit sowie Optional Stromverbrauch auf zwei 32x32 LED Matrizen dar.
Der Skript wird auf einem RaspberryPi Pico der Adafruit's Circuit Python 6.3 als Python Interpreter nutzt.

## Anleitung zum selbermachen:
### __Wichtige__ Vorrausetztungen und Vorwissen
- Du musst wissen wie man lötet, oder jemanden kennen der Löten kann
- Erfahrung in der Elektronik (keine Sorge wir arbeiten mit Sehr geringen Spannungen (5V) und Strömen (3A))
- Grundlegende Verständnisse in Programmierung (Sprache Python)


### Material
Das notwendige Material kannst du online bestellen, oder im Laden kaufen, leider gibt es in Deutschland nur wenige Verkäfter mit vernünftigen Preisen. Ich versuche immer einen Weblink zuim kaufen bei mindestens einem Deutschen Händer und einen Händler in der EU oder Großbritannien (GB) an.
Lese bevor du etwas käuftst am besten die gesamte Anleitung einmal durch.

__Wichtig für bestellungen auserhalb des Europäischen Binnenmarkt ist Zoll zu zahlen, der wird oft im Preis nicht angegeben__

*Dem Klima zu liebe verucht bei so weingen Händlern wie möglich zu kaufen dann mussen weniger Parkete verschickt werden, die meisten Produkte findest du bei Reichelt und Pimoroni (GB)*

| Produkt | Händler 1 (DE) | Handler 2 (DE) | Händler 3 |
| --- | --- | --- | --- |
| 1x Raspberry Pi Pico | [Reichelt Elektronik, 4,95 € Online](https://www.reichelt.de/raspberry-pi-pico-rp2040-cortex-m0-microusb-rasp-pi-pico-p295706.html?&trstct=pos_0&nbc=1) | [Conrad Electronic, 6,49 €](https://www.conrad.de/de/p/raspberry-pi-mikrocontroller-rp-pico-2348726.html) |  [(GB) Pimoroni, 3,54 €  Online](https://shop.pimoroni.com/products/raspberry-pi-pico) |
| 2x RGB LED Matrizen 32x32 6mm Raster | [Berry Blase; Bereits 32x64 6mm Raster; NUR einmal kaufen 66,90 € Online](https://www.berrybase.de/sensoren-module/led/andere-led-module/64x32-rgb-led-matrix-6mm-raster) | [EXP Tech 32x32 4mm Raster, das heißt deine Bilder sind kleiner. 36,00 € Online](https://www.exp-tech.de/displays/led/5497/rgb-led-panel-32x32?c=1073) | [(GB) Pimoroni 32x32 6mm Raster 17,70 € Online](https://shop.pimoroni.com/products/rgb-led-matrix-panel) |
| 1x Solar-Charger (Optinal) | [Reichelt Elektronik 9,99 ](https://www.reichelt.de/entwicklerboards-solar-ladegeraet-fuer-6-bis-24-v-panels-debo-pwr-solar2-p266038.html) | [Eckstein Komponente 8,87 € Online](https://eckstein-shop.de/WaveshareSolarPowerManagementModule2Cfor6V-24VSolarPanelEN)
| 2x Solarzellen (Optional) | [Reichelt Elektronik 12,90 € Online](https://www.reichelt.de/entwicklerboards-solarpanel-5-w-debo-solar-5w-p266039.html) | [Amazon 14,99 € Online](https://www.amazon.de/Waveshare-Solar-Power-Management-Protection/dp/B07NZNPGZQ) | |
| Alternativ zur Solarzellen und Solarcharger | | | [(GB) Pimoroni 18,43 € Online](https://shop.pimoroni.com/products/powerboost-1000-charger-rechargeable-5v-lipo-usb-boost-1a-1000c)|
| 1x Li-Po Batterie (für etwa 45min bis 1h Akkulaufzeit. LED Matrizen haben einen hohen Stromverbrauch) | | | [(GB) Pimoroni 13,27 € Online](https://shop.pimoroni.com/products/high-capacity-lithium-ion-battery-pack) |
| 1x CO2 Sensor CCS881| [Reichelt Elektronik 18,70 € Online](https://www.reichelt.de/entwicklerboards-sensor-fuer-luftqualitaet-ccs811-debo-sens-ccs811-p253655.html?&trstct=pol_4&nbc=1) | | [(GB) Pimoroni 18,29 € Online](https://shop.pimoroni.com/products/adafruit-ccs811-air-quality-sensor-breakout-voc-and-eco2) |
| 1x Temperatursensor DHT22 | [Reichelt Elektronik 4,65 € Online](https://www.reichelt.de/entwicklerboards-temperatur-feuchtigkeitssensor-dht22-debo-dht-22-p224218.html) | [Conrad Electronics, 6,99 € in Filiale Frankfurt Konstablerwache](https://www.conrad.de/de/p/joy-it-sen-dht22-temperatur-sensor-1-st-passend-fuer-entwicklungskits-arduino-asus-asus-tinker-board-banana-pi-b-2159178.html) | [(GB) Pimoroni 11,21 € Online](https://shop.pimoroni.com/products/cm2302-dht22-temperature-humidity-sensor-module) |
| 2x Stromsensor INA219 (Optional, wenn du Stromverbrauch und Produktion messen willst)) | [Reichelt Elektronik 2,99 € Online](https://www.reichelt.de/entwicklerboards-stromsensor-mit-breakoutboard-ina219-debo-sens-power-p266047.html) | [Eckstein Komponente 4,39 € Online](https://eckstein-shop.de/GY-INA219-Digital-Current-Sensor-Module-I2C-SMBUS-16-programmierbare-Adresse) | [(GB) Pimoroni 8,85 € Online](https://shop.pimoroni.com/products/ina219-high-side-dc-current-sensor-breakout-26v-3-2a-max-stemma-qt) |
| Diverse Header zum anlöten |[Reichelt 2x 1,35 € Online](https://www.reichelt.de/buchsenleiste-20-polig-vergoldet-2-54-bkl-10120828-p235676.html) & [1x 0,21 € Online](https://www.reichelt.de/40pol-stiftleiste-gerade-rm-2-54-sl-1x40g-2-54-p19506.html) & [1x 2,25 € Online](https://www.reichelt.de/stiftleisten-2-54-mm-1x36-gewinkelt-vergoldet-fis-sl3-25-36g-p292528.html) | | [(GB) Pimoroni (Set mit allem Möglichen Sachen) 6,19 € Online](https://shop.pimoroni.com/products/maker-essentials-various-headers)|
| Divere Kabel zum verbinden | [Reichelt Elektronik 4,80 € Online](https://www.reichelt.de/entwicklerboards-steckbrueckenkabel-25cm-20-kabel-einzeln-debo-kabelset4-p238964.html) | | |
| 1x Hohlstecker zum anschrauben/löten | [Reichelt Elektronik 0,19 € Online](https://www.reichelt.de/hohlstecker-knickschutz-aussen-5-5-mm-innen-2-5-mm-hs-25-14-p8648.html) | | |
| 1x LED matrix Feather Wing (Optional aber macht das leben einfacher) | [Berry Blase 7,75 € Online](https://www.berrybase.de/dev.-boards/adafruit-feather/featherwing/adafruit-rgb-matrix-featherwing-kit-f-252-r-feather-m0-und-m4?c=2426) | [Amazon 14,06 € Online](https://www.amazon.de/Adafruit-RGB-Matrix-Featherwing-Kit/dp/B07GYYB795) | [(GB) Pimoroni 7,08 € Online](https://shop.pimoroni.com/products/adafruit-rgb-matrix-featherwing-kit-for-m0-and-m4-feathers)
| Stemma QT Kabel (optinal wenn du weniger löten willst) Nur möglich wenn du auch den CO2 Sensor und die beiden Stromsensoren von Pimoroni kauft| | | [(GB) Pimoroni 1,47 € Online](https://shop.pimoroni.com/products/jst-sh-cable-qwiic-stemma-qt-compatible?variant=31910609846355) & 2x dieses Kalbel (nur wenn du Stromsensoren hast)[(GB) Pimoroni 1,47 € Online](https://shop.pimoroni.com/products/jst-sh-cable-qwiic-stemma-qt-compatible?variant=31910609813587)|
| 2x Alte USB Handy-Ladekabel, eins davon wird zerschnitten| | | |
| Wekzeuge wie Schraubenzieher Schraubenschüssen, Sägen, Akkubohrer, Sandpapier, etc. | | | |
| Steckplatine (optional, macht aner das löten um einiges einfacher)| | | |
| Holzschrauben 1,6 cm lang | | | |
| 2 bis 3 Holzschrauben 3 cm lang | | | |
| Schrauben mit Muttern 5 mm um die Solarpanele zu befestigen | | | |
| Modellbauholz 25x50 cm | | | |
| Holzbalken 2x4 cm breit und 2 m lang | | | |
| Rechteckleiste 5x20 mm ~1m lang | | | |

So jetzt wo alles hast können wir anfangen.

## Schritt 1 Löten
Wir fangen mit dem Löten der einzelen Komponenten an:
__Warung Lötkolben werden sehr heiß 200 °C oder mehr, pass auf das du dich nicht verbrennst__
#### 1.
* Wenn deine Stromsensoren (INA219) und CO2 sensor (CCS881) von Adafruit oder Sparkfun produziert worden sind, und ddu das Optionale Stemma QT/Qwiic Kabel gekauft hast dann kannst du dir etwas löten ersparen, und einfach nur 3 Sensoren in eine Reihe Stecken, Diese Sensoren haben auf den beiden kuzen Seite einen Steckverbinder wo man ein Solches Kabel einstecken kann. Wenn du von Anderen Herstellen gekauft hast, dann musst du die (meistens Beigelegte) Stiftleiste anlöten. [Hier gibt es eine Anleitung mit Bildern, wie du das bei dem CO2 Sensor macht, das selbe gilt auch für den Stromsensor](https://learn.adafruit.com/adafruit-ccs811-air-quality-sensor/assembly).
#### 2.
* Je nachdem wo du deinen Temperatur und Luftfeuchtigkeitssensor gekauft hast, musst du löten oder auch nicht. Ich empfehle den von Pimoroni, denn hier musst du nicht löten, braucht keine Platine zum anlöten oder Wiederstände, der Kommt komplett vorbereitet, du muss dann nur die Kabel anschließen.[Wenn du einen der anderen hast, dann kannst du hier naschauen wie du ihn anschließt](https://learn.adafruit.com/dht/connecting-to-a-dhtxx-sensor). Achte auf den Wiederstand von _20-50 Kilo Ohm_.
Damit sind alle Snesoren vorbereitet.
#### 3.
* Nun müssen wir die Buchsenleistenleisten an den Raspberry Pi Pico anlöten. Eine Buchenleiste sieht wie im Bild hier aus: ![Bild 1 Buchsenleiste](https://cdn-reichelt.de/bilder/web/xxl_ws/C140/BKL_10120984.png "Das ist eine Buchenleiste")
* Der Raspbbery Pi Pico hat 40 Sogenannte Pins oben. Davon habe 28 spezielle Funktionen. Interessiert uns aber alles nicht. Um uns das leben einfacher zu machen, schuern wir uns das Pinout Diagram an was der Hersteller bereit stellt. ![Bild 2 Raspberry Pi Pico Pinout](https://www.raspberrypi.org/documentation/rp2040/getting-started/static/64b50c4316a7aefef66290dcdecda8be/Pico-R3-SDK11-Pinout.svg "Pinout Diagram"). Hier ist sehr viel zu sehen, aber vieles ist für dich egal, wenn du den Quellcode nicht verändern willst.
* Wir Orientiern nun unseren Raspberry Pi Pico genauso wie im bild, das Logo mit der Himbeere kommt nach unten und die USB Buchse kommt nach oben.
* Nun suchen wir aus unsern Set an Buchenleisten So viele raus, das wir insgesammt 14 Buchen haben. Wenn du das Set von Pimoroni gekauft hast, dann musst du die Kurzen Enden der buchen mit Sandpapier etwas abreiben, damit sie nebeneinander passen. Wenn du von Reichelt gekauft hast, kannst du dir einfach 14 von den 20 Buchen abschneiden. Du braucht 2 mal Leisten der Länge 14 und nicht mehr.
`//TODO insert Picture`
* * Diese Leisten löten wir jetzt auf beide Seiten an, so das sie nach oben Zeigen. Das heißt wir wollen die Leisten und die Himbeere zugleich sehen können. Wir löten sie aber nicht irgendwo an, Die Leisten werden von Pin 7 (GP5) bis Pin 20 (GP15) angelötet, die obenren 6 Pins neben der USB-Buche bleiben frei. Um zu wissen wo diese Pins sind, könne wir uns wieder das Pinout Diagram anschauen. Jeder der Pins zwischen Pin 7 und 20 muss angelötet werden.
* * auf der anderen Seite machen wir das selbe. Wir lassen wieder die Oben 6 Pins frei, und löten die Buchenleiste an alle Pins zwischen Pin 21 (GP16) und Pin 34 (GP28) an. Das hat dann folgend auszusehen. *Ich habe bei mir noch Pin 30 (Run) frei gelassen, das müsst ihr aber nicht machen*
`//TODO insert Picture`
* Nun kommen wir zu den 6 Freigelassen Pins auf beiden Seiten. diese füllen wir mit den Gewinkelten Stiftleisten auf. Also die die um die Ecke gehen. [](https://cdn-reichelt.de/bilder/web/xxl_ws/C140/SL3.png "Gewinkelte Stiftleiste") du kannst einfach 6 abscheiden von denen die du gekauft hast.
Damit ist der Raspberry Pi Pico fertig gelötet, lege ihn ersteinmal beiseite, ihn brauchen wir erst einmal nicht.
#### 4.
* Nun Kommen wir zum Löten, des "Featherwings", der ist realtiv komplizert zu löten, wenn du Probleme damit hast, dann frage einen Verwanten oder einen Freund. Im Set ist sehr viel Zeug, wir brauchen, da haben den Hohlsteckerbuchse (im Bild 5 Blau), den IDC Buchse auch Schneidklemme genannt (im Bild 5 Rot), eine Schraubklemme (im Bild 5 Grün), und ein paar Stiftleisten (im Bild 5 Gelb). ![Bild 1 Featherwing](https://github.com/theholypumpkin/FFF/blob/main/Pictures/Components.jpg "Bild 5 Komponenten") ![Bild 6 Featherwing](https://github.com/theholypumpkin/FFF/blob/main/Pictures/Where%20to%20Solder.jpg "Bild 2 Wo hin löten")
* Wir fangen mit der IDC Buchse/Schneidklemme Bild 5 (Rot) an. Die ist ja im Bild 6 (Rot) makiert und hat auf einer Seite eine Kerbe. __Die Kerbe ich ganz wichtig!__ Die IDC Buchse/Schneidklemme gehört auf dem Featherwing in die Mitte (auch Rot markiert). __Achte auf die Kerbe, die auch auf dem Featherwing Markiert ist. Die Kerbe auf der IDC Buchse muss auf der Selben Seite sein, wie die des Featherwing__
* Jetzt kommen wir erst einmal zum Schwersten Teil, die Stiftleisten.
* * an alle im Bild 6 (__GELB__) Markierten Flächen, und auch __nur__ an diesen positionen Brauchen gerade Stiftleisten nach Unten. Wenn du dir nicht sicher bist, was die Geraden Stiftleisten sind, hier ist noch einmal ein Bild ![Bild 7 Gerade Stiftleiste](https://cdn-reichelt.de/bilder/web/xxl_ws/C140/SL_1X40G_2-54.png "Gerade Stiftleiste"). Mit Stiftleisten nach unten ist gemeint, dass wenn wir den "Featherwing" genauso wie in Bild 5 vor uns haben, dann können wir die Stifte nicht sehen. __Aufpassen, die Stifte sind versetzt. Einmal sind sie auf der äußerne Reihe und einmal auf der mittleren Reihe__
* * An den Magenta/Lila sind Auch Stifte anzubringen, aber diese mal Müssen sie nach __Oben__ Zeigen! Das heißt wenn wir wollen die Stift sehen, wenn wir den "Featherwing" genauso wie im Bild 6 Betrachten.
* * Nun kommen noch an die Orange makierten Stellen gewinkelte Stifte wie im letzten Unterpunkt von Punkt 3.
* Als nächstes installieren wir die Schraubklemme Bild 5 (Grün) auf der Rechten Seite Bild 6 (Grün). Stelle sicher, das die Schrauböffnung nach Außen zeigt.
* Nun installieren wir die Hohlsteckerbuchse Bild 5 (Dunkelblau) an die Stelle in Bild 6 (Hellblau), hier kannst du eigentlich nichts flasch machen es geht nur in ein einzige weise anzulöten.
Nun haben wir alles angelötet fast ferig mit dem allem was Gelötet werden muss aber das Kommt später noch einmal.
## Schritt 2 Vorbereiten und Programmieren den Reaspberry Pi Pico
#### 1.
* Wir gehen in Internet und [laden uns Circuit-Python 6.3.0 herunter](https://circuitpython.org/board/raspberry_pi_pico/). Wen zu deinem Zeitpunkt bereits eine neuere Version verfügbar ist, dann musst du trotzdem die Version 6.3.0 installieren, die "alte" Verion die du brauchts findest du [hier](https://adafruit-circuit-python.s3.amazonaws.com/bin/raspberry_pi_pico/de_DE/adafruit-circuitpython-raspberry_pi_pico-de_DE-6.3.0.uf2 "Direct Download") Nun müssen wir die Datei auf den Rasperry Pi Pico kopieren. Dafür musst du den Knop der auf dem Pico ist gedrückt halten, und dann ihn mit dem Handy-Lade-Kabel an dne Computer anschließen. In deinem Datei-Explorer auf dein Computer Müsste nun eine "USB-Stick" names __`RPI-RP2`__ auftauchen. Nun ziehst du einfach die Datei die du heruntergelanden hast, in diesen Ordner. Der __`RPI-RP2` "USB-Stick" sollte verschwinden__, und kurz darauf ein neuer "USB-Stick" names __`CIRCUITPY`__ auftauchen. Das wars. Lasse den Raspberry Pi Pico eingesteckt in deinem Computer. *Falls du probleme hattest, hier ist noch einmal eine [Anleitung online](https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/circuitpython)*
#### 2.
* Nun gehst du auf dieser Website wo du gerade das ließt, ganz nach oben, und dort ist ein Grüner Knopf, der sagt __Code__ wenn du darauf klickst, dann bekommst du ein kleines Fester. Hier gibt es einen weitern Knopf Names __Download Zip__ diesen klickst du an und der Quellcode für das Demoschild wird Heruntergeladen. Wenn du zu faul bist, bis nach ganz oben zu zu Scrollen [hier kannst du den Code auch herunterladen](https://github.com/theholypumpkin/FFF/archive/refs/heads/main.zip)
#### 3.
* die Heruntergeladen Datei musst du nun entpacken mit einem Program wie WinRar oder 7zip, ich gehe aber davon aus das du so etwas bereits installiert hast.
#### 4.
* Im entpackten Ordner gibt es 3 sachen die du auf den __`CIRCUITPY`__ "USB-Stick" kopieren musst.
* * Du musst den Ordner names `lib` auf den __`CIRCUITPY`__ "USB-Stick" kopieren
* * Du musst die Dateien `bitmap.bmp` und `code.py` "USB-Stick" kopieren. *Gegebennefalls heißen die dateien auch nur `bitmap` `code`*
Jetzt hast du schon alles Programmiert was du machen musst, wenn wir nachher dann alles verkabeln, dann sollte deine LED Matrizen die Diashow anzeigen.
## Schritt 3 Alles verkabeln und noch etwas mehr löten
* placholder

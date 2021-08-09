# Digitales Fridays For Future Demoschild
Dieser Python Skript stellt diverse Bilder sowie live gemessende CO2, Temperatur, Luftfeuchtigkeit, Stromverbrauch und Stromprodiktion auf zwei 32x32 LED Matrizen dar.
Der Skript wird auf einem RaspberryPi Pico der Adafruit's Circuit Python 6.3 als Python Interpreter nutzt.

## Anleitung zum selbermachen:
### __Wichtige__ Vorrausetztungen und Vorwissen
- Du musst wissen wie man lötet, oder jemanden kennen der Löten kann
- Erfahrung in der Elektronik (keine Sorge wir arbeiten mit Sehr geringen Spannungen (5V) und Strömen (1A))
- Grundlegende Verständnisse in Programmierung (Sprache Python)


### Material
Das notwendige Material kannst du online bestellen, oder im Laden kaufen, leider gibt es in Deutschland nur wenige Verkäfter mit vernünftigen Preisen. Ich versuche immer einen Weblink zuim kaufen bei mindestens einem Deutschen Händer und einen Händler in der EU oder Großbritannien (GB) an.
Trotzdem all so etwas ist ein Teueres Hobby und ich habe viele teile verwendet, die ich eh schon hatte. 
Rechne aber am besten damit __Mindesten 100 €__ dafür auszugeben. Lese bevor du etwas käuftst am besten die gesamte anleitung einmal durch.

__Wichtig für bestellungen auserhalb des Europäischen Binnenmarkt ist Zoll zu zahlen, der wird oft im Preis nicht angegeben__

*Dem Klima zu liebe verucht bei so weingen Händlern wie möglich zu kaufen dann mussen weniger Parkete verschickt werden, die meisten Produkte findest du bei Reichelt und Pimoroni (GB)*

| Produkt | Händler 1 (DE) | Handler 2 (DE) | Händler 3 |
| --- | --- | --- | --- |
| 1x Raspberry Pi Pico | [Reichelt Elektronik, 4,95 € Online](https://www.reichelt.de/raspberry-pi-pico-rp2040-cortex-m0-microusb-rasp-pi-pico-p295706.html?&trstct=pos_0&nbc=1) | [Conrad Electronic, 6,49 € in Filiale Frankfurt Konstablerwache](https://www.conrad.de/de/p/raspberry-pi-mikrocontroller-rp-pico-2348726.html) |  [(GB) Pimoroni, 3,54 €  Online](https://shop.pimoroni.com/products/raspberry-pi-pico) |
| 2x RGB LED Matrizen 32x32 6mm Raster | [Berry Blase; Bereits 32x64 6mm Raster; NUR einmal kaufen 66,90 € Online](https://www.berrybase.de/sensoren-module/led/andere-led-module/64x32-rgb-led-matrix-6mm-raster) | [EXP Tech 32x32 NUR 4mm Raster 36,00 € Online](https://www.exp-tech.de/displays/led/5497/rgb-led-panel-32x32?c=1073) | [(GB) Pimoroni 32x32 6mm Raster 17,70 € Online](https://shop.pimoroni.com/products/rgb-led-matrix-panel) |
| 1x Solar-Charger | [Reichelt Elektronik 9,99 € Online](https://www.reichelt.de/entwicklerboards-solar-ladegeraet-fuer-6-bis-24-v-panels-debo-pwr-solar2-p266038.html) | [Eckstein Komponente 8,87 € Online](https://eckstein-shop.de/WaveshareSolarPowerManagementModule2Cfor6V-24VSolarPanelEN)
| 2x Solarzellen | [Reichelt Elektronik 12,90 € Online](https://www.reichelt.de/entwicklerboards-solarpanel-5-w-debo-solar-5w-p266039.html) | [Amazon 14,99 € Online](https://www.amazon.de/Waveshare-Solar-Power-Management-Protection/dp/B07NZNPGZQ) | |
| 1x Li-Po Batterie | | | [(GB) Pimoroni 13,27 € Online](https://shop.pimoroni.com/products/high-capacity-lithium-ion-battery-pack) |
| 1x CO2 Sensor CCS881| [Reichelt Elektronik 18,70 € Online](https://www.reichelt.de/entwicklerboards-sensor-fuer-luftqualitaet-ccs811-debo-sens-ccs811-p253655.html?&trstct=pol_4&nbc=1) | | [Pimoroni 18,29 € Online](https://shop.pimoroni.com/products/adafruit-ccs811-air-quality-sensor-breakout-voc-and-eco2) |
| 1x Temperatursensor DHT22 | [Reichelt Elektronik 4,65 € Online](https://www.reichelt.de/entwicklerboards-temperatur-feuchtigkeitssensor-dht22-debo-dht-22-p224218.html) | [Conrad Electronics, 6,99 € in Filiale Frankfurt Konstablerwache](https://www.conrad.de/de/p/joy-it-sen-dht22-temperatur-sensor-1-st-passend-fuer-entwicklungskits-arduino-asus-asus-tinker-board-banana-pi-b-2159178.html) | [(GB) Pimoroni 11,21 € Online](https://shop.pimoroni.com/products/cm2302-dht22-temperature-humidity-sensor-module) |
| 2x Stromsensor INA219 | [Reichelt Elektronik 2,99 € Online](https://www.reichelt.de/entwicklerboards-stromsensor-mit-breakoutboard-ina219-debo-sens-power-p266047.html) | [Eckstein Komponente 4,39 € Online](https://eckstein-shop.de/GY-INA219-Digital-Current-Sensor-Module-I2C-SMBUS-16-programmierbare-Adresse) | [(GB) Pimoroni 8,85 € Online](https://shop.pimoroni.com/products/ina219-high-side-dc-current-sensor-breakout-26v-3-2a-max-stemma-qt) |
| Diverse Header zum anlöten |[Reichelt 2x 1,35 € Online](https://www.reichelt.de/buchsenleiste-20-polig-vergoldet-2-54-bkl-10120828-p235676.html) & [1x 0,21 € Online](https://www.reichelt.de/40pol-stiftleiste-gerade-rm-2-54-sl-1x40g-2-54-p19506.html) | | [(GB) Pimoroni (Set mit allem Möglichen Sachen) 6,19 € Online](https://shop.pimoroni.com/products/maker-essentials-various-headers)|
| Divere Kabel zum verbinden | [Reichelt Elektronik 4,80 € Online](https://www.reichelt.de/entwicklerboards-steckbrueckenkabel-25cm-20-kabel-einzeln-debo-kabelset4-p238964.html) | | |
| 1x Hohlstecker zum anschrauben/löten | [Reichelt Elektronik 0,19 € Online](https://www.reichelt.de/hohlstecker-knickschutz-aussen-5-5-mm-innen-2-5-mm-hs-25-14-p8648.html) | | |
| 1x LED matrix Feather Wing (Optional aber macht das leben einfacher) | [Berry Blase 7,75 € Online](https://www.berrybase.de/dev.-boards/adafruit-feather/featherwing/adafruit-rgb-matrix-featherwing-kit-f-252-r-feather-m0-und-m4?c=2426) | [Amazon 14,06 € Online](https://www.amazon.de/Adafruit-RGB-Matrix-Featherwing-Kit/dp/B07GYYB795) | [(GB) Pimoroni 7,08 € Online](https://shop.pimoroni.com/products/adafruit-rgb-matrix-featherwing-kit-for-m0-and-m4-feathers)
|3x Stemma QT Kabel (optinal)| | | |
| Alte USB Handy-Ladekabel als Kabelspender| | | |
| Wekzeuge wie Schraubenzieher Schraubenschüssen, Sägen, Akkubohrer, etc. | | | |
| Steckplatine | | | |

So jetzt wo alles hast können wir anfangen.

## Schritt 1 Löten:
Wir fangen mit dem Löten der einzelen Komponenten an:
__Warung Lötkolben werdne sehr heiß 200 oder mehr, pass auf das du dich nicht verbrennst__
- Wenn deine Stromsensoren (INA219) und CO2 sensor (CCS881) von Adafruit oder Sparkfun produziert worden sind, und ddu das Optionale Stemma QT/Qwiic Kabel gekauft hast dann kannst du dir etwas löten ersparen, und einfach nur 3 Sensoren in eine Reihe Stecken, Diese Sensoren haben auf den beiden kuzen Seite einen Steckverbinder wo man ein Solches Kabel einstecken kann. Wenn du von Anderen Herstellen gekauft hast, dann musst du die (meistens Beigelegte) Stiftleiste anlöten. [Hier gibt es eine Anleitung mit Bildern, wie du das bei dem CO2 Sensor macht, das selbe gilt auch für den Stromsensor](https://learn.adafruit.com/adafruit-ccs811-air-quality-sensor/assembly)
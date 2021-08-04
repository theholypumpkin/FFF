# Digitales Fridays For Future Demoschild
Dieser Python Skript stellt diverse Bilder sowie live gemessende CO2, Temperatur, Luftfeuchtigkeit, Stromverbrauch und Stromprodiktion auf zwei 32x32 LED Matrizen dar.
Der Skript wird auf einem RaspberryPi Pico der Adafruit's Circuit Python 6.3 als Python Interpreter nutzt.

## Anleitung zum selbermachen:
### __Wichtige__ Vorrausetztungen
- Du musst wissne wie man lötet, oder jemanden kennen der Löten kann

### Material
Das notwendige Material kannst du online bestellen, oder im Laden kaufen, leider gibt es in Deutschland nur wenige Verkäfter mit vernünftigen Preisen. Ich versuche immer einen Weblink zuim kaufen bei mindestens einem Deutschen Händer und einen Händler in der EU oder Großbritannien (GB) an.
Trotzdem all so etwas ist ein Teueres Hobby und ich habe viele teile verwendet, die ich eh schon hatte. Rechne am besten damit __Mindesten 100 €__ dafür auszugeben.
`Wichtig für bestellungen auserhalb des Europäischen Binnenmarkt ist Zoll zu zahlen, der wird oft im Preis nicht angegeben`
*Dem Klima zu liebe verucht bei so weingen Händlern wie möglich zu kaufen dann mussen weniger Parkete verschickt werden, die meisten Produkte findest du bei Reichelt und Pimoroni (GB)*

| Produkt | Händler 1 (DE) | Handler 2 (DE) | Händler 3 |
| --- | --- | --- | --- |
| 1x Raspberry Pi Pico | [Conrad Electronic, 6,49 € in Filiale Frankfurt Konstablerwache](https://www.conrad.de/de/p/raspberry-pi-mikrocontroller-rp-pico-2348726.html) | [Reichelt Elektronik, 4,95 € Online](https://www.reichelt.de/raspberry-pi-pico-rp2040-cortex-m0-microusb-rasp-pi-pico-p295706.html?&trstct=pos_0&nbc=1) | [(GB) Pimoroni, 3,54 €  Online](https://shop.pimoroni.com/products/raspberry-pi-pico) |
| 2x RGB LED Matrizen 32x32 6mm Raster | [Berry Blase; Bereits 32x64 6mm Raster; NUR einmal kaufen 66,90 € Online](https://www.berrybase.de/sensoren-module/led/andere-led-module/64x32-rgb-led-matrix-6mm-raster) | [EXP Tech 32x32 NUR 4mm Raster 36,00 € Online](https://www.exp-tech.de/displays/led/5497/rgb-led-panel-32x32?c=1073) | [(GB) Pimoroni 32x32 6mm Raster 17,70 € Online](https://shop.pimoroni.com/products/rgb-led-matrix-panel) |
| 1x LED matrix Feather Wing (Optional aber macht das leben einfacher) | [Berry Blase 7,75 € Online](https://www.berrybase.de/dev.-boards/adafruit-feather/featherwing/adafruit-rgb-matrix-featherwing-kit-f-252-r-feather-m0-und-m4?c=2426) | [Amazon 14,06 € Online](https://www.amazon.de/Adafruit-RGB-Matrix-Featherwing-Kit/dp/B07GYYB795) | [(GB) Pimoroni 7,08 € Online](https://shop.pimoroni.com/products/adafruit-rgb-matrix-featherwing-kit-for-m0-and-m4-feathers)
| 1x Solar-Charger | [Reichelt Elektronik 9,99 € Online](https://www.reichelt.de/entwicklerboards-solar-ladegeraet-fuer-6-bis-24-v-panels-debo-pwr-solar2-p266038.html) |
| 2x Solarzellen | [Reichelt Elektronik 12,90 € Online](https://www.reichelt.de/entwicklerboards-solarpanel-5-w-debo-solar-5w-p266039.html) | [Amazon 14,99 € Online](https://www.amazon.de/Waveshare-Solar-Power-Management-Protection/dp/B07NZNPGZQ) | --- |
| 1x Li-Po Batterie | --- | --- | [(GB) Pimoroni 13,27 € Online](https://shop.pimoroni.com/products/high-capacity-lithium-ion-battery-pack) |
| 1x CO2 Sensor CCS881| [Reichelt Elektronik 18,70 € Online](https://www.reichelt.de/entwicklerboards-sensor-fuer-luftqualitaet-ccs811-debo-sens-ccs811-p253655.html?&trstct=pol_4&nbc=1) | --- | [Pimoroni 18,29 € Online](https://shop.pimoroni.com/products/adafruit-ccs811-air-quality-sensor-breakout-voc-and-eco2) |
| 1x Temperatursensor DHT22 | [Reichelt Elektronik 4,65 € Online](https://www.reichelt.de/entwicklerboards-temperatur-feuchtigkeitssensor-dht22-debo-dht-22-p224218.html) | [Conrad Electronics, 6,99 € in Filiale Frankfurt Konstablerwache](https://www.conrad.de/de/p/joy-it-sen-dht22-temperatur-sensor-1-st-passend-fuer-entwicklungskits-arduino-asus-asus-tinker-board-banana-pi-b-2159178.html) | [(GB) Pimoroni 11,21 € Online](https://shop.pimoroni.com/products/cm2302-dht22-temperature-humidity-sensor-module) |
| 2x Stromsensor INA219 | [Reichelt Elektronik 2,99 € Online](https://www.reichelt.de/entwicklerboards-stromsensor-mit-breakoutboard-ina219-debo-sens-power-p266047.html) | [Eckstein Komponente 4,39 € Online](https://eckstein-shop.de/GY-INA219-Digital-Current-Sensor-Module-I2C-SMBUS-16-programmierbare-Adresse) | [(GB) Pimoroni 8,85 € Online](https://shop.pimoroni.com/products/ina219-high-side-dc-current-sensor-breakout-26v-3-2a-max-stemma-qt) |
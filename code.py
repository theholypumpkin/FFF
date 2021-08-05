import board

from math import floor

from switch import Switch  # one switch case implermetation

import time  # to make the controller sleep
import busio  # i2c spi uart etc.

import displayio  # lib to disoplay more complex things on the martrix
import rgbmatrix  # lib for the matrix
import terminalio
import framebufferio
from adafruit_display_text.label import Label
import adafruit_ccs811
import adafruit_dht
import adafruit_ina219  # Ampere / Volt Sensor
# -----------------------------------------------------------------------------
# Setting up Sensors
i2c = busio.I2C(board.GP1, board.GP0)
ccs = adafruit_ccs811.CCS811(i2c)
dht = adafruit_dht.DHT22(board.GP5)
ina_battery = adafruit_ina219.INA219(i2c)
ina_solar = adafruit_ina219.INA219(i2c, 0x41)

switch = Switch()

# Global Variables
image_cycle = 0
i = 0  # TODO set value to 0
solar_power = []
power_usage = []
co2_concentration = []
temperature = []
humidity = []
# -----------------------------------------------------------------------------
# RGB Pins: [GP20 = R1, GP19 = G1, GP21 = B1, GP22 = R2, GP27 = G2, GP28 = B2]
# ADDR Pins: [GP9 = A, GP8 = B, GP7 = C, GP6 = D]
# GP26 = CLK
# GP13 = Latch
# GP12 = OE (output enable)
# -----------------------------------------------------------------------------
# Matrix Setup
displayio.release_displays()

matrix = rgbmatrix.RGBMatrix(  # Gives me 2^4 = 16 Brightness levels to save
                               # power we make it dimer
    width=64,
    height=32,
    bit_depth=6,
    rgb_pins=[board.GP20, board.GP19, board.GP21,
              board.GP22, board.GP27, board.GP28],
    addr_pins=[board.GP9, board.GP8, board.GP7, board.GP6],
    clock_pin=board.GP26, latch_pin=board.GP13, output_enable_pin=board.GP12,
    doublebuffer=True)

display = framebufferio.FramebufferDisplay(matrix, auto_refresh=True)
# -----------------------------------------------------------------------------
# Create 3 Text Columns
line1 = Label(terminalio.FONT,
              color=0x000000,
              text="")
line1.x = 63
line1.y = 31

line2 = Label(terminalio.FONT,
              color=0x000000,
              text="")
line2.x = 63
line2.y = 31

line3 = Label(terminalio.FONT,
              color=0x000000,
              text="")
line3.x = 63
line3.y = 31
# -----------------------------------------------------------------------------
# Loading Bitmaps to display imanges
bitmap_file = open("bitmap.bmp", "rb")
bitmap_bmp = displayio.OnDiskBitmap(bitmap_file)

bitmap_tiles = displayio.TileGrid(bitmap_bmp,
                                  pixel_shader=getattr(bitmap_bmp,
                                                       'pixel_shader',
                                                       displayio.
                                                       ColorConverter()),
                                  width=1, height=1, tile_height=32,
                                  tile_width=64, default_tile=0, x=0, y=0)

bitmap_group = displayio.Group()
bitmap_group.append(bitmap_tiles)
bitmap_group.append(line1)
bitmap_group.append(line2)
bitmap_group.append(line3)
display.show(bitmap_group)
# -----------------------------------------------------------------------------
# Scroll a line in a defined direction or multiple directions
def scroll(line, x, y=0, iterations=1):
    for i in range(iterations):

        line.x = floor(line.x + x)
        line.y = floor(line.y + y)
        line_width = line.bounding_box[2]
        line_height = line.bounding_box[3]

        if line.x < -line_width:
            line.x = display.width

        elif line.x >= display.width:
            line.x = -line_width

        if line.y < -line_height:
            line.y = display.height

        elif line.y >= display.height:
            line.y = -line_height

        time.sleep(0.06250)  # Wait before restarting the loop
# -----------------------------------------------------------------------------
def read_sensors():
    # TODO Try-Catch-block!
    power_usage.append(ina_battery.power)  # Read the power usage every tile
    solar_power.append(ina_solar.power)  # Read power production on every til
    try:
        co2_concentration.append(ccs.eco2)
    except RuntimeError as e:
        print("Execption: ", e.args)
        co2_concentration.append(450)
    else:
        print("co2 concentration appended to list")
    try:
        temperature.append(dht.temperature)
        humidity.append(dht.humidity)
    except RuntimeError as e:
        print("Execption: ", e.args)  # When the checksum did not validated
        temperature.append(25)
        humidity.append(50)
    else:
        print("temperature and humidity appended to list")
# -----------------------------------------------------------------------------
# Set text, when tile zero and one are displayed
def tile_line_values(line, text="", color=0x000000,
                     background_color=None, x=63, y=31):
    line.text = text
    line.color = color
    line.background_color = background_color
    line.x = x
    line.y = y
# -----------------------------------------------------------------------------
# the 1.3 Degrees Earth Tiles
def tile_0():
    read_sensors()
    tile_line_values(line2)  # Reset lines
    tile_line_values(line3)
    tile_line_values(line1, "how much?", 0x0000ff, x=64, y=8)
    scroll(line1, x=-1, iterations=119)
# -----------------------------------------------------------------------------
# the 1.5 Degrees Earth Tiles
def tile_1():
    read_sensors()
    tile_line_values(line1, "Stop!", 0xff0000, x=64, y=8)
    scroll(line1, x=-1, iterations=95)
# -----------------------------------------------------------------------------
# The two degrees Earth tile
def tile_2():
    read_sensors()
    tile_line_values(line1, " TO HOT!", 0xffffff, 0xff0000, x=64, y=7)
    scroll(line1, x=-1, iterations=112)
# -----------------------------------------------------------------------------
# The 4 Degree Earth tile
def tile_3():
    read_sensors()
    tile_line_values(line1, "End of Socity!",
                     0xff0000, x=64, y=8)
    scroll(line1, x=-1, iterations=145)
# -----------------------------------------------------------------------------
# All tile which don't have text
def tile_4_9_A_B_10_11():
    read_sensors()
# -----------------------------------------------------------------------------
# The tile Show your Stripes
def tile_5():
    read_sensors()
    tile_line_values(line1)  # Reset line1
    tile_line_values(line2, "#ShowYourStripes", 0xff0000, x=63, y=24)
    scroll(line2, x=-1, iterations=158)
# -----------------------------------------------------------------------------
# The tile displaying the Sun and Battery
def tile_6():
    # We display the mean (avarage) of all power_usage readings of last 2 min
    read_sensors()
    print(solar_power)
    print(power_usage)
    tile_line_values(line1, "{:.2} W".format(sum(solar_power)/len(solar_power)),
                     0xffffff, 0x000000, x=20, y=8)
    tile_line_values(line2, "{:.2} W".format(sum(power_usage)/len(power_usage)),
                     0xffffff, 0x000000, x=20, y=24)
    solar_power.clear()  # Remove all values from array so we can fill it again
    power_usage.clear()
# -----------------------------------------------------------------------------
# The tile displaying the Green Gost
def tile_7():
    read_sensors()
    tile_line_values(line1, "Buhh!", 0x16ca31, x=32, y=6)
    tile_line_values(line2, "Bring", 0x16ca31, x=32, y=16)
    tile_line_values(line3, "Oko!", 0x16ca31, x=32, y=26)
# -----------------------------------------------------------------------------
# The tile displaying the Smokestacks and CO2
def tile_8():
    read_sensors()
    print(co2_concentration)
    tile_line_values(line2)  # Reset Lines
    tile_line_values(line3)
    # We display the avarage CO2 concentration of the last two minutes
    tile_line_values(line1,
                     f'CO2 {int(sum(co2_concentration)/len(co2_concentration))}',
                     0xff0000, x=16, y=8)
    tile_line_values(line2, "PPM", 0xff0000, x=40, y=20)
    co2_concentration.clear()
# -----------------------------------------------------------------------------
# The tile displaying the Explosion
def tile_C():
    read_sensors()
    tile_line_values(line1, "NOW!", 0xff0000, x=20, y=14)
# -----------------------------------------------------------------------------
# The CDU Tiles
def tile_D_E_F():
    read_sensors()
    tile_line_values(line1, "Gibt", 0xffffff, x=4, y=4)
    tile_line_values(line2, "mir", 0xffffff, x=4, y=16)
    tile_line_values(line3, "ein", 0xffffff, x=4, y=27)
# -----------------------------------------------------------------------------
# The Temperature, humidity tiles
def tile_12():
    read_sensors()
    print(temperature)
    print(humidity)
    # Print the temperature with on foating point number
    tile_line_values(line1, "{:.2}".format(sum(temperature)/len(temperature)),
                     0xffff00, x=12, y=6)

    tile_line_values(line2, f'{int(sum(humidity)/len(humidity))}%',
                     0x0000ff, x=32, y=24)
    temperature.clear()
    humidity.clear()
# -----------------------------------------------------------------------------
# The black empty tile with github link
def tile_13():
    tile_line_values(line1, "Smash Ca(r)pitalism", 0x0000ff, x=64, y=8)
    scroll(line1, x=-1, iterations=179)
# -----------------------------------------------------------------------------
# Add an case for each tile
case_tile_0 = tile_0
case_tile_1 = tile_1
case_tile_2 = tile_2
case_tile_3 = tile_3
case_tile_4_9_A_B_10_11 = tile_4_9_A_B_10_11
case_tile_5 = tile_5
case_tile_6 = tile_6
case_tile_7 = tile_7
case_tile_8 = tile_8
case_tile_C = tile_C
case_tile_D_E_F = tile_D_E_F
case_tile_12 = tile_12
case_tile_13 = tile_13

# adding cases to switch
switch.add_case(0, case_tile_0, True)
switch.add_case(1, case_tile_1, True)
switch.add_case(2, case_tile_2, True)
switch.add_case(3, case_tile_3, True)
switch.add_case(4, case_tile_4_9_A_B_10_11, True)
switch.add_case(5, case_tile_5, True)
switch.add_case(6, case_tile_6, True)
switch.add_case(7, case_tile_7, True)
switch.add_case(8, case_tile_8, True)
switch.add_case(9, case_tile_4_9_A_B_10_11, True)
switch.add_case(10, case_tile_4_9_A_B_10_11, True)
switch.add_case(11, case_tile_4_9_A_B_10_11, True)
switch.add_case(12, case_tile_C, True)
switch.add_case(13, case_tile_D_E_F, True)
switch.add_case(14, case_tile_D_E_F, True)
switch.add_case(15, case_tile_D_E_F, True)
switch.add_case(16, case_tile_4_9_A_B_10_11, True)
switch.add_case(17, case_tile_4_9_A_B_10_11, True)
switch.add_case(18, case_tile_12, True)
switch.add_case(19, case_tile_13, True)

# -----------------------------------------------------------------------------
# Wait for the sensor to be ready
while not ccs.data_ready:
    pass
# The main program loop
while True:
    if (image_cycle + 0.1) < time.monotonic():
        bitmap_tiles[0] = i
        sub = time.monotonic()  # get the time before the execution of switch
        switch.case(i)
        # substract the execution time of switch from the sleep time
        dif = time.monotonic() - sub
        print(f'dif before: {dif}')
        if dif > 5:  # When a tile takes longer than 5 sec to process
            dif = 0
        else:
            dif = 5 - dif  # when tile takes less than 5 sec to process
        print(f'difafter:{dif}')
        image_cycle = time.monotonic()
        if (i > 19):
            i = 0
    time.sleep(dif)
    tile_line_values(line1)  # Reset the line Label
    tile_line_values(line2)
    tile_line_values(line3)
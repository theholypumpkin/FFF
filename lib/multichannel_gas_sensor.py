"""
The MIT License (MIT)
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.


* `This Library is a cirucit python port of 
   Seeed Grove_Multichannel_Gas_Sensor V2.0 by Seeed-Studio
   <https://github.com/Seeed-Studio/Seeed_Arduino_MultiGas>`_


* Author: Pascal S (theholypumpkin)

**Hardware:**

* `Seeedstrudio Grove - Multichannel Gas Sensor v2
  <https://www.seeedstudio.com/Grove-Multichannel-Gas-Sensor-v2-p-4569.html>`_

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

 * Adafruit's Bus Device library: https://github.com/adafruit/Adafruit_CircuitPython_BusDevice
 * Adafruit's Register library: https://github.com/adafruit/Adafruit_CircuitPython_Register

**Notes:**

* `To get the Athmosapheric conentration of any of the measurable gasses use 
   - measureNO2
   - measureC2H5OH
   - measureVOC
   - measureCO

   To get Volage use:
   - measureNO2_Voltage
   - measureC2H5OH_Voltage
   - measureVOC_Voltage
   - measureCO_Voltage

   Using 
   _getGM102B, _getGM302B, _getGM502B, _getGM502B. is not recommended because of readablility,
   but it will work, and will return the Atmospheric concentration of the particular gas the
   sensor is measuring.`
"""
import time
import struct
from micropython import const
from adafruit_bus_device.i2c_device import I2CDevice
from adafruit_register import i2c_bit
from adafruit_register import i2c_bits

__version__ = "1.0.0"
__repo__ = "https://github.com/theholypumpkin/Circuitpython-Groove-Multichannel-Gas-Sensor-lib.git"

_GM_N02_VALUE = const(0x01)         # Nitrogend Dioxide Sensor
# Alcohole, Acetone, Methybenzene Formeldahyde Sensor
_GM_C2H5CH_VALUE = const(0x03)
_GM_VOC_VALUE = const(0x05)         # Vloitile Organcic Compounds Sensors
_GM_CO_VALUE = const(0x07)          # Carbonmoxide Sensor
_GM_CHANGE_I2C_ADDR = const(0x55)   # Change the i2c bus address
_GM_WARM_UP = const(0xFE)           # Warm-up
_GM_WARM_DOWN = const(0xFF)         # warm-down

_GM_RESOLUTION = const(1023)

# TODO explenation of this class


class GM_Multi_Gas:
    """
    Seeedstrudio Grove - Multichannel Gas Sensor v2 Driver

    :param ~busio.I2C i2c_bus: The I2C bus the Sensor is connected to
    :param int address: The I2C address of the Sesnsor. Defaults to :const:`0x08`

    **Quickstart: Importing and using the Multichannel Gas Sensor v2**

        Here is an example of using the :class:`GM_Multi_Gas` class.
        First you will need to import the libraries to use the sensor

        .. code-block:: python

            import board
            import multichannel_gas_sensor
            from busio import I2C

        Once this is done you can define your `board.I2C` object and define your sensor object

        .. code-block:: python

            i2c = board.I2C()   # uses board.SCL and board.SDA
            gas = multichannel_gas_sensor.GM_Multi_Gas(i2c)

        Now you have access to the :attr:`no2`, `c2h5oh`, `voc` and :attr:`co` attributes.

        .. code-block:: python

            no2 = gas.measureNO2()
            co = gas.measureCO()
            c2h5oh = gas.measureC2H5OH()
            voc = gas.measureVOC()

        To get the Sensor Voltage :attr:`no2_vol`, `c2h5oh_vol`, `voc_vol` and :attr:`co_vol` attributes.

        .. code-block:: python

            no2_vol = gas.measureNO2_Voltage()
            co_vol = gas.measureCO_Voltage()
            c2h5oh_vol = gas.measureC2H5OH_Voltage()
            voc_vol = gas.measureVOC_Voltage()

    """

    isPreheated = False

    def __init__(self, i2c_bus, address=0x08):
        self.i2c_device = I2CDevice(i2c_bus, address)

    def _GMWriteByte(self, registerAddr: const):
        """Writing a byte to a defined register"""
        with self.i2c_device as i2c:
            # converts the constant int into a bytearray to be bufferable
            i2c.write(bytes([registerAddr]), end=1)
        time.sleep(0.1)

    # This messege read 4 bytes at a given adress
    def _getData(self, registerAddr: const):
        """Getting the sensor data from a speific register"""
        buf = bytearray(4)
        with self.i2c_device as i2c:
            # Reads 4 bytes from a defined Register Address
            # converts the constant int into a bytearray to be bufferable
            i2c.write_then_readinto(bytes([registerAddr]), buf)
        time.sleep(0.1)
        # unpacks the bytearray into an integer
        return struct.unpack('<i', buf)

    def preheated(self):
        """Warms up the sensors"""
        self._GMWriteByte(_GM_WARM_UP)
        self.isPreheated = True

    def unpreheated(self):
        """Cools down the sensors"""
        self._GMWriteByte(_GM_WARM_DOWN)
        self.isPreheated = False

    # Updates the i2c device with a new address
    def setAddress(self, i2c_bus, address):
        """sets the sensor i2c adress in case it changed"""
        self.i2c_device = I2CDevice(i2c_bus, address)
        self.preheated()

    def changeGMAddress(self, new_i2c_address: bytes):
        """change the I2C address of gas sonsor"""
        if new_i2c_address == 0 or new_i2c_address > 127:
            print(f'{new_i2c_address} is an invalid address.\n The Adress has to be higher than 0 and lower than 128\n Keeping Current Address')
        else:
            with self.i2c_device as i2c:
                # Writes to the intended i2c adress to change the address to the new address
                buf = [_GM_CHANGE_I2C_ADDR, new_i2c_address]
                i2c.write(buf)
            time.sleep(0.1)

    def _getGM102B(self):
        """get the adc value of GM102B"""
        if not self.isPreheated:
            self.preheated()
        return self._getData(_GM_N02_VALUE)

    def _getGM302B(self):
        """get the adc value of GM302B"""
        if not self.isPreheated:
            self.preheated()
        return self._getData(_GM_C2H5CH_VALUE)

    def _getGM502B(self):
        """get the adc value of GM502B"""
        if not self.isPreheated:
            self.preheated()
        return self._getData(_GM_VOC_VALUE)

    def _getGM702B(self):
        """get the adc value of GM702B"""
        if not self.isPreheated:
            self.preheated()
        return self._getData(_GM_CO_VALUE)

    def calcVol(self, adc: float):
        """Calculates the voltage based on the parts per billion value"""
        return (adc[0] * 3.3)/_GM_RESOLUTION

    def measureNO2_Voltage(self):
        """The Voltage of the Nitrogendioxide Sensor as a decimal number in Volts"""
        adc = self._getGM102B()
        return self.calcVol(adc)

    def measureC2H5OH_Voltage(self):
        """The Voltage of the Alcohole, Acetone, Methybenzene and Formeldahyde as a decimal number in Volts"""
        adc = self._getGM302B()
        return self.calcVol(adc)

    def measureVOC_Voltage(self):
        """The Voltage of the Volatile Organic Compound Sensor as a decimal number in Volts"""
        adc = self._getGM502B()
        return self.calcVol(adc)

    def measureCO_Voltage(self):
        """The Voltage of the Carbonmonoxide Sensor as a decimal number in Volts"""
        adc = self._getGM702B()
        return self.calcVol(adc)

    def measureNO2(self):
        """Total Atmospheric Nitrogendioxide level in parts per billion"""
        adc = self._getGM102B()
        return adc[0]

    def measureC2H5OH(self):
        """Total Alcohole, Acetone, Methybenzene and Formeldahyde level in parts per billion"""
        adc = self._getGM302B()
        return adc[0]

    def measureVOC(self):
        """Total Volatile Organic Compound in parts per billion."""
        adc = self._getGM502B()
        return adc[0]

    # TODO explenation of this method
    def measureCO(self):
        """Total Atmospheric Carbonmonoxide level in parts per billion"""
        adc = self._getGM702B()
        return adc[0]

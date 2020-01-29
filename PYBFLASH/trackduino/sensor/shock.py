from pyb import Pin, ADC
from trackduino.common import constrain, analog_read


class ShockSensor:
    def __init__(self, pin: Pin):
        self._adc = ADC(pin)

    def read(self):
        return analog_read(self._adc, bit=10)

    def shock(self, threshold=55):
        return self.read() <= constrain(threshold, 0, 1023)

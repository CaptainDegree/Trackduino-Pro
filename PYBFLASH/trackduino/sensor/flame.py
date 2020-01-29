from pyb import Pin, ADC
from trackduino.common import constrain, analog_read


class FlameSensor:
    def __init__(self, pin: Pin):
        self._adc = ADC(pin)

    def read(self):
        return analog_read(self._adc, bit=10)

    def flame(self, threshold=900):
        return self.read() >= constrain(threshold, 0, 1023)

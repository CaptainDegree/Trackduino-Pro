from pyb import Pin, ADC
from trackduino.common import constrain, analog_read


class IRSensor:
    def __init__(self, pin: Pin):
        self._adc = ADC(pin)

    def read(self):
        return analog_read(self._adc, bit=10)

    def white(self, threshold=700):
        return self.read() >= constrain(threshold, 0, 1023)

    def black(self, threshold=700):
        return not self.is_white()

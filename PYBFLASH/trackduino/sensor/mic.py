from pyb import Pin, ADC
from trackduino.common import constrain, analog_read


class MicSensor:
    def __init__(self, pin: Pin):
        self._adc = ADC(pin)

    def read(self):
        pass


class AnalogMicSensor(MicSensor):
    def __init__(self, pin: Pin):
        super().__init__(pin)
    
    def read(self):
        reading = 0
        for _ in range(150):
            new_reading = analog_read(self._adc, bit=10)
            if new_reading > reading:
                reading = new_reading
        
        return reading


class DigitalMicSensor(MicSensor):
    def __init__(self, pin: Pin):
        self._adc = ADC(Pin(pin, mode=Pin.IN, pull=Pin.PULL_UP))
    
    def sound(self, threshold=100):
        return analog_read(self._adc, bit=10) <= constrain(threshold, 0, 1023)

from pyb import Pin
from trackduino.common import amap, analog_write_percent, constrain, has_pwm


class BuiltinLED:
    class Color:
        BLACK = (False, False, False)
        RED = (False, False, True)
        GREEN = (False, True, False)
        BLUE = (True, False, False)
        YELLOW = (False, True, True)
        PURPLE = (True, False, True)
        CYAN = (True, True, False)
        WHITE = (True, True, True)

    def __init__(self):
        self._pin_r = Pin(Pin.cpu.E15, mode=Pin.OUT)
        self._pin_g = Pin(Pin.cpu.D0, mode=Pin.OUT)
        self._pin_b = Pin(Pin.cpu.D1, mode=Pin.OUT)

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(BuiltinLED, cls).__new__(cls)
        return cls.instance

    @property
    def color(self):
        return (self._pin_b, self._pin_g, self._pin_r)

    @color.setter
    def color(self, color):
        self._pin_b.value(color[0])
        self._pin_g.value(color[1])
        self._pin_r.value(color[2])

    def on(self):
        self.color = BuiltinLED.Color.WHITE

    def off(self):
        self.color = BuiltinLED.Color.BLACK

class LED:
    class Mode:
        DIGITAL = 0
        ANALOG = 1
    
    def __init__(self, pin: Pin, mode=None):
        self._pin = pin
        self._value = 0

        if mode is None or mode == LED.Mode.DIGITAL:
            self._mode = LED.Mode.DIGITAL
        elif mode == LED.Mode.ANALOG:
            if has_pwm(pin):
                self._mode = mode
            else:
                raise ValueError('Specified pin cannot be used in analog mode. Use one of the PWM pins')
        else:
            raise ValueError('Unknown mode')

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        self._value = constrain(value, 0, 100)

        if self._mode == LED.Mode.ANALOG:
            analog_write_percent(self._pin, self._value)
        else:
            self._pin.value(amap(self._value, 0, 100, 0, 1))
    
    def on(self):
        self.value = 100
    
    def off(self):
        self.value = 0

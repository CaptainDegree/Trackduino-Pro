from pyb import Pin, udelay
from machine import time_pulse_us
from micropython import const
from trackduino.common import constrain


class UltrasonicSensor:
    _DIVIDER_CM = const(58)
    _MIN_DISTANCE_CM = const(2)
    _MAX_DISTANCE_CM = const(400)

    _DIVIDER_IN = const(148)
    _MIN_DISTANCE_IN = _MIN_DISTANCE_CM * _DIVIDER_CM / _DIVIDER_IN
    _MAX_DISTANCE_IN = _MAX_DISTANCE_CM * _DIVIDER_CM / _DIVIDER_IN

    def __init__(self, pin: Pin):
        self._pin = pin
    
    def _send_pulse(self):
        pin = Pin(self._pin, mode=Pin.OUT)
        pin.low()
        udelay(2)
        pin.high()
        udelay(10)
        pin.low()
        pin = Pin(self._pin, mode=Pin.IN)
    
    def _distance(self, min_value, max_value, divider):
        self._send_pulse()
        
        duration = time_pulse_us(self._pin, 1, 20_000)
        if duration != -1:
            return constrain(duration / divider, min_value, max_value)
        else:
            return -1
    
    def distance_cm(self):
        return self._distance(self._MIN_DISTANCE_CM, self._MAX_DISTANCE_CM, self._DIVIDER_CM)
    
    def distance_in(self):
        return self._distance(self._MIN_DISTANCE_IN, self._MAX_DISTANCE_IN, self._DIVIDER_IN)

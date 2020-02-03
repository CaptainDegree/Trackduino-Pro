from pyb import Pin, delay
from trackduino.common import amap, constrain, has_pwm
from trackduino.timer_manager import *


class Buzzer:
    def __init__(self, pin: Pin, freq=450, volume=100):
        self._pin = pin
        if not has_pwm(self._pin):
            raise ValueError('Specified pin cannot be used for buzzer. Use one of the PWM pins')

        self._freq = 0
        self._is_on = False
        self._volume = 0

        self._timer = TimerManager().get_timer_for_pin(self._pin)
        self._channel = TimerManager().get_timer_channel_for_pin(self._pin)
        
        self.freq = freq
        self.volume = volume

    @property
    def freq(self):
        return self._freq
    
    @freq.setter
    def freq(self, freq):
        self._freq = constrain(freq, 0, 18_000)
        self._timer.freq(self._freq)
    
    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, volume):
        self._volume = amap(constrain(volume, 0, 100), 0, 100, 0, 8)

        if self._is_on:
            self.on()
    
    def on(self):
        self._is_on = True
        TimerManager.set_percent(self._channel, self._volume)
    
    def off(self):
        self._is_on = False
        TimerManager.set_percent(self._channel, 0)
    
    def tone(self, freq=None, volume=None, time_ms):
        if freq is not None:
            self.freq = freq
        if volume is not None:
            self.volume = volume
        
        self.on()
        delay(time_ms)
        self.off()

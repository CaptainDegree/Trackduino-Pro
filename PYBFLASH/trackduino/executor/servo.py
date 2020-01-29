from trackduino.timer_manager import *
from trackduino.common import amap, constrain


class Servo:
    def __init__(self, pin):
        self._min_duty = 500
        self._max_duty = 0

        tim = TimerManager().get_timer_for_pin(pin)
        tim.freq(50)

        self._timer_channel = TimerManager().get_timer_channel_for_timer_on_pin(tim, pin)

    def center(self):
        self._timer_channel.pulse_width((self._min_duty + self._max_duty) // 2)

    def angle(self, angle):
        angle = constrain(angle, 0, 180)
        width = amap(angle, 0, 180, self._min_duty, self._max_duty)
        self._timer_channel.pulse_width(int(width))


class SmallServo(Servo):
    def __init__(self, pin):
        super().__init__(pin)
        self._max_duty = 1500


class BigServo(Servo):
    def __init__(self, pin):
        super().__init__(pin)
        self._min_duty = 800
        self._max_duty = 1500

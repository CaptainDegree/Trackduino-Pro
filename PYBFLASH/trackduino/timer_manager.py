from pyb import Timer
from trackduino.pins import TrackduinoPin as Pins


class TimerManager:
    def __init__(self):
        # (timer number, channel number) for specified pins
        self._timer_pinout = {
            id(Pins.Out.PWM.OUT1): (3, 2),
            id(Pins.Out.PWM.OUT2): (3, 3),
            id(Pins.Out.PWM.OUT3): (3, 4),
            id(Pins.Out.PWM.OUT4): (2, 4),
            id(Pins.Out.PWM.OUT5): (12, 2),
            id(Pins.Motor.M1_ENC): (4, 2),
            id(Pins.Motor.M2_ENC): (4, 1),
            id(Pins.Motor.M3_ENC): (4, 3),
            id(Pins.Motor.M4_ENC): (4, 4)
        }

        self._active_timers = dict()
        self._active_channels = dict()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(TimerManager, cls).__new__(cls)
        return cls.instance

    @classmethod
    def _make_timer(cls, timer_number, freq=1000):
        return Timer(timer_number, freq=freq)

    @classmethod
    def _make_channel(cls, timer: Timer, channel_number, pin):
        channel = timer.channel(channel_number, Timer.PWM,
                                pin=pin, pulse_width=16000)
        cls.set_percent(channel, 0)

        return channel

    def get_timer_for_pin(self, pin):
        timer_num = None

        if id(pin) in self._timer_pinout:
            timer_num, _ = self._timer_pinout.get(id(pin))
        else:
            raise ValueError("This pin does not allow PWM")

        timer = None

        if timer_num not in self._active_timers:
            timer = self._make_timer(timer_num)
            self._active_timers[timer_num] = timer
        else:
            timer = self._active_timers[timer_num]

        return timer

    def get_timer_channel_for_timer_on_pin(self, timer, pin):
        timer_num, channel_num = None, None
        if id(pin) in self._timer_pinout:
            timer_num, channel_num = self._timer_pinout.get(id(pin))
        else:
            raise ValueError("This pin does not allow PWM")

        channel = None

        if (timer_num, channel_num) not in self._active_channels:
            channel = self._make_channel(timer, channel_num, pin)
            self._active_channels[(timer_num, channel_num)] = channel
        else:
            channel = self._active_channels[(timer_num, channel_num)]

        return channel

    def get_timer_channel_for_pin(self, pin):
        return self.get_timer_channel_for_timer_on_pin(self.get_timer_for_pin(pin), pin)

    @classmethod
    def set_percent(cls, channel: TimerChannel, percent):
        channel.pulse_width_percent(percent)

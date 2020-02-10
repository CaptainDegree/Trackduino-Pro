from micropython import const
from pyb import Pin, micros, elapsed_micros, millis
import uctypes


class IRRC(object):
    class Channel(object):
        CHANNEL_1 = const(0xFC)
        CHANNEL_2 = const(0x3C)
        CHANNEL_3 = const(0xCC)
        CHANNEL_4 = const(0x0C)
        CHANNEL_5 = const(0xF0)
        CHANNEL_6 = const(0x30)
        CHANNEL_7 = const(0xC0)
        CHANNEL_8 = const(0x00)

    class Key(object):
        UP = const(0x1FC3)
        DOWN = const(0x1F)
        LEFT = const(0x07)
        RIGHT = const(0x73)

        UP_AND_LEFT_KEY = const(0x7C3)
        UP_AND_RIGHT_KEY = const(0x7F)
        DOWN_AND_LEFT_KEY = const(0x70F)
        DOWN_AND_RIGHT_KEY = const(0x1CF)

        F1 = const(0x7CF)
        F2 = const(0x1C3F)
        F3 = const(0x7F3)
        F4 = const(0x1CCF)
        F5 = const(0x1F0F)
        F6 = const(0x703)
        OFF = const(0x733)

    _TIMEOUT = const(500)
    _SHIFT = const(8)

    def __init__(self, pin: Pin, channel: int):
        self._CHANNELS = (self.Channel.CHANNEL_1, self.Channel.CHANNEL_2, self.Channel.CHANNEL_3, self.Channel.CHANNEL_4,
                     self.Channel.CHANNEL_5, self.Channel.CHANNEL_6, self.Channel.CHANNEL_7, self.Channel.CHANNEL_8)
        self._KEYS = (self.Key.UP, self.Key.DOWN, self.Key.LEFT, self.Key.RIGHT, self.Key.UP_AND_LEFT_KEY, self.Key.UP_AND_RIGHT_KEY, self.Key.DOWN_AND_LEFT_KEY,
                 self.Key.DOWN_AND_RIGHT_KEY, self.Key.F1, self.Key.F2, self.Key.F3, self.Key.F4, self.Key.F5, self.Key.F6, self.Key.OFF)

        self._pin = Pin(pin, mode=Pin.IN, pull=Pin.PULL_UP)
        self.channel = channel

        self._button_id = 0
        self._impulse = True
        self._res = 0
        self._state = 0
        self._timeout_mark = 0
        self._buf = 0

        self._time = micros()

        self._pin.irq(lambda p: self._update())

    @property
    def channel(self) -> int:
        return self._channel

    @channel.setter
    def channel(self, channel: int):
        if channel in self._CHANNELS:
            self._channel = channel
        else:
            raise ValueError("`channel` must be the one of IRRC.Channel")

    @property
    def _res(self):
        return self._res

    @_res.setter
    def _res(self, _res):
        self._res = _res & (uctypes.UINT32 - 1)

    @property
    def _buf(self):
        return self._buf

    @_buf.setter
    def _buf(self, _buf):
        self._buf = _buf & (uctypes.UINT8 - 1)

    @property
    def _button_id(self):
        return self._button_id

    @_button_id.setter
    def _button_id(self, _button_id):
        self._button_id = _button_id & (uctypes.UINT32 - 1)

    @property
    def _state(self):
        return self._state

    @_state.setter
    def _state(self, _state):
        self._state = _state & 0x7F

    def _update(self):
        diff_time = elapsed_micros(self._time)
        self._time += diff_time

        self._buf = diff_time
        del diff_time

        if self._buf % 200 > 101:
            self._buf = (self._buf // 200) + 1
        else:
            self._buf //= 200

        if self._buf == 0:
            self._buf = 1

        if self._state == 0:
            if not self._impulse:
                self._state += 1
                self._res = 0 << self._buf
        else:
            if self._impulse:
                self._res <<= self._buf
                for i in range(self._buf):
                    self._res |= 1 << i
            else:
                self._res <<= self._buf

                if (self._res & 0x7F) == 0x38:
                    self._buf = 1

                    for i in range(1, self._SHIFT):
                        self._buf = (self._buf << 1) + 1

                    channel_buf = ((self._res >> 6) & self._buf) & 0x7F  # channel_buf is byte

                    if channel_buf == self._channel:
                        self._button_id = self._res >> (6 + self._SHIFT)

                        while not (self._button_id & 1):
                            self._button_id >>= 1

                        self._timeout_mark = millis()

                    self._state = 0
                    self._res = 0

        self._impulse = not self._impulse

    def pressed(self, key: int) -> bool:
        if key in self._KEYS:
            pass
        else:
            raise ValueError("`key` must be the one of IRRC.KEY")

        if (millis() - self._timeout_mark >= self._TIMEOUT):
            self._button_id = self.Key.OFF

        if (key == self._button_id):
            return True

        return False

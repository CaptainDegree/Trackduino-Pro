from micropython import const
from pyb import Pin


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

    _CHANNELS = tuple(IRRC.Channel.CHANNEL_1, IRRC.Channel.CHANNEL_2, IRRC.Channel.CHANNEL_3, IRRC.Channel.CHANNEL_4,
                      IRRC.Channel.CHANNEL_5, IRRC.Channel.CHANNEL_6, IRRC.Channel.CHANNEL_7, IRRC.Channel.CHANNEL_8)
    _KEYS = tuple(IRRC.Key.UP, IRRC.Key.DOWN, IRRC.Key.LEFT, IRRC.Key.RIGHT, IRRC.Key.UP_AND_LEFT_KEY, IRRC.Key.UP_AND_RIGHT_KEY,
                  IRRC.Key.DOWN_AND_LEFT_KEY, IRRC.Key.DOWN_AND_RIGHT_KEY, IRRC.Key.F1, IRRC.Key.F2, IRRC.Key.F3, IRRC.Key.F4, IRRC.Key.F5, IRRC.Key.F6, IRRC.Key.OFF)

    _TIMEOUT = const(500)
    _SHIFT = const(8)

    def __init__(self, pin: Pin, channel: int):
        self._pin = pin
        self.channel = channel

    @property
    def channel(self) -> int:
        return self._channel

    @channel.setter
    def channel(self, channel: int):
        if channel in IRRC._CHANNELS:
            self._channel = channel
        else:
            raise ValueError("`channel` must be the one of IRRC.Channel")

    def pressed(self, key: int) -> bool:
        if key in IRRC._KEYS:
            pass
        else:
            raise ValueError("`key` must be the one of IRRC.KEY")

from pyb import ADC, Pin
from trackduino.timer_manager import TimerManager
from trackduino.pins import TrackduinoPin as Pins


class ReferencableVariable:
    """
    This class allows to operate variables as well, as you pass them by a pointer

    Parameters
    ----------
    `value` : An initial value of the variable

    Examples
    --------
    >>> a = ReferencableVariable(4)
    >>> a.get()
    4
    >>> b = a
    >>> b.set(128)
    >>> a.get()
    128
    >>> c = b
    >>> c.set(64)
    >>> a.get()
    64
    """

    def __init__(self, value):
        self._value = None
        self.set(value)

    def get(self):
        return self._value

    def set(self, value):
        self._value = value


def constrain(value, min_value, max_value):
    """
    Constrains the `value` to the specified range `[min_value, max_value]`

    Parameters
    ----------
    `value` : The value to be constrained

    `min_value` : The lower limit of range (inclusive)

    `max_value` : The upper limit of range (inclusive)

    Returns
    -------
    `min_value` : if `value` is less than `min_value`

    `max_value` : if `value` is greater than `max_value`

    `value` : otherwise

    Examples
    --------
    >>> constrain(10, 20, 40)
    20
    >>> constrain(30, 20, 40)
    30
    >>> constrain(50, 20, 40)
    40
    """

    return min(max(value, min_value), max_value)


def amap(x, in_min, in_max, out_min, out_max):
    """
    This is an analog of Arduino's `map()` function. It maps the `x` located in range `[in_min, in_max]` to a new value located in range `[out_min, out_max]` accordingly to the position of `x` in `in`-range

    This function does not check if `x` is really located in `in`-range. In some situations it may be needed to perform `constrain(x, in_min, in_max)` before passing to this function as `x`

    Parameters
    ----------
    `x` : The value to be mapped

    `in_min` : The lower limit of input range (inclusive)

    `in_max` : The upper limit of input range (inclusive)

    `out_min` : The lower limit of output range (inclusive)

    `out_max` : The upper limit of output range (inclusive)

    Returns
    -------
    `x` which is mapped to the `out`-range

    Examples
    --------
    >>> amap(5, 0, 10, 10, 20)
    15.0
    >>> amap(0, -10, 10, 0, 10)
    5.0
    >>> amap(-8, -8, -4, 2, 6)
    2.0
    >>> amap(2.5, 0, 5, 0, 1)
    0.5
    """

    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def analog_read(adc_pin, bit=10):
    data = adc_pin.read()
    bit = constrain(bit, 8, 12)

    return data >> (12 - bit)


def analog_write_percent(pin, percent):
    channel = TimerManager().get_timer_channel_for_pin(pin)
    TimerManager.set_percent(channel, percent)


def has_pwm(pin: Pin):
    if pin == Pins.Out.PWM.OUT1 or \
       pin == Pins.Out.PWM.OUT2 or \
       pin == Pins.Out.PWM.OUT3 or \
       pin == Pins.Out.PWM.OUT4 or \
       pin == Pins.Out.PWM.OUT5 or \
       pin == Pins.Analog.A0 or \
       pin == Pins.Analog.A1 or \
       pin == Pins.Analog.A2 or \
       pin == Pins.Analog.A3 or \
       pin == Pins.Analog.A4 or \
       pin == Pins.Analog.A5 or \
       pin == Pins.Digital.PWM.D3 or \
       pin == Pins.Digital.PWM.D5 or \
       pin == Pins.Digital.PWM.D6 or \
       pin == Pins.Digital.PWM.D9 or \
       pin == Pins.Digital.PWM.D11:

        return True

    return False

def average(iterable):
    return sum(iterable) / len(iterable)

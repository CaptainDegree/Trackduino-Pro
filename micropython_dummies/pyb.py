from typing import Optional, List, Tuple, Union


def delay(ms: int) -> None:
    """
    Delay for the given number of milliseconds.
    """
    pass


def udelay(us: int) -> None:
    """
    Delay for the given number of microseconds.
    """
    pass


def millis() -> int:
    """
    Returns the number of milliseconds since the board was last reset.

    The result is always a MicroPython smallint (31-bit signed number), so after 2^30 milliseconds (about 12.4 days) this will start to return negative numbers.

    Note that if `pyb.stop()` is issued the hardware counter supporting this function will pause for the duration of the "sleeping" state. This will affect the outcome of `pyb.elapsed_millis()`.
    """
    pass


def micros() -> int:
    """
    Returns the number of microseconds since the board was last reset.

    The result is always a MicroPython smallint (31-bit signed number), so after 2^30 microseconds (about 17.8 minutes) this will start to return negative numbers.

    Note that if `pyb.stop()` is issued the hardware counter supporting this function will pause for the duration of the "sleeping" state. This will affect the outcome of `pyb.elapsed_micros()`.
    """
    pass


def elapsed_millis(start: int) -> int:
    """
    Returns the number of milliseconds which have elapsed since start.

    This function takes care of counter wrap, and always returns a positive number. This means it can be used to measure periods up to about 12.4 days.

    Example:

    >>> start = millis()
    >>> while elapsed_millis(start) < 1000:
    >>>     # Perform some operation
    """
    pass


def elapsed_micros(start: int) -> int:
    """
    Returns the number of microseconds which have elapsed since start.

    This function takes care of counter wrap, and always returns a positive number. This means it can be used to measure periods up to about 17.8 minutes.

    Example:

    >>> start = micros()
    >>> while elapsed_micros(start) < 1000:
    >>>     # Perform some operation
    >>>     pass
    """
    pass


def hard_reset() -> None:
    """Resets the board in a manner similar to pushing the external RESET button."""
    pass


def disable_irq() -> None:
    """
    Disable interrupt requests. Returns the previous IRQ state: `False`/`True` for disabled/enabled IRQs respectively. This return value can be passed to enable_irq to restore the IRQ to its original state.
    """
    pass


def enable_irq(state: bool = True) -> None:
    """
    Enable interrupt requests. If `state` is `True` (the default value) then IRQs are enabled. If `state` is `False` then IRQs are disabled. The most common use of this function is to pass it the value returned by `disable_irq` to exit a critical section.
    """
    pass


def wfi() -> None:
    """
    Wait for an internal or external interrupt.

    This executes a `wfi` instruction which reduces power consumption of the MCU until any interrupt occurs (be it internal or external), at which point execution continues. Note that the system-tick interrupt occurs once every millisecond (1000Hz) so this function will block for at most 1ms.
    """
    pass


def stop() -> None:
    """
    Put the board in a "sleeping" state.

    This reduces power consumption to less than 500 uA. To wake from this sleep state requires an external interrupt or a real-time-clock event. Upon waking execution continues where it left off.
    """
    pass


def standby() -> None:
    """
    Put the board into a "deep sleep" state.

    This reduces power consumption to less than 50 uA. To wake from this sleep state requires a real-time-clock event, or an external interrupt on `(PA0=WKUP)` or `(PC13=TAMP1)`. Upon waking the system undergoes a hard reset.
    """
    pass


def main(filename: str) -> None:
    """
    Set the filename of the main script to run after `boot.py` is finished. If this function is not called then the default file `main.py` will be executed.

    It only makes sense to call this function from within `boot.py`.
    """
    pass


def rng() -> int:
    """Return a 30-bit hardware generated random number."""
    pass


class ADC(object):
    """
    Create an ADC object associated with the given pin. This allows you to then read analog values on that pin.
    """

    def __init__(self, pin: Pin):
        pass

    def read(self) -> int:
        """Read the value on the analog pin and return it. The returned value will be between 0 and 4095."""
        pass


class Pin(object):
    """
    A Pin represents a physical pin on the microprocessor. Each pin can have a variety of functions.

    Constants:

    IN  - initialise the pin to input mode

    OUT - initialise the pin to output mode

    OUT_OD  - initialise the pin to output mode with an open-drain drive

    OUT_PP  - initialise the pin to output mode with a push-pull drive

    AF_OD   - initialise the pin to alternate-function mode with an open-drain drive

    AF_PP   - initialise the pin to alternate-function mode with a push-pull drive

    ANALOG  - initialise the pin to analog mode

    PULL_NONE   - don’t enable any pull up or down resistors on the pin

    PULL_UP - enable the pull-up resistor on the pin

    PULL_DOWN   - enable the pull-down resistor on the pin
    """

    class cpu(object):
        # region A
        A0 = None
        A1 = None
        A2 = None
        A3 = None
        A4 = None
        A5 = None
        A6 = None
        A7 = None
        A8 = None
        A9 = None
        A10 = None
        A11 = None
        A12 = None
        A13 = None
        A14 = None
        A15 = None
        # endregion
        # region B
        B0 = None
        B1 = None
        B2 = None
        B3 = None
        B4 = None
        B5 = None
        B6 = None
        B7 = None
        B8 = None
        B9 = None
        B10 = None
        B11 = None
        B12 = None
        B13 = None
        B14 = None
        B15 = None
        # endregion
        # region C
        C0 = None
        C1 = None
        C2 = None
        C3 = None
        C4 = None
        C5 = None
        C6 = None
        C7 = None
        C8 = None
        C9 = None
        C10 = None
        C11 = None
        C12 = None
        C13 = None
        C14 = None
        C15 = None
        # endregion
        # region D
        D0 = None
        D1 = None
        D2 = None
        D3 = None
        D4 = None
        D5 = None
        D6 = None
        D7 = None
        D8 = None
        D9 = None
        D10 = None
        D11 = None
        D12 = None
        D13 = None
        D14 = None
        D15 = None
        # endregion
        # region E
        E0 = None
        E1 = None
        E2 = None
        E3 = None
        E4 = None
        E5 = None
        E6 = None
        E7 = None
        E8 = None
        E9 = None
        E10 = None
        E11 = None
        E12 = None
        E13 = None
        E14 = None
        E15 = None
        # endregion

    IN = None
    OUT = None
    OUT_OD = None
    OUT_PP = None
    AF_OD = None
    AF_PP = None
    ANALOG = None
    PULL_NONE = None
    PULL_UP = None
    PULL_DOWN = None

    def __init__(self, id, mode=IN, pull=PULL_NONE):
        pass

    def init(self, mode: int, pull: int = PULL_NONE, af: int = -1) -> None:
        """
        Initialise the pin:

        `mode` can be one of:

        - `Pin.IN`        - configure the pin for input;

        - `Pin.OUT_PP`    - configure the pin for output, with push-pull control;

        - `Pin.OUT_OD`    - configure the pin for output, with open-drain control;

        - `Pin.AF_PP`     - configure the pin for alternate function, pull-pull;

        - `Pin.AF_OD`     - configure the pin for alternate function, open-drain;

        - `Pin.ANALOG`    - configure the pin for analog.

        `pull` can be one of:

        - `Pin.PULL_NONE`  - no pull up or down resistors;

        - `Pin.PULL_UP`    - enable the pull-up resistor;

        - `Pin.PULL_DOWN`  - enable the pull-down resistor.

        when `mode` is `Pin.AF_PP` or `Pin.AF_OD`, then af can be the index or name of one of the alternate functions associated with a pin.
        """
        pass

    def value(self, value: Optional[bool] = None) -> Optional[int]:
        """
        Get or set the digital logic level of the pin:

        - With no argument, return 0 or 1 depending on the logic level of the pin.

        - With `value` given, set the logic level of the pin. `value` can be anything that converts to a boolean. If it converts to `True`, the pin is set high, otherwise it is set low.
        """
        pass

    def af(self) -> int:
        """
        Returns the currently configured alternate-function of the pin. The integer returned will match one of the allowed constants for the af argument to the init function.
        """
        pass

    def af_list(self) -> List[PinAF]:
        """
        Returns an array of alternate functions available for this pin.
        """
        pass

    def mode(self) -> int:
        """
        Returns the currently configured mode of the pin. The integer returned will match one of the allowed constants for the mode argument to the init function.
        """
        pass

    def name(self) -> str:
        """
        Get the pin name.
        """
        pass

    def names(self) -> Tuple[str, str]:
        """
        Returns the cpu and board names for this pin
        """
        pass

    def pin(self) -> int:
        """
        Get the pin number.
        """
        pass

    def port(self) -> int:
        """
        Get the pin port.
        """
        pass

    def pull(self) -> int:
        """
        Returns the currently configured pull of the pin. The integer returned will match one of the allowed constants for the pull argument to the init function.
        """
        pass


class PinAF(object):
    """
    A Pin represents a physical pin on the microprocessor. Each pin can have a variety of functions (GPIO, I2C SDA, etc). Each PinAF object represents a particular function for a pin.
    """

    def __init__(self):
        pass

    def index(self) -> int:
        """
        Return the alternate function index.
        """
        pass

    def name(self) -> str:
        """
        Return the name of the alternate function.
        """
        pass

    def reg(self) -> int:
        """
        Return the base register associated with the peripheral assigned to this alternate function. For example, if the alternate function were `TIM2_CH3` this would return `stm.TIM2`
        """
        pass


class Timer(object):
    """
    Timers can be used for a great variety of tasks. At the moment, only the simplest case is implemented: that of calling a function periodically.

    Each timer consists of a counter that counts up at a certain rate. The rate at which it counts is the peripheral clock frequency (in Hz) divided by the timer prescaler. When the counter reaches the timer period it triggers an event, and the counter resets back to zero. By using the callback method, the timer event can call a Python function.
    """

    UP: int = None
    DOWN: int = None
    CENTER: int = None

    PWM: int = None
    PWM_INVERTED: int = None
    OC_TIMING: int = None
    OC_ACTIVE: int = None
    OC_INACTIVE: int = None
    OC_TOGGLE: int = None
    OC_FORCED_ACTIVE: int = None
    OC_FORCED_INACTIVE: int = None
    IC: int = None
    ENC_A: int = None
    ENC_B: int = None
    ENC_AB: int = None

    HIGH: int = None
    LOW: int = None

    RISING: int = None
    FALLING: int = None
    BOTH: int = None

    def __init__(self, id: int, freq: int = None, prescaler: int = None, period: int = None, mode: int = None, div: int = None, callback: function = None, deadtime: int = None):
        """
        Construct a new timer object of the given `id`. If additional arguments are given, then the timer is initialized by `init(...)`. id can be 1 to 14.

        `freq`  — specifies the periodic frequency of the timer. You might also view this as the frequency with which the timer goes through one complete cycle.

        `prescaler` [0-0xffff]  - specifies the value to be loaded into the timer’s Prescaler Register (PSC). The timer clock source is divided by `(prescaler + 1)` to arrive at the timer clock. Timers 2-7 and 12-14 have a clock source of 84 MHz (pyb.freq()[2] * 2), and Timers 1, and 8-11 have a clock source of 168 MHz (pyb.freq()[3] * 2).

        `period` [0-0xffff] for timers 1, 3, 4, and 6-15. [0-0x3fffffff] for timers 2 & 5. Specifies the value to be loaded into the timer’s AutoReload Register (ARR). This determines the period of the timer (i.e. when the counter cycles). The timer counter will roll-over after `period + 1` timer clock cycles.

        `mode` can be one of:

            `Timer.UP`  - configures the timer to count from 0 to ARR (default)

            `Timer.DOWN`    - configures the timer to count from ARR down to 0.

            `Timer.CENTER`  - configures the timer to count from 0 to ARR and then back down to 0.

        `div` can be one of 1, 2, or 4. Divides the timer clock to determine the sampling clock used by the digital filters.

        `callback`  - as per `Timer.callback()`

        `deadtime`  - specifies the amount of “dead” or inactive time between transitions on complimentary channels (both channels will be inactive) for this time). deadtime may be an integer between 0 and 1008, with the following restrictions: 0-128 in steps of 1. 128-256 in steps of 2, 256-512 in steps of 8, and 512-1008 in steps of 16. deadtime measures ticks of source_freq divided by div clock ticks. deadtime is only available on timers 1 and 8.
        """
        pass

    def deinit(self) -> None:
        """
        Deinitializes the timer.

        Disables the callback (and the associated irq).

        Disables any channel callbacks (and the associated irq). Stops the timer, and disables the timer peripheral.
        """
        pass

    def callback(self, fun: function) -> None:
        """
        Set the function to be called when the timer triggers. `fun` is passed 1 argument, the timer object. If `fun` is `None` then the callback will be disabled.
        """
        pass

    def channel(self, channel: int, mode: int, callback: function = None, pin: Pin = None, pulse_width: int = None, pulse_width_percent: int = None, compare: int = None, polarity: int = None) -> TimerChannel:
        """
        If only a channel number is passed, then a previously initialized channel object is returned (or `None` if there is no previous channel).

        Otherwise, a TimerChannel object is initialized and returned.

        Each channel can be configured to perform pwm, output compare, or input capture. All channels share the same underlying timer, which means that they share the same timer clock.

        Arguments

        `mode` can be one of:

            `Timer.PWM` — configure the timer in PWM mode (active high).
            `Timer.PWM_INVERTED`    — configure the timer in PWM mode (active low).
            `Timer.OC_TIMING`   — indicates that no pin is driven.
            `Timer.OC_ACTIVE`   — the pin will be made active when a compare match occurs (active is determined by polarity)
            `Timer.OC_INACTIVE` — the pin will be made inactive when a compare match occurs.
            `Timer.OC_TOGGLE`   — the pin will be toggled when an compare match occurs.
            `Timer.OC_FORCED_ACTIVE`    — the pin is forced active (compare match is ignored).
            `Timer.OC_FORCED_INACTIVE`  — the pin is forced inactive (compare match is ignored).
            `Timer.IC`  — configure the timer in Input Capture mode.
            `Timer.ENC_A`   — configure the timer in Encoder mode. The counter only changes when CH1 changes.
            `Timer.ENC_B`   — configure the timer in Encoder mode. The counter only changes when CH2 changes.
            `Timer.ENC_AB`  — configure the timer in Encoder mode. The counter changes when CH1 or CH2 changes.

        `callback`  - as per TimerChannel.callback()

        `pin` None (the default) or a Pin object. If specified (and not None) this will cause the alternate function of the the indicated pin to be configured for this timer channel. An error will be raised if the pin doesn’t support any alternate functions for this timer channel.

        Keyword arguments for `Timer.PWM` modes:

            `pulse_width`   - determines the initial pulse width value to use.

            `pulse_width_percent`   - determines the initial pulse width percentage to use.

        Keyword arguments for `Timer.OC` modes:

            `compare`   - determines the initial value of the compare register.

            `polarity` can be one of:

                `Timer.HIGH` - output is active high

                `Timer.LOW` - output is active low

        Optional keyword arguments for `Timer.IC` modes:

            `polarity` can be one of:

                `Timer.RISING`  - captures on rising edge.

                `Timer.FALLING` - captures on falling edge.

                `Timer.BOTH`    - captures on both edges.

        Note that capture only works on the primary channel, and not on the complimentary channels.

        Notes for `Timer.ENC` modes:

        Requires 2 pins, so one or both pins will need to be configured to use the appropriate timer AF using the Pin API.

        Read the encoder value using the timer.counter() method.

        Only works on CH1 and CH2 (and not on CH1N or CH2N)

        The channel number is ignored when setting the encoder mode.
        """
        pass

    def counter(self, value: Optional[int]) -> Optional[int]:
        """
        Get or set the timer counter.
        """
        pass

    def freq(self, value: Optional[int]) -> Optional[int]:
        """
        Get or set the frequency for the timer (changes prescaler and period if set).
        """
        pass
    
    def period(self, value: Optional[int]) -> Optional[int]:
        """
        Get or set the period of the timer.
        """
        pass

    def prescaler(self, value: Optional[int]) -> Optional[int]:
        """
        Get or set the prescaler for the timer.
        """
        pass

    def source_freq(self) -> int:
        """
        Get the frequency of the source of the timer.
        """
        pass


class TimerChannel(object):
    """
    Timer channels are used to generate/capture a signal using a timer.
    """
    
    def __init__(self):
        """
        TimerChannel objects are created using the `Timer.channel()` method.
        """
        pass

    def callback(self, fun: function) -> None:
        """
        Set the function to be called when the timer channel triggers. fun is passed 1 argument, the timer object. If fun is None then the callback will be disabled.
        """
        pass

    def capture(self, value: Optional[int]) -> Optional[int]:
        """
        Get or set the capture value associated with a channel. capture, compare, and pulse_width are all aliases for the same function. capture is the logical name to use when the channel is in input capture mode.
        """
        pass

    def compare(self, value: Optional[int]) -> Optional[int]:
        """
        Get or set the compare value associated with a channel. capture, compare, and pulse_width are all aliases for the same function. compare is the logical name to use when the channel is in output compare mode.
        """
        pass

    def pulse_width(self, value: Optional[int]) -> Optional[int]:
        """
        Get or set the pulse width value associated with a channel. capture, compare, and pulse_width are all aliases for the same function. pulse_width is the logical name to use when the channel is in PWM mode.

        In edge aligned mode, a `pulse_width` of `period + 1` corresponds to a duty cycle of 100%. In center aligned mode, a `pulse_width` of `period` corresponds to a duty cycle of 100%
        """
        pass

    def pulse_width_percent(self, value: Optional[int]) -> Optional[int]:
        """
        Get or set the pulse width percentage associated with a channel. The value is a number between 0 and 100 and sets the percentage of the timer period for which the pulse is active. The value can be an integer or floating-point number for more accuracy. For example, a value of 25 gives a duty cycle of 25%.
        """
        pass


class I2C(object):
    """
    I2C is a two-wire protocol for communicating between devices. At the physical level it consists of 2 wires: SCL and SDA, the clock and data lines respectively.

    I2C objects are created attached to a specific bus. They can be initialized when created, or initialized later on.

    Constants:

    `I2C.MASTER` - for initializing the bus to master mode
    `I2C.SLAVE` - for initializing the bus to slave mode
    """

    MASTER: int = None
    SLAVE: int = None

    def __init__(self, bus: int, mode: int, addr: int = 0x12, baudrate: int = 400000, gencall: bool = False, dma: bool = False):
        """
        Construct an I2C object on the given bus. With no additional parameters, the I2C object is created but not initialized (it has the settings from the last initialization of the bus, if any). If extra arguments are given, the bus is initialized. See init for parameters of initialization.
        """
        pass

    def init(self, mode: int, addr: int = 0x12, baudrate: int = 400000, gencall: bool = False, dma: bool = False):
        """
        Initialise the I2C bus with the given parameters:

        `mode` must be either `I2C.MASTER` or `I2C.SLAVE`
        
        `addr` is the 7-bit address (only sensible for a slave)
        
        `baudrate` is the SCL clock rate (only sensible for a master)
        
        `gencall` is whether to support general call mode
        
        `dma` is whether to allow the use of DMA for the I2C transfers (note that DMA transfers have more precise timing but currently do not handle bus errors properly)
        """
        pass

    def is_ready(self, addr: int):
        """
        Check if an I2C device responds to the given address. Only valid when in master mode.
        """
        pass

    def mem_read(self, data: Union[int, bytearray], addr: int, memaddr: int, timeout: int = 5000, addr_size: int = 8) -> int:
        """
        Read from the memory of an I2C device:

        `data` can be an integer (number of bytes to read) or a buffer to read into
        
        `addr` is the I2C device address
        
        `memaddr` is the memory location within the I2C device
        
        `timeout` is the timeout in milliseconds to wait for the read
        
        `addr_size` selects width of memaddr: 8 or 16 bits
        
        Returns the read data. This is only valid in master mode.
        """
        pass

    def mem_write(self, data: Union[int, bytearray], addr: int, memaddr: int, timeout: int = 5000, addr_size: int = 8) -> None:
        """
        Write to the memory of an I2C device:

        `data` can be an integer or a buffer to write from
        
        `addr` is the I2C device address
        
        `memaddr` is the memory location within the I2C device
        
        `timeout` is the timeout in milliseconds to wait for the write
        
        `addr_size` selects width of memaddr: 8 or 16 bits
        
        Returns `None`. This is only valid in master mode.
        """
        pass

    def recv(self, recv: bytearray, addr: int, timeout: int = 5000) -> bytearray:
        """
        Receive data on the bus:

        `recv` can be an integer, which is the number of bytes to receive, or a mutable buffer, which will be filled with received bytes
        
        `addr` is the address to receive from (only required in master mode)
        
        `timeout` is the timeout in milliseconds to wait for the receive
        
        Return value: if `recv` is an integer then a new buffer of the bytes received, otherwise the same buffer that was passed in to recv.
        """
        pass

    def send(self, send: Union[int, bytearray], addr: int, timeout: int = 5000) -> None:
        """
        Send data on the bus:

        `send` is the data to send (an integer to send, or a buffer object)
        
        `addr` is the address to send to (only required in master mode)
        
        `timeout` is the timeout in milliseconds to wait for the send
        
        Return value: `None`.
        """
        pass

    def scan(self) -> List[int]:
        """
        Scan all I2C addresses from 0x01 to 0x7f and return a list of those that respond. Only valid when in master mode.
        """
        pass

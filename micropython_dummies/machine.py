from pyb import Pin
from typing import Optional


# region Reset related functions

PWRON_RESET: int = None
HARD_RESET: int = None
WDT_RESET: int = None
DEEPSLEEP_RESET: int = None
SOFT_RESET: int = None

def reset():
    """
    Resets the device in a manner similar to pushing the external RESET button.
    """
    pass

def soft_reset():
    """
    Performs a soft reset of the interpreter, deleting all Python objects and resetting the Python heap. It tries to retain the method by which the user is connected to the MicroPython REPL (eg serial, USB, Wifi).
    """
    pass

def reset_cause():
    """
    Get the reset cause
    """
    pass

# endregion

# region Interrupt related functions

IDLE: int = None
SLEEP: int = None
DEEPSLEEP: int = None

def disable_irq():
    """
    Disable interrupt requests. Returns the previous IRQ state which should be considered an opaque value. This return value should be passed to the `enable_irq()` function to restore interrupts to their original state, before `disable_irq()` was called.
    """
    pass

def enable_irq():
    """
    Re-enable interrupt requests. The state parameter should be the value that was returned from the most recent call to the `disable_irq()` function.
    """
    pass

# endregion

# region Power related functions

def freq():
    """
    Returns CPU frequency in hertz.
    """
    pass

def idle():
    """
    Gates the clock to the CPU, useful to reduce power consumption at any time during short or long periods. Peripherals continue working and execution resumes as soon as any interrupt is triggered (on many ports this includes system timer interrupt occurring at regular intervals on the order of millisecond).
    """
    pass

def lightsleep(time_ms: Optional[int] = None):
    """
    Stops execution in an attempt to enter a low power state.

    If `time_ms` is specified then this will be the maximum time in milliseconds that the sleep will last for. Otherwise the sleep can last indefinitely.

    With or without a timout, execution may resume at any time if there are events that require processing. Such events, or wake sources, should be configured before sleeping, like `Pin` change or `RTC` timeout.

    The precise behaviour and power-saving capabilities of lightsleep and deepsleep is highly dependent on the underlying hardware, but the general properties are:

    A lightsleep has full RAM and state retention. Upon wake execution is resumed from the point where the sleep was requested, with all subsystems operational.
    """
    pass

def deepsleep(time_ms: Optional[int] = None):
    """
    Stops execution in an attempt to enter a low power state.

    If `time_ms` is specified then this will be the maximum time in milliseconds that the sleep will last for. Otherwise the sleep can last indefinitely.

    With or without a timout, execution may resume at any time if there are events that require processing. Such events, or wake sources, should be configured before sleeping, like `Pin` change or `RTC` timeout.

    The precise behaviour and power-saving capabilities of lightsleep and deepsleep is highly dependent on the underlying hardware, but the general properties are:

    A deepsleep may not retain RAM or any other state of the system (for example peripherals or network interfaces). Upon wake execution is resumed from the main script, similar to a hard or power-on reset. The `reset_cause()` function will return `machine.DEEPSLEEP` and this can be used to distinguish a deepsleep wake from other resets.
    """
    pass

def wake_reason():
    """
    Get the wake reason.
    """
    pass

# endregion

def time_pulse_us(pin: Pin, pulse_level: int, timeout_us: int = 1000000):
    """
    Time a pulse on the given `pin`, and return the duration of the pulse in microseconds. The `pulse_level` argument should be 0 to time a low pulse or 1 to time a high pulse.

    If the current input value of the `pin` is different to `pulse_level`, the function first (*) waits until the `pin` input becomes equal to `pulse_level`, then (**) times the duration that the `pin` is equal to pulse_level. If the `pin` is already equal to pulse_level then timing starts straight away.

    The function will return -2 if there was timeout waiting for condition marked (*) above, and -1 if there was timeout during the main measurement, marked (**) above. The timeout is the same for both cases and given by `timeout_us` (which is in microseconds).
    """
    pass

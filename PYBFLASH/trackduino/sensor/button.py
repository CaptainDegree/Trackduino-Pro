from pyb import Pin


class TouchSensor:
    def __init__(self, pin: Pin):
        self._pin = Pin(pin, mode=Pin.IN)

    def read(self):
        return self._pin.value()

    def pressed(self):
        return self.read() == 0

    def released(self):
        return self.read() == 1


class BuiltinButton(TouchSensor):
    def __init__(self, pin: Pin):
        super().__init__(pin)
        self._pin = Pin(self._pin, mode=Pin.IN, pull=Pin.PULL_UP)

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(BuiltinButton, cls).__new__(cls)
        return cls.instance


class ButtonLeft(BuiltinButton):
    def __init__(self):
        super().__init__(Pin(Pin.cpu.B13, mode=Pin.IN))


class ButtonRight(BuiltinButton):
    def __init__(self):
        super().__init__(Pin(Pin.cpu.C12, mode=Pin.IN))


class ButtonUp(BuiltinButton):
    def __init__(self):
        super().__init__(Pin(Pin.cpu.C11, mode=Pin.IN))


class ButtonDown(BuiltinButton):
    def __init__(self):
        super().__init__(Pin(Pin.cpu.C10, mode=Pin.IN))


class ButtonCenter(BuiltinButton):
    def __init__(self):
        super().__init__(Pin(Pin.cpu.B12, mode=Pin.IN))

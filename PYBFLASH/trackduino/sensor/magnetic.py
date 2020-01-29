from pyb import Pin


class MagneticFieldSensor:
    def __init__(self, pin: Pin):
        self._pin = pin

    def read(self):
        return self._pin.value()

    def magnetic(self):
        return self.read() == 1

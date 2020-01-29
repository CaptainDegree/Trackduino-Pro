from pyb import Pin


class TiltSensor:
    def __init__(self, pin: Pin):
        self._self = pin

    def read(self):
        return self._pin.value()

    def tilted(self):
        return self.read() == 1

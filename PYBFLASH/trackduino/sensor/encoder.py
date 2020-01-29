from pyb import Pin


class Encoder:
    def __init__(self, pin_a: Pin, pin_b: Pin):
        self._channel_a = pin_a
        self._channel_b = pin_b
        self._data = 0

        self._channel_a.irq(lambda p: self._scan())
        self._channel_b.irq(lambda p: self._scan())
        self._prev_status = self._status()

    def _status(self):
        return self._channel_a.value() + 2 * self._channel_b.value()

    def _scan(self):
        status = self._status()

        print(self._prev_status, status)

        if self._prev_status == 0:
            if status == 2:
                self._data += 1
            elif status == 1:
                self._data -= 1
        elif self._prev_status == 1:
            if status == 0:
                self._data += 1
            elif status == 3:
                self._data -= 1
        elif self._prev_status == 2:
            if status == 3:
                self._data += 1
            elif status == 0:
                self._data -= 1
        elif self._prev_status == 3:
            if status == 1:
                self._data += 1
            elif status == 2:
                self._data -= 1
        
        self._prev_status = status

    def zero(self):
        self._data = 0

    def read(self):
        return self._data * 5 // 2

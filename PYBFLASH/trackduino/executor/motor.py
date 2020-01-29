from pyb import Pin
from trackduino.common import constrain, analog_write_percent
from trackduino.timer_manager import TimerManager


class Motor:
    class Direction:
        FORWARD = 1
        BACKWARD = -1

    def __init__(self):
        self._power = 0
        self._direction = Motor.Direction.FORWARD

        self._IN1 = None
        self._IN2 = None
        self._ENC = None

    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, power):
        self._power = constrain(power, 0, 100)
        analog_write_percent(self._ENC, self._power)

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, direction):
        self._direction = direction

        if direction == Motor.Direction.FORWARD:
            self._IN1.off()
            self._IN2.on()
        elif direction == Motor.Direction.BACKWARD:
            self._IN1.on()
            self._IN2.off()

    def run(self, power=None, direction=None):
        if (power is None):
            power = self._power
        if (direction is None):
            direction = self._direction

        self.direction = direction
        self.power = power

    def stop(self):
        self.power = 0

    def hard_stop(self):
        self._IN1.off()
        self._IN2.off()
        self.power = 100


class M1(Motor):
    def __init__(self):
        super().__init__()
        self._IN1 = Pin(Pin.cpu.E0, mode=Pin.OUT)
        self._IN2 = Pin(Pin.cpu.E6, mode=Pin.OUT)
        self._ENC = Pin(Pin.cpu.D13, mode=Pin.OUT)

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(M1, cls).__new__(cls)
        return cls.instance


class M2(Motor):
    def __init__(self):
        super().__init__()
        self._IN1 = Pin(Pin.cpu.E5, mode=Pin.OUT)
        self._IN2 = Pin(Pin.cpu.B14, mode=Pin.OUT)
        self._ENC = Pin(Pin.cpu.D12, mode=Pin.OUT)

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(M2, cls).__new__(cls)
        return cls.instance


class M3(Motor):
    def __init__(self):
        super().__init__()
        self._IN1 = Pin(Pin.cpu.D7, mode=Pin.OUT)
        self._IN2 = Pin(Pin.cpu.D4, mode=Pin.OUT)
        self._ENC = Pin(Pin.cpu.D14, mode=Pin.OUT)

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(M3, cls).__new__(cls)
        return cls.instance


class M4(Motor):
    def __init__(self):
        super().__init__()
        self._IN1 = Pin(Pin.cpu.D3, mode=Pin.OUT)
        self._IN2 = Pin(Pin.cpu.D2, mode=Pin.OUT)
        self._ENC = Pin(Pin.cpu.D15, mode=Pin.OUT)

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(M4, cls).__new__(cls)
        return cls.instance

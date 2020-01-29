from pyb import Pin, delay
from micropython import const
from trackduino.cds import LightSensor
from trackduino.common import constrain, amap, average


class LightColorSensor:
    class Color:
        BLACK = const(0)
        WHITE = const(1)
        RED = const(2)
        GREEN = const(3)
        BLUE = const(4)
        YELLOW = const(5)
        PURPLE = const(6)
        CYAN = const(7)
        UNKNOWN = const(-1)
    
    def __init__(self, redPin: Pin, greenPin: Pin, bluePin: Pin, cdsPin: Pin):
        self._cds = LightSensor(cdsPin)
        self._colorPins = [Pin(redPin, mode=Pin.OUT),
                           Pin(greenPin, mode=Pin.OUT),
                           Pin(bluePin, mode=Pin.OUT)]

        self._white_sample = [0, 0, 0]
        self._black_sample = [0, 0, 0]

        self._color_near = const(100 // 4)
        self._color_far = const(100 // 2)
        self._upper_threshold = const(100 - 100 // 4)
        self._lower_threshold = const(100 // 4)
        self._delta_black = 8
        self._delta_color = 4

    def _blink(self, times=3):
        for _ in range(times):
            self._colorPins[2].high()
            delay(100)
            self._colorPins[2].low()
            delay(50)

    def _cds_multiple_read(self, times):
        readings = []
        for _ in range(times):
            readings.append(self._cds.read())
            delay(10)

        return average(readings)

    def calibrate(self):
        print("Setting white balance")
        self._blink()
        delay(1500)
        for i in range(3):
            self._colorPins[i].high()
            delay(50)
            self._white_sample[i] = self._cds_multiple_read(5)
            self._colorPins[i].low()
            delay(100)

        delay(1500)

        print("Setting black balance")
        self._blink()
        delay(1500)
        for i in range(3):
            self._colorPins[i].high()
            delay(50)
            self._black_sample[i] = self._cds_multiple_read(5)
            self._colorPins[i].low()
            delay(100)

    def color(self):
        measured_color = [0, 0, 0]
        for i in range(3):
            self._colorPins[i].high()
            delay(10)
            measured_color[i] = self._cds_multiple_read(5)
            measured_color[i] = int(amap(constrain(measured_color[i], self._black_sample[i], self._white_sample[i]), self._black_sample[i], self._white_sample[i], 0, 100))
            self._colorPins[i].low()
            delay(10)

        # WHITE
        if measured_color[0] >= self._upper_threshold and \
            measured_color[1] >= self._upper_threshold and \
            measured_color[2] >= self._upper_threshold and \
            abs(measured_color[0] - measured_color[1]) <= self._color_near and \
            abs(measured_color[0] - measured_color[2]) <= self._color_near and \
            abs(measured_color[1] - measured_color[2]) <= self._color_near:
            return self.Color.WHITE
        # BLACK
        elif measured_color[0] <= self._lower_threshold and \
            measured_color[1] <= self._lower_threshold and \
            measured_color[2] <= self._lower_threshold and \
            abs(measured_color[0] - measured_color[1]) <= self._delta_black and \
            abs(measured_color[0] - measured_color[2]) <= self._delta_black and \
            abs(measured_color[1] - measured_color[2]) <= self._delta_black:
            return self.Color.BLACK
        # RED
        elif measured_color[0] - measured_color[1] >= self._delta_color and \
            measured_color[0] - measured_color[2] >= self._delta_color:
            return self.Color.RED
        # GREEN
        elif measured_color[1] - measured_color[0] >= self._delta_color and \
            measured_color[1] - measured_color[2] >= self._delta_color:
            return self.Color.GREEN
        # BLUE
        elif measured_color[2] - measured_color[0] >= self._delta_color and \
            measured_color[2] - measured_color[1] >= self._delta_color:
            return self.Color.BLUE
        # YELLOW
        elif measured_color[0] - measured_color[2] >= self._color_near and \
            measured_color[1] - measured_color[2] >= self._color_near and \
            abs(measured_color[0] - measured_color[1]) <= self._delta_color:
            return self.Color.YELLOW
        # PURPLE
        elif measured_color[0] - measured_color[1] >= self._color_near and \
            measured_color[2] - measured_color[1] >= self._color_near and \
            abs(measured_color[0] - measured_color[2]) <= self._delta_color:
            return self.Color.PURPLE
        # CYAN
        elif measured_color[1] - measured_color[0] >= self._color_near and \
            measured_color[2] - measured_color[0] >= self._color_near and \
            abs(measured_color[1] - measured_color[2]) <= self._delta_color:
            return self.Color.CYAN
        
        return self.Color.UNKNOWN

    def cds(self):
        return self._cds.read()

    def dark(self, threshold=500):
        return self._cds.read(threshold)

    def light(self, threshold=500):
        return self._cds.read(threshold)

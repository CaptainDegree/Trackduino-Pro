from trackduino.executor.led import BuiltinLED
from pyb import delay


for _ in range(3):
    BuiltinLED().color = BuiltinLED.Color.GREEN
    delay(100)
    BuiltinLED().off()
    delay(100)

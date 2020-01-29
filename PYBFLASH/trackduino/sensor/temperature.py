from micropython import const
from onewire import OneWire


class TemperatureSensor:
    class _Const:
        CONVERT = const(0x44)
        RD_SCRATCH = const(0xbe)
    
    def __init__(self, pin):
        self._onewire = OneWire(pin)
        self._buffer = bytearray(9)
        self._rom = [rom for rom in self._onewire.scan() if rom[0] in (0x10, 0x22, 0x28)][0]
        self._convert_temp()

    def _convert_temp(self):
        self._onewire.reset(True)
        self._onewire.writebyte(self._onewire.SKIP_ROM)
        self._onewire.writebyte(self._Const.CONVERT)

    def _read_scratch(self):
        self._onewire.reset(True)
        self._onewire.select_rom(self._rom)
        self._onewire.writebyte(TemperatureSensor._Const.RD_SCRATCH)
        self._onewire.readinto(self._buffer)
        if self._onewire.crc8(self._buffer):
            raise Exception('Temperature sensor::CRC error')
        
        return self._buffer

    def read(self):
        buffer = self._read_scratch()
        if self._rom[0] == 0x10:
            if self._buffer[1]:
                t = self._buffer[0] >> 1 | 0x80
                t = -((~t + 1) & 0xff)
            else:
                t = self._buffer[0] >> 1
            
            return t - 0.25 + (self._buffer[7] - self._buffer[6]) / self._buffer[7]
        else:
            t = self._buffer[1] << 8 | self._buffer[0]
            if t & 0x8000:
                t = -((t ^ 0xffff) + 1)
            
            return t / 16

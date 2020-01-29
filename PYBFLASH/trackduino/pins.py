from pyb import Pin


class TrackduinoPin:
    class In:
        IN1 = Pin(Pin.cpu.B0, Pin.IN)
        IN2 = Pin(Pin.cpu.B1, Pin.IN)
        IN3 = Pin(Pin.cpu.C0, Pin.IN)
        IN4 = Pin(Pin.cpu.C1, Pin.IN)
        IN5 = Pin(Pin.cpu.C2, Pin.IN)
        IN6 = Pin(Pin.cpu.C3, Pin.IN)
        IN7 = Pin(Pin.cpu.C4, Pin.IN)
        IN8 = Pin(Pin.cpu.C5, Pin.IN)

    class Out:
        OUT1 = Pin(Pin.cpu.B5, Pin.OUT)
        OUT2 = Pin(Pin.cpu.C8, Pin.OUT)
        OUT3 = Pin(Pin.cpu.C9, Pin.OUT)
        OUT4 = Pin(Pin.cpu.B11, Pin.OUT)
        OUT5 = Pin(Pin.cpu.B15, Pin.OUT)
        OUT6 = Pin(Pin.cpu.D10, Pin.OUT)
        OUT7 = Pin(Pin.cpu.E14, Pin.OUT)
        OUT8 = Pin(Pin.cpu.E13, Pin.OUT)

        class PWM:
            OUT1 = Pin(Pin.cpu.B5, Pin.OUT)
            OUT2 = Pin(Pin.cpu.C8, Pin.OUT)
            OUT3 = Pin(Pin.cpu.C9, Pin.OUT)
            OUT4 = Pin(Pin.cpu.B11, Pin.OUT)
            OUT5 = Pin(Pin.cpu.B15, Pin.OUT)

    class Analog:
        A0 = Pin(Pin.cpu.A0)
        A1 = Pin(Pin.cpu.A1)
        A2 = Pin(Pin.cpu.A2)
        A3 = Pin(Pin.cpu.A3)
        A4 = Pin(Pin.cpu.A4)
        A5 = Pin(Pin.cpu.A5)

    class Digital:
        D2 = Pin(Pin.cpu.A13)
        D3 = Pin(Pin.cpu.B10)
        D4 = Pin(Pin.cpu.E11)
        D5 = Pin(Pin.cpu.B4)
        D6 = Pin(Pin.cpu.A15)
        D7 = Pin(Pin.cpu.E10)
        D8 = Pin(Pin.cpu.E9)
        D9 = Pin(Pin.cpu.E4)
        D10 = Pin(Pin.cpu.E3)
        D11 = Pin(Pin.cpu.E2)
        D12 = Pin(Pin.cpu.E8)
        D13 = Pin(Pin.cpu.E7)

        class PWM:
            D3 = Pin(Pin.cpu.B10)
            D5 = Pin(Pin.cpu.B4)
            D6 = Pin(Pin.cpu.A15)
            D9 = Pin(Pin.cpu.E4)
            D11 = Pin(Pin.cpu.E2)

    class Motor:
        M1_ENC = Pin(Pin.cpu.D13, mode=Pin.OUT)
        M2_ENC = Pin(Pin.cpu.D12, mode=Pin.OUT)
        M3_ENC = Pin(Pin.cpu.D14, mode=Pin.OUT)
        M4_ENC = Pin(Pin.cpu.D15, mode=Pin.OUT)

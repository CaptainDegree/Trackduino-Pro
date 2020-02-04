class ADC(object):
    def __init__(self):
        pass


class Pin(object):
    class cpu(object):
        # region A
        A0 = None
        A1 = None
        A2 = None
        A3 = None
        A4 = None
        A5 = None
        A6 = None
        A7 = None
        A8 = None
        A9 = None
        A10 = None
        A11 = None
        A12 = None
        A13 = None
        A14 = None
        A15 = None
        # endregion
        # region B
        B0 = None
        B1 = None
        B2 = None
        B3 = None
        B4 = None
        B5 = None
        B6 = None
        B7 = None
        B8 = None
        B9 = None
        B10 = None
        B11 = None
        B12 = None
        B13 = None
        B14 = None
        B15 = None
        # endregion
        # region C
        C0 = None
        C1 = None
        C2 = None
        C3 = None
        C4 = None
        C5 = None
        C6 = None
        C7 = None
        C8 = None
        C9 = None
        C10 = None
        C11 = None
        C12 = None
        C13 = None
        C14 = None
        C15 = None
        # endregion
        # region D
        D0 = None
        D1 = None
        D2 = None
        D3 = None
        D4 = None
        D5 = None
        D6 = None
        D7 = None
        D8 = None
        D9 = None
        D10 = None
        D11 = None
        D12 = None
        D13 = None
        D14 = None
        D15 = None
        # endregion
        # region E
        E0 = None
        E1 = None
        E2 = None
        E3 = None
        E4 = None
        E5 = None
        E6 = None
        E7 = None
        E8 = None
        E9 = None
        E10 = None
        E11 = None
        E12 = None
        E13 = None
        E14 = None
        E15 = None
        # endregion

    IN = None
    OUT = None
    OUT_PP = None
    OUT_OD = None
    AF_PP = None
    AF_OD = None
    ANALOG = None
    PULL_NONE = None
    PULL_UP = None
    PULL_DOWN = None

    def __init__(self, id, mode=Pin.IN, pull=PULL_NONE):
        pass

    def value(self, value=None):
    	pass


def delay(time_ms):
    pass

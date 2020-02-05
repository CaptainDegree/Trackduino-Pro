def const(expr: int):
    """
    Used to declare that the expression is a constant so that the compile can optimise it.

    Constants declared this way are still accessible as global variables from outside the module they are declared in. On the other hand, if a constant begins with an underscore then it is hidden, it is not available as a global variable, and does not take up any memory during execution.

    This const function is recognised directly by the MicroPython parser and is provided as part of the micropython module mainly so that scripts can be written which run under both CPython and MicroPython, by following the above pattern.
    """
    pass

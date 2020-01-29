# This script runs on boot-up
# It can run arbitrary Python, but best to keep it minimal

import machine
import pyb


pyb.main('main.py')

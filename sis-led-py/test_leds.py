"""
Cycle through the outputs enabling one by one
"""
import time

from led import gpio

while True:
    for i in range(144):
        gpio.outputValue(1 << i)
        time.sleep(0.2)

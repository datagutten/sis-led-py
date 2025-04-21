# https://forums.raspberrypi.com/viewtopic.php?p=828976&sid=d1cb3d39607530fb59d8b081e13d8e3d#p828976


from RPi import GPIO

GPIO.setmode(GPIO.BOARD)

data_pin = 37  # 19
latch_pin = 38  # 22
clock_pin = 40  # 23

GPIO.setup(data_pin, GPIO.OUT)
GPIO.setup(clock_pin, GPIO.OUT)
GPIO.setup(latch_pin, GPIO.OUT)


def pulsePin(pin):
    # Pulse a pin high then low
    # the latch and the clock pins
    # need this to load in and output data
    GPIO.output(pin, 1)
    GPIO.output(pin, 0)


def latch():
    GPIO.output(latch_pin, 1)


def unlatch():
    GPIO.output(latch_pin, 0)


def output_bit(bit: int):
    """
    Output a bit on the data pin and pulse the clock pin
    :param bit:
    :return:
    """
    GPIO.output(data_pin, bit)
    pulsePin(clock_pin)


def outputValue(value, unlatch=True):
    # Convert a decimal value to a binary one
    # then load that onto the shift register, one bit at a time
    # by setting the datapin high for 1, low for zero
    # Pulse the clock pin until all 16 bits have been loaded
    # on to the shift register
    # then pulse the latch pin to output the data
    GPIO.output(latch_pin, 1)
    if unlatch:
        sbin = "{0:0144b}".format(value)
    else:
        sbin = "{0:035b}".format(value)
    print("binary for %s is %s " % (value, sbin))
    # step through one bit at a time
    for bit in sbin:
        # print("bit  == ", bit)
        if bit == "0":
            GPIO.output(data_pin, 1)
        else:
            GPIO.output(data_pin, 0)
        pulsePin(clock_pin)
    # all bits loaded, now output them
    # pulsePin(latch_pin)
    if unlatch:
        GPIO.output(latch_pin, 0)

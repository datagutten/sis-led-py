import os.path

from . import gpio

from PIL import Image

cols = 5
rows = 7
display_offset = {
    1: 72,  # 70 and 71 is not used
    2: 107,
    3: 0,
    4: 35
}
display_order = [3, 4, 1, 2]
display_count = 4

letters_folder = os.path.join(os.path.dirname(__file__), 'letters')


def display_start(display: int):
    """
    Get the start position for the given display
    """
    return display_offset[display]


def pixels():
    mappings = {}

    for row in range(rows):
        pos = row
        for col in range(cols):
            mappings[pos] = col, row
            pos += rows

    return mappings


def image_to_byte(image_file: str, offset=0):
    """
    Convert a bitmap image file to a byte array
    :param image_file: Image file path
    :param offset:
    :return:
    """
    with Image.open(image_file) as im:
        if im.mode != '1':
            raise RuntimeError('Image must be in binary mode')
        byte = 0
        for led, pix in pixels().items():
            color = im.getpixel(pix)
            if not bool(color):
                byte = byte | (1 << led + offset)

        return byte


def letter_to_byte(letter, offset=0):
    file = os.path.join(letters_folder, str(letter) + '.bmp')
    return image_to_byte(file, offset)


def show_text(value, display=1, adjust_right=False):
    if adjust_right:
        value = reversed(str(value))
        if not display:
            display = display_count
    else:
        value = str(value)

    byte = 0
    for char in value:
        byte_digit = letter_to_byte(char, display_start(display))
        byte = byte | byte_digit
        if adjust_right:
            display -= 1
        else:
            display += 1

    return gpio.outputValue(byte)

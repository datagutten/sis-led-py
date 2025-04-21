"""
Output a bitmap letter as ASCII art
"""
import sys

from led import graphic

pos = 0
offset = 0


def bitmap_ascii(character):
    value = graphic.letter_to_byte(character)

    sbin = "{0:035b}".format(value)[::-1]

    print()
    for row in range(graphic.rows):
        pos = row + offset
        if row == 0:
            print('  ', end='')
            for key in range(graphic.cols):
                print(key, end='')
            print()

        for col in range(graphic.cols):
            if col == 0:
                print(row, end=' ')

            if sbin[pos] == '1':
                print('x', end='')
            else:
                print(' ', end='')

            pos += graphic.rows
        print()


bitmap_ascii(sys.argv[1])

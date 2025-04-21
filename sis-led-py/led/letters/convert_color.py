import sys

import PIL.Image

with PIL.Image.open(sys.argv[1]) as im:
    if im.mode != '1':
        print('Im mode is %s convert to 1' % im.mode)
        im.convert("1").save(sys.argv[1])
    else:
        print('Im mode is already 1')

    pass

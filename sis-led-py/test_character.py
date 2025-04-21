"""
Output one or more bitmap characters
"""
import sys

from led import graphic

if len(sys.argv) > 2:
    start_display = int(sys.argv[2])
else:
    start_display = 1

graphic.show_text(sys.argv[1], start_display)

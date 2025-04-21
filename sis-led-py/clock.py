import time
from datetime import datetime

from led import graphic

while True:
    now = datetime.now()
    text = now.strftime("%H%M")
    graphic.show_text(text)
    time.sleep(1)

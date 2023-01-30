import os
import time


while True:
    os.system('clear')
    print('\n', os.popen('xdotool getactivewindow getwindowname').read(), end='')
    time.sleep(1)

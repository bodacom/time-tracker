import os
import time



first = True
while True:
    if first:
        print()
        first = False
    print(os.popen('xdotool getactivewindow getwindowname').read(), end='')
    time.sleep(1)
    print('\033[1A', end='\x1b[2K')

import time
import os
import re
import sys
from datetime import datetime

# getwindowfocus == getactivewindow
# 'xdotool getwindowfocus getwindowname getactivewindow getmouselocation'

xdo_command = 'xdotool getactivewindow getwindowname getmouselocation '
data = ''
file_name = 'tracker_log.txt'

# for i in range(10):
while True:

    xdo = os.popen(xdo_command).read()
    now = datetime.now().time()
    time_ = time.time()
    # print(xdo_command, xdo, now, sep='\n', end='\n\n')
    data = data + str(time_)+ '\n' + xdo + '\n'
    
    try:
        with open(file_name, 'a') as data_file:
            data_file.write(str(time_) + '\n' + xdo + '\n')
        data = ''
    except:
        print('Eror writing to file. Data will be collected in buffer and written while write operation will be available.')

    time.sleep(1)

# try-except for os.popen().read()
# context manager for data saving to save the buffer in case of script fault

import time
import os
import re
import sys
from datetime import datetime



def save_to_file(file: str, data: str):
    try:
        with open(file, 'a') as data_file:
            data_file.write(data)
        return True
    except:
        print('Eror writing to file. Data will be collected in buffer and written while write operation will be available.')
        return False


def track():

    # getwindowfocus == getactivewindow
    # 'xdotool getwindowfocus getwindowname getactivewindow getmouselocation'

    XDO_COMMANDS = ['xdotool', 'getactivewindow', 'getwindowname', 'getmouselocation',]
    XDO_COMMAND = ' '.join(XDO_COMMANDS)
    print(XDO_COMMAND)
    data = ''
    FILE_NAME = 'tracker_log_1.txt'
    MEASUREMENT_ACCURACY = 2 # measurement accuracy in seconds
    measurement_delay = MEASUREMENT_ACCURACY / 2

    while True:

        activity_details = os.popen(XDO_COMMAND).read()
        time_stamp = time.time()

        activity_frame = f'{str(time_stamp)}\n{activity_details}\n'
        
        data = data + activity_frame
        
        if save_to_file(FILE_NAME, data):
            data = ''

        time.sleep(measurement_delay)


def light_tracker():
    
    XDO_COMMANDS = ['xdotool', 'getactivewindow', 'getwindowname', 'getmouselocation',]
    XDO_COMMAND = ' '.join(XDO_COMMANDS)
    
    activity_details = os.popen(XDO_COMMAND).read()
    time_stamp = time.time()

    return time_stamp, activity_details



if __name__ == '__main__':
    track()

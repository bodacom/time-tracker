import analyzer
import time

def check_log(log_file_name: str = 'tracker_log.txt') -> list:
    '''
    Checks through all the file lines.
    Returns nothing so far.
    
    File format.
    One entity consists of three lines like the next:

     "1665761850.8328192                            (contains unix time stamp)
      main.py - beetroot - Visual Studio Code       (contains the window and the task name)
      x:1191 y:1051 screen:0 window:115343363"      (contains coursore coordinates x and y, screen number, window id)
                                                    (contains empty line as an entity separator)
      -- // --
    '''
    
    with open(log_file_name, 'r') as log_file:
        previous_line = str()
        last_line =str()
        for line in log_file:
            previous_line = last_line
            last_line = line 
            if line == "afdsgnsdfhsd\n":
                print('Here we are')
        print(previous_line)


def seek_log(log_file_name: str = 'tracker_log.txt') -> list:
    '''
    Seek to the end of file and back to already tracked lines.
    Returns nothing so far.
    
    File format.
    One entity consists of three lines like the next:

     "1665761850.8328192                            (contains unix time stamp)
      main.py - beetroot - Visual Studio Code       (contains the window and the task name)
      x:1191 y:1051 screen:0 window:115343363"      (contains coursore coordinates x and y, screen number, window id)
                                                    (contains empty line as an entity separator)
      -- // --
    '''
    
    with open(log_file_name, 'r') as log_file:
        
        log_file.seek(0,2)
        print(type(log_file.tell()), log_file.tell())
        # for i in range(100):
        #     letter = log_file.read(1)
        #     log_file.seek(-2,1)
        #     print(letter, sep='', end='')


def read_all_file(repeat_times, sleep_time):
    for i in range(repeat_times):
        start_time = time.time()
        file_content = analyzer.read_log("/home/bohdan/tracker_log.txt")
        finish_time = time.time()

        lines_start_time = time.time()
        for number, _ in enumerate(file_content):
            pass

        lines_finish_time = time.time()

        print('Read time = ', finish_time - start_time)
        print('Number of lines = ', number)

        print('Lines enumerating time = ', lines_finish_time - lines_start_time)
        print('Number of lines = ', number)

        time.sleep(sleep_time)


def check_through_file(repeat_times, sleep_time):
    for i in range(repeat_times):
        start_time = time.time()
        check_log("/home/bohdan/tracker_log.txt")
        finish_time = time.time()

        print('Read time = ', finish_time - start_time)
        #print('Number of lines = ', lines_quantity)

        time.sleep(sleep_time)


def seek_file(repeat_times, sleep_time):
    for i in range(repeat_times):
        start_time = time.time()
        seek_log("/home/bohdan/tracker_log.txt")
        finish_time = time.time()

        print('Read time = ', finish_time - start_time)
        #print('Number of lines = ', lines_quantity)

        time.sleep(sleep_time)

if __name__ == '__main__':

    # read_all_file(1,0)

    seek_file(3,1)


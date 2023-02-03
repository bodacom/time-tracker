
# Розбирати записи на складові
# Словник із групуванням на:
#     проекти (задачі, ще щось)
#     програми
#     назви файлів
#     час використання: кожна секунда в трекінгу відповідає секунді використання.
#     час простою: не вважати використанням, якщо немає активності миші більше хх секунд?

import time
import datetime
import matplotlib.pyplot as plt 



def read_log(log_file_name: str = '/home/bohdan/tracker_log.txt') -> list:
    '''
    Reads all the file content.
    Returns list containing lines.
    
    File format.
    One entity consists of three lines like the next:

     "1665761850.8328192                            (contains unix time stamp)
      main.py - beetroot - Visual Studio Code       (contains the window and the task name)
      x:1191 y:1051 screen:0 window:115343363"      (contains coursore coordinates x and y, screen number, window id)
                                                    (contains empty line as an entity separator)
      -- // --
    '''
    
    with open(log_file_name, 'r') as log_file:
        log_dump = log_file.readlines()
    
    return log_dump


def make_entities(log_dump: list) -> list:
    '''
    Makes entities from list containing raw log_dump strings.
    Returns list with entities of list type.
    
    ['1665761850.8328192',
     'main.py - beetroot - Visual Studio Code',
     'x:1191 y:1051 screen:0 window:115343363', ...]
    
    becomes

    [['1665761850.8328192', 'main.py - beetroot - Visual Studio Code', 'x:1191 y:1051 screen:0 window:115343363'], ...]
    
    '''
    log_entities = []
    entity = []
    
    for line in log_dump:
        # if line_counter == 4:
        #     log_entities.append(entity)
        #     entity = []
        #     line_counter = 1
        # else:
        #     entity.append(line.rstrip())
        #     line_counter += 1
        try:
            float(line)
            if len(entity) !=0:
                log_entities.append(entity)
                entity = []
            entity.append(line.rstrip())
        except:
            entity.append(line.rstrip())

    del entity
    
    return log_entities


def unique_names(log_entities: list) -> list:
    '''
    Defines unique names of loged windows among the entities.
    Returns a list with unique names as strings.
    '''
    entities_names = []
    for entity in log_entities:
        entities_names.append(entity[1])
        
    uniq_names = list(set(entities_names))
    print('Number of unique names: ',len(uniq_names))

    return uniq_names


def sorted_frequency_dictionary(entities: list, reversed: bool = True) -> dict:
    '''
    Sorts names by times of appearance.
    Returns a dictionary of unique names as keys and frequency as values
    
    '''
    frequency_dictionary = {}
    # define names frequency:
    for entity in entities:
        if frequency_dictionary.get(entity[1]):
            frequency_dictionary[entity[1]] += 1
        else:
            frequency_dictionary[entity[1]] = 1

    frequency_dictionary = {k: v for k, v in sorted(frequency_dictionary.items(), key=lambda item: item[1], reverse=reversed)}

    return frequency_dictionary


def task_total_time(frequency_dictionary: dict, key_word: str) -> int:
    '''

    Returns total number of entities containing "key_word" from a frequency dictionary.

    '''
    total_time = 0
    key_time = 0
    for key, value in frequency_dictionary.items():
        total_time += value
        if key_word in key:
            key_time += value
        
    return key_time, total_time


def logged_intervals(entities: list, gap: float) -> list:
    '''
    Finds and returns the intervals with the gap more than 'gap' seconds
    
    '''
    intervals = []
    interval = []
        
    for index, entity in enumerate(entities):
        if index == len(entities) -1:
            if len(interval) == 0:
                interval.extend([float(entity[0]) for i in range(2)])
            else:
                interval.append(float(entity[0]))
            intervals.append(tuple(interval))
        elif index == 0:
            previous_time = float(entity[0])
            interval.append(previous_time)
        else:
            current_time = float(entity[0])
            if current_time - previous_time < gap + 1:
                previous_time = current_time
            else:
                interval.append(previous_time)
                intervals.append(tuple(interval))
                interval = []
                interval.append(current_time)
                previous_time = current_time

    intervals = tuple(intervals)
    return intervals


def get_mouse_location(entity: str) -> int:
    temp_string = entity[-2].replace(' ', ':')
    temp_list = temp_string.split(':')
    x = temp_list[1]
    y = temp_list[3]
    location = int(x + y)

    return location


def active_logged_intervals(entities: list, gap: float, sleep: float) -> list:
    '''
    Finds and returns the active intervals with the sleep time no more than 'sleep' seconds
    
    '''
    intervals = []
    interval = []
    sleep_counter = 0
    for index, entity in enumerate(entities):
        if index == len(entities) -1:
            if len(interval) == 0:
                interval.extend([float(entity[0]) for i in range(2)])
            else:
                interval.append(float(entity[0]))
            intervals.append(tuple(interval))
        elif index == 0:
            previous_time = float(entity[0])
            previous_mouse_location = get_mouse_location(entity)
            interval.append(previous_time)
        else:
            
            current_mouse_location = get_mouse_location(entity)
            if current_mouse_location == previous_mouse_location:
                sleep_counter += 1
                print(sleep_counter)
            else:
                sleep_counter = 0
                previous_mouse_location = current_mouse_location
            
            current_time = float(entity[0])
            if current_time - previous_time < gap + 1 and sleep_counter < sleep:
                previous_time = current_time
            elif current_time - previous_time > gap + 1 or sleep_counter >= sleep:
                previous_time = current_time
                if not hold:
                    interval.append(previous_time)
                    intervals.append(tuple(interval))
                    interval = []
                    interval.append(current_time)
                    previous_time = current_time
                    sleep_counter = 0
                    hold = True
            else:
                interval.append(previous_time)
                intervals.append(tuple(interval))
                interval = []
                interval.append(current_time)
                previous_time = current_time
                sleep_counter = 0

    intervals = tuple(intervals)
    return intervals

if __name__ == '__main__':

    file_name = input('Enter log file name: (empty=default) ')
    lines = read_log()
    
    log_entities = make_entities(lines)
    print('Number of log entities:',len(log_entities))
    del(lines)

    frequency_dictionary = sorted_frequency_dictionary(log_entities, True)
    # del(log_entities)

    for entity in log_entities:
        # if entity[1] == '':
        #     print(datetime.datetime.utcfromtimestamp(float(entity[0])).strftime('%Y-%m-%d %H:%M:%S'))
        try:
            float(entity[0])
            if entity[1] == '':
                print(datetime.datetime.utcfromtimestamp(float(entity[0])).strftime('%Y-%m-%d %H:%M:%S'))
        except Exception:
            print(entity)

    total = sum(frequency_dictionary.values())
    i = 0
    names = []
    times = []
    for name, value in frequency_dictionary.items():
        # print(str(datetime.timedelta(seconds = value)), key)
        # total += value
        if i < 10:
            names.append(name)
            times.append(value)
        else:
            break
        i += 1

    plt.pie(times, labels=names, startangle=240)
    plt.show()

    #print(str(datetime.timedelta(seconds = telegram_time)), 'Total telegram time')
    #print(str(datetime.timedelta(seconds = mozilla_time)), 'Total mozilla time')
    
    print('Total time: ',str(datetime.timedelta(seconds = total)))
    print('Tracking started: ', time.ctime(float(log_entities[0][0])))
    print('Last entity: ', time.ctime(float(log_entities[-1][0])))

    intervals = logged_intervals(log_entities, 4)
    # print(len(intervals))
    for index, interval in enumerate(intervals):
        if index < 9:
            index = ' ' + str(index + 1)
        else:
            index = str(index + 1)
        print(index, time.strftime(' %d %H:%M  -  ',time.localtime(interval[0])),\
              time.strftime('%d %H:%M : ',time.localtime(interval[1])),\
              str(datetime.timedelta(seconds = interval[1] - interval[0])))


    # print(type(log_lines))
    # print(type(log_lines[0]))
    # print(log_lines[0])

    # for index in range(10):
    #     print(log_lines[index])

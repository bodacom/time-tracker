import os
import time

counter = 1
hours = 0
minutes = 0
seconds = 0
previous_activity = ''
session_activities = {}
first_time = True

while True:
    os.system('clear')
    activity_name = os.popen('xdotool getactivewindow getwindowname').read().rstrip()
    if first_time:
        previous_activity = activity_name
    if activity_name == previous_activity:
        counter += 1
        seconds = counter % 60
        minutes = counter // 60
        hours = minutes // 60
        minutes = minutes % 60
    else:
        if session_activities.get(previous_activity):
            activity_time = session_activities[previous_activity]
            activity_time += counter
            session_activities[previous_activity] = activity_time
        else:
            session_activities[previous_activity] = counter
        counter = 1
        seconds = 1
        minutes = 0
        hours = 0
    if not first_time:
        print('\n', f'{hours:02}:{minutes:02}:{seconds:02}  ', activity_name, end='\n\n')

        i = 0
        a = dict(sorted(session_activities.items(), key=lambda item: item[1], reverse=True))
        for activity, activity_time in a.items():
            seconds = activity_time % 60
            minutes = activity_time // 60
            hours = minutes // 60
            minutes = minutes % 60
            print(f' {hours:02}:{minutes:02}:{seconds:02}  ', activity)
            i += 1
            if i == 9:
                break
        i = 0
    else:
        first_time = False
    time.sleep(1)
    previous_activity = activity_name
    
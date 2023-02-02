import os
import time
import tkinter as tk
import json
import tracker
import random



def main():

    counter = 0
    hours = 0
    minutes = 0
    seconds = 0
    previous_activity = ''
    session_activities = {}
    first_time = True
    text_to_print = '00:00:00'
    text_display = canvas.create_text(20, 20, text=text_to_print, font=('Helvetica',14),\
                           fill='green',state='normal', anchor=tk.NW)
    list_to_display = ''
    list_display = None

    autosave_time = 10
    autosave_timer = 0
    total_time = 0

    while True:
        
        os.system('clear')
        activity_name = os.popen('xdotool getactivewindow getwindowname').read().rstrip()

        if first_time:
            previous_activity = activity_name

        if activity_name == previous_activity:
            # counter += 1
            # seconds = counter % 60
            # minutes = counter // 60
            # hours = minutes // 60
            # minutes = minutes % 60
            if session_activities.get(previous_activity):
                activity_time = session_activities[previous_activity]
                activity_time += 1
                session_activities[previous_activity] = activity_time
            else:
                session_activities[previous_activity] = 1

        else:
            
            counter = 1
            seconds = 1
            minutes = 0
            hours = 0

            if session_activities.get(activity_name):
                activity_time = session_activities[activity_name]
                activity_time += 1
                session_activities[activity_name] = activity_time
            else:
                session_activities[activity_name] = 1
        activity_time = session_activities[activity_name]
        seconds = activity_time % 60
        minutes = activity_time // 60
        hours = minutes // 60
        minutes = minutes % 60
        text_to_print = f'{hours:02}:{minutes:02}:{seconds:02}   {activity_name}'
        print('\n', text_to_print, end='\n')
        canvas.itemconfig(text_display, state='hidden')
        del(text_display)
        text_display = canvas.create_text(20, 20, text=text_to_print, font=('Helvetica',14),\
                        fill='green',state='normal', anchor=tk.NW)

        i = 0
        session_activities = dict(sorted(session_activities.items(), key=lambda item: item[1], reverse=True))
        list_to_display = ''
        
        for activity, activity_time in session_activities.items():
            seconds = activity_time % 60
            minutes = activity_time // 60
            hours = minutes // 60
            minutes = minutes % 60
            if not activity == 'Total time':
                total_time += activity_time
                list_to_display = list_to_display + f'{hours:02}:{minutes:02}:{seconds:02}   {activity}\n'
            i += 1
            # if i == 10:
            #     break
        print('\n', list_to_display, end='\n\n')
        canvas.itemconfig(list_display, state='hidden')
        del(list_display)
        list_display = canvas.create_text(20, 60, text=list_to_display, font=('Helvetica',13),\
                                          fill='gray',state='normal', anchor=tk.NW)
        session_activities['Total time'] = total_time
        total_time = 0
        
        if first_time:
            first_time = False
            autosave_file_name = f'widget_log_{random.randint(1000, 9999)}.txt'
        for _ in range(19):
            window.update()
            time.sleep(0.05)
        previous_activity = activity_name

        if autosave_timer == autosave_time:
            tracker.save_to_file(autosave_file_name, json.dumps(session_activities, indent=4), 'w')
            autosave_timer = 0
        else:
            autosave_timer += 1
    

if __name__ == '__main__':

    window = tk.Tk()
    window.title("Tracker widget")
    window.resizable(1, 1)
    window.wm_attributes("-topmost",1)
    canvas = tk.Canvas(window, width=700, height=400, bd=0, highlightthickness=1)
    canvas.pack()
    window.update()

    main()

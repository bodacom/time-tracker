import os
import time
import tkinter as tk



def main():

    counter = 1
    hours = 0
    minutes = 0
    seconds = 0
    previous_activity = ''
    session_activities = {}
    first_time = True
    text_to_print = ''
    text_display = canvas.create_text(20, 20, text=text_to_print, font=('Helvetica',14),\
                           fill='green',state='hidden', anchor=tk.NW)

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
            text_to_print = f'{hours:02}:{minutes:02}:{seconds:02}   {activity_name}'
            print('\n', text_to_print, end='\n\n')
            canvas.itemconfig(text_display, state='hidden')
            del(text_display)
            text_display = canvas.create_text(20, 20, text=text_to_print, font=('Helvetica',14),\
                           fill='green',state='normal', anchor=tk.NW)

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
        for i in range(20):
            window.update()
            time.sleep(0.05)
        previous_activity = activity_name
    

if __name__ == '__main__':

    window = tk.Tk()
    window.title("Tracker widget")
    window.resizable(1, 1)
    window.wm_attributes("-topmost",1)
    canvas = tk.Canvas(window, width=700, height=200, bd=0, highlightthickness=0)
    canvas.pack()
    window.update()

    main()

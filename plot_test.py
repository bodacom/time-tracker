import matplotlib.pyplot as plt 
import numpy as np
import json

file_name = input('Enter file name:')

with open('widget_log_6888.txt', 'r') as widget:
    try:
        data = widget.read()
        data = json.loads(data)
    except json.JSONDecodeError:
        data = {}

names = []
times = []
total_time = data['Total time']
others_time = total_time

for name, time in data.items():
    if not name == "Total time":
        names.append(name)
        times.append(time)

names_to_display = names[0:5]
names_to_display.append(f'Other {str(len(data.keys())-6)}')
times_to_display = times[0:5]

for index, time in enumerate(times):
    if index < 5:
        others_time -= time

times_to_display.append(others_time)
fractions = []
for time in times_to_display:
    fraction = round((time * 100) / total_time)
    fractions.append(fraction)

for index, name in enumerate(names_to_display):
    names_to_display[index] = name +': ' + str(fractions[index]) + '%'


exp = [0, 0, 0, 0, 0, 0,]
names = names[1:]
times = times[1:]
plt.pie(times_to_display, labels=names_to_display, explode=exp, startangle=255)
plt.show()
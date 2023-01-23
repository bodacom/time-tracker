# Трекати та відмічати, скільки боксів-помадорів пройдено, 
# скільки залишилося, скільки запланованих справ ще належить зробити за день.
# Отже, запускаємо 25 хвилинний інтервал, чи будь-який інший, і рахуємо час.
# Як тільки час пройдено - відмічається проходження одного блоку. Плануємо інший блок.
# функції паузи, відновлення, повної зупанки
#
# ANSI Escape sequences
# Colorama


import time
import sys
import keyboard


# chars = 'ABCDEFGH'
# loop = range(1, len(chars) + 1)

# LINE_CLEAR = '\x1b[2K' # <-- ANSI sequence

# for idx in loop:
#     print(chars[:idx], end='\r')
#     time.sleep(.5)

# print(end=LINE_CLEAR) # <-- clear the line where cursor is located
# print('done')

LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'

sec = input('Back counter: ')
sec = sec.split(':')
t = 0
for i in range(2,len(sec)+1):
    t = int(sec[-i]) * 60 * (i -1)
sec = int(sec[-1]) + t
time_buffer = time.time()
start_time = time_buffer
print(f'{sec//60:02d}:{sec%60:02d}')
while sec > 0:
    time.sleep(0.05)
    if time.time() >= time_buffer + 1:
        time_buffer += 1
        sec -= 1
        print(LINE_UP, end=LINE_CLEAR)
        print(f'{sec//60:02d}:{sec%60:02d}')
print(time.time() - start_time)
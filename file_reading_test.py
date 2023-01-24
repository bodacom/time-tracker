import analyzer
import time


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


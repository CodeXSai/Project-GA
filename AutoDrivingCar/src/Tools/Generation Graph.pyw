#Hide the python terminals
import win32gui, win32con
The_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(The_program_to_hide , win32con.SW_HIDE)
#######################################

import os
import datetime
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')
fig = plt.figure()


def animate(i):
    xs = []
    ys = []

    plt.clf()
    plt.xlabel('Generation')
    plt.ylabel('Average Fitness')
    graph_data = open(os.getcwd() + '\GenerationInput.txt', 'r')

    for line in graph_data.readlines():
        if len(line) > 1:
            line = line.strip()
            x, y= line.split(',')
            xs.insert(len(xs), date_time(x))
            ys.insert(len(ys), int(y))
    plt.plot(ys, xs, linewidth=1)


def date_time(date):
    return datetime.datetime.strptime(date, "%H:%M:%S.%f")

animate(1)
plt.show()




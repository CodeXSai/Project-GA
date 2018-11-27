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
    zs = []
    xss = []
    yss = []
    zss = []
    l = []
    lss = []

    plt.clf()
    plt.setp(plt.gca().get_xticklabels(), rotation=90, horizontalalignment='right')
    plt.xlabel('Time')
    plt.ylabel('Speed')
    graph_data = open(os.getcwd() + '\GraphInput.txt', 'r')

    for line in graph_data.readlines():
        if len(line) > 1:
            line = line.strip()
            x, y, z, a = line.split(',')
            xs.insert(len(xs), date_time(x))
            ys.insert(len(ys), float(y))
            zs.insert(len(zs), z)
            l.insert(len(l), int(a))

    r = len(l)
    i = 0
    while r > 0:
        xss.insert(len(xss), [])
        yss.insert(len(yss), [])
        zss.insert(len(zss), [])
        lss.insert(len(lss), [])
        one = l[0]
        j = 0
        r1 = r
        while r1 > 0:
            if one == l[j]:
                xss[i].insert(len(xss[i]), xs[j])
                yss[i].insert(len(yss[i]), ys[j])
                zss[i].insert(len(zss[i]), zs[j])
                lss[i].insert(len(lss[i]), l[j])
                del xs[j], ys[j], zs[j], l[j]
            else:
                j += 1
            r1 -= 1
        i += 1
        r = len(l)

    for i in range(len(xss)):
        for j in range(len(xss[i])):
            plt.plot_date(xss[i][j], yss[i][j], linewidth=2, color=zss[i][j])
        plt.plot(xss[i], yss[i], linewidth=1)
        plt.annotate(str(lss[i][0]), xy=(xss[i][-1], yss[i][-1]), xytext=(5,0), textcoords='offset points', va='center')

def date_time(date):
    return datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()




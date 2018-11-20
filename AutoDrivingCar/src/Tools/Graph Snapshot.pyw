import datetime
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')
fig = plt.figure()


def animate(a, b):
    try:
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
        graph_data = open('E:\Projects\Project-GA\AutoDrivingCar\src\Tools\GraphInput.txt', 'r')

        if b.lower() != "Now".lower() and a.lower() != "Start".lower() and b.lower() != "End".lower():
            if date_time(a) > date_time(b):
                print("\n Error: From is grater than To\n")
                raise Exception
            elif date_time(a) == date_time(b):
                print("\n Error: From and To are same\n")
                raise Exception

        for line in graph_data.readlines():
            if len(line) > 1:
                line = line.strip()
                x, y, z, li = line.split(',')

                if b.lower() == "Now".lower():
                    xs.insert(len(xs), date_time(x))
                    ys.insert(len(ys), float(y))
                    zs.insert(len(zs), z)
                    l.insert(len(l), int(li))
                elif a.lower() == "Start".lower() and b.lower() == "End".lower():
                    xs.insert(len(xs), date_time(x))
                    ys.insert(len(ys), float(y))
                    zs.insert(len(zs), z)
                    l.insert(len(l), int(li))
                elif a.lower() != "Start".lower() and b.lower() != "End".lower() and date_time(a) <= date_time(
                        x) <= date_time(b):
                    xs.insert(len(xs), date_time(x))
                    ys.insert(len(ys), float(y))
                    zs.insert(len(zs), z)
                    l.insert(len(l), int(li))
                elif b.lower() != "End".lower() and a.lower() == "Start".lower() and date_time(b) >= date_time(x):
                    xs.insert(len(xs), date_time(x))
                    ys.insert(len(ys), float(y))
                    zs.insert(len(zs), z)
                    l.insert(len(l), int(li))
                elif a.lower() != "Start".lower() and date_time(a) <= date_time(x) and b.lower() == "End".lower():
                    xs.insert(len(xs), date_time(x))
                    ys.insert(len(ys), float(y))
                    zs.insert(len(zs), z)
                    l.insert(len(l), int(li))

                if b.lower() != "End".lower() and b.lower() != "Now".lower() and date_time(x) >= date_time(b):
                    break

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
            plt.annotate(str(lss[i][0]), xy=(xss[i][-1], yss[i][-1]), xytext=(5, 0), textcoords='offset points',
                         va='center')

        plt.show()
        print("-----------------------------------------------------------\n\n\n")
        main()

    except Exception as e:
        print("\n", e)
        print(" Invalid Input. Please retry\n")
        print("\n-----------------------------------------------------------\n\n\n")
        dr = display()
        animate(dr[0], dr[1])


def date_time(date):
    return datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")


def display():
    print("Please select your date-time range for the graph based on the instructions.\n")
    print("Instructions:\n")
    print("The date-time format: YYYY-mm-dd HH:MM:SS.ffffff\n")
    print("If you want to see from the beginning point, please type 'Start'\n")
    print("If you want to see to the last point, please type 'End'\n")
    print("If you want to see all the points, please type 'Now'\n")
    print("User Input")
    To = input("To: ")
    if To.lower() == "Now".lower():
        From = ""
    else:
        From = input("From: ")
    return From, To


def main():
    d = display()
    animate(d[0], d[1])


main()

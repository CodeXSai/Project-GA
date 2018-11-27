import datetime

from .Enum import *
from Tools.fileio import fileio
import itertools as IT
import copy


class Object:

    def __init__(self, dna, frame, ObjType, ObjPosX, ObjPosY, ObjLength, ObjWidth, SquareColour, index, lane, cwd):
        self.col_line = None
        self._speed_limit = dna.speed_limit
        self._frame = frame
        self._type = ObjType
        self._coordinates = ObjPosY
        self._accelerate = 0
        self._dna = dna
        self._index = index
        self._dirFlag = 1
        self._lane = lane
        self.collide = False
        self._cwd = cwd
        self.start_state = False

        if dna.ratio is None:
            self._ratio = (0, 0, 0)
        else:
            self._ratio = dna.ratio

        self._Points = [(ObjPosX, ObjPosY), (ObjPosX + ObjLength, ObjPosY), (ObjPosX + ObjLength, ObjPosY + ObjWidth),
                        (ObjPosX, ObjPosY + ObjWidth)]
        # self.centroid(self._Points)
        # self.init_radar(dna.radius*dna.ratio[0], dna.radius *dna.ratio[1], dna.radius *dna.ratio[2], aicanvas, "yellow", "green", "red")
        self._Shape = self._frame.canvas.create_polygon(self._Points, fill=SquareColour)
        self.object_coords()

    def is_collide(self):
        return self.collide

    def accelerate(self):
        return self._accelerate

    @property
    def speed_limit(self):
        return self._speed_limit

    @speed_limit.setter
    def speed_limit(self, set_speed):
        self._speed_limit = set_speed

    @property
    def index(self):
        return self._index

    @speed_limit.deleter
    def speed_limit(self):
        del self._speed_limit

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, set_controller):
        self._controller = set_controller

    @controller.deleter
    def controller(self):
        del self._controller

    def front_back(self):
        minX = self._frame.canvas.coords(self._Shape)[0]
        maxX = self._frame.canvas.coords(self._Shape)[2]
        y = self.centroid()
        return [(maxX, y[1]), (minX, y[1])]

    def coordinates(self):
        return self._frame.canvas.coords(self._Shape)

    @staticmethod
    def area_of_polygon(x, y):
        """Calculates the signed area of an arbitrary polygon given its verticies
        http://stackoverflow.com/a/4682656/190597 (Joe Kington)
        http://softsurfer.com/Archive/algorithm_0101/algorithm_0101.htm#2D%20Polygons
        """
        area = 0.0
        for i in range(-1, len(x) - 1):
            area += x[i] * (y[i + 1] - y[i - 1])
        return area / 2.0

    def centroid(self, Points=None):

        if Points is None:
            Points = self._frame.canvas.coords(self._Shape)

        points = [(Points[0], Points[1]), (Points[2], Points[3]), (Points[4], Points[5]), (Points[6], Points[7])]

        if self._type is Type.CAR:
            """
             http://stackoverflow.com/a/14115494/190597 (mgamba)
            """
            area = self.area_of_polygon(*zip(*points))
            result_x = 0
            result_y = 0
            N = len(points)
            points = IT.cycle(points)
            x1, y1 = next(points)
            for i in range(N):
                x0, y0 = x1, y1
                x1, y1 = next(points)
                cross = (x0 * y1) - (x1 * y0)
                result_x += (x0 + x1) * cross
                result_y += (y0 + y1) * cross
            result_x /= (area * 6.0)
            result_y /= (area * 6.0)

            self._CenterX = result_x
            self._CenterY = result_y
            return (result_x, result_y)

    def changeCoords(self):
        self._frame.canvas.coords(self._Shape, self._Shape_coords)

    def border_check(self):
        return self._frame.canvas.coords(self._Shape)[0] > self._frame.root.winfo_screenwidth()

    def move(self, obj):
        speed_strike = .01
        colour = self.fuzzy_logic(obj)  # Calling Fuzzy Logic

        if self.collide is True:
            if self._accelerate > 0:
                self._accelerate -= speed_strike
        elif colour is "yellow" and self.collide is False:
            if self._dirFlag == 2:
                if self._accelerate < self._speed_limit:
                    self._accelerate += speed_strike
            else:
                self._dirFlag = 1
                if self._accelerate > 0:
                    self._accelerate -= speed_strike / 2
        elif colour is "green" and self.collide is False:
            self._dirFlag = 2
        elif colour is "red" and self.collide is False:
            self._dirFlag = 0
            if self._accelerate > 0:
                self._accelerate -= speed_strike
        elif colour is "blue":
            self.collide = True
            if self._accelerate > 0:
                self._accelerate -= speed_strike
        else:
            self._dirFlag = 3
            if self._accelerate < self._speed_limit:
                self._accelerate += speed_strike
        self._frame.canvas.move(self._Shape, self._accelerate, 0)
        if self.border_check():
            self.changeCoords()

        if self.start_state is False:
            self.start_state = True
            l = [datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"), ",", str(self._accelerate), ",black", ",",
                 str(self.index), "\n"]
            stri = "".join(l)
            fileio(self._cwd + '\Tools\GraphInput.txt').write_file(stri)
        elif colour is "yellow":
            l = [datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"), ",", str(self._accelerate), ",y", ",",
                 str(self.index), "\n"]
            stri = "".join(l)
            fileio(self._cwd + '\Tools\GraphInput.txt').write_file(stri)
        elif colour is "green":
            l = [datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"), ",", str(self._accelerate), ",g", ",",
                 str(self.index), "\n"]
            stri = "".join(l)
            fileio(self._cwd + '\Tools\GraphInput.txt').write_file(stri)
        elif colour is "red":
            l = [datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"), ",", str(self._accelerate), ",r", ",",
                 str(self.index), "\n"]
            stri = "".join(l)
            fileio(self._cwd + '\Tools\GraphInput.txt').write_file(stri)
        elif colour is "blue":
            l = [datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"), ",", str(self._accelerate), ",blue", ",",
                 str(self.index), "\n"]
            stri = "".join(l)
            fileio(self._cwd + '\Tools\GraphInput.txt').write_file(stri)

    def object_coords(self):
        self._Shape_coords = self._frame.canvas.coords(self._Shape)

    ###################################################   Fuzzy Logic   ####################################################

    def fuzzy_logic(self, obj):
        col_obj = None
        previous_obj = copy.copy(col_obj)
        col_dist = 1000000000
        colour = "white"
        l = []

        xy = self.centroid()

        if len(obj) > 1:
            for i in range(len(obj)):
                if obj[i].index != self.index:
                    obj_xy = obj[i].centroid()

                    if xy[1] == obj_xy[1] and obj[i].is_collide() is not True:
                        if ((self._dna.radius * self._dna.ratio[0]) + xy[0]) >= obj[i].front_back()[1][0] \
                                and (self._dna.radius * self._dna.ratio[1] + xy[0]) < obj[i].front_back()[1][0] \
                                and self.front_back()[0][0] < obj[i].front_back()[1][0]:
                            if col_dist > (obj[i].front_back()[1][0] - self.front_back()[0][0]):
                                col_dist = (obj[i].front_back()[1][0] - self.front_back()[0][0])
                                col_obj = obj[i]
                            colour = "yellow"

                        elif (self._dna.radius * self._dna.ratio[1] + xy[0]) >= obj[i].front_back()[1][0] \
                                and (self._dna.radius * self._dna.ratio[2] + xy[0]) < obj[i].front_back()[1][0] \
                                and self.front_back()[0][0] < obj[i].front_back()[1][0]:
                            if col_dist > (obj[i].front_back()[1][0] - self.front_back()[0][0]):
                                col_dist = (obj[i].front_back()[1][0] - self.front_back()[0][0])
                                col_obj = obj[i]
                            colour = "green"

                        elif (self._dna.radius * self._dna.ratio[2] + xy[0]) >= obj[i].front_back()[1][0] \
                                and self.front_back()[0][0] < obj[i].front_back()[1][0]:
                            if col_dist > (obj[i].front_back()[1][0] - self.front_back()[0][0]):
                                col_dist = (obj[i].front_back()[1][0] - self.front_back()[0][0])
                                col_obj = obj[i]
                            colour = "red"

                        elif self.front_back()[0][0] >= obj[i].front_back()[1][0] \
                                and self.front_back()[1][0] <= obj[i].front_back()[1][0]:
                            colour = "blue"
                            self._frame.canvas.itemconfig(self._Shape, fill="blue")
                            col_dist = 1000000000
                            self._frame.canvas.delete(self.col_line)
                            col_obj = None
                            self.col_line = None

            if col_dist != 1000000000:
                l.insert(len(l), self.front_back())
                l.insert(len(l), col_obj.front_back())
                if previous_obj is col_dist:
                    self._frame.canvas.itemconfig(self.col_line, l[0][0][0], l[0][0][1], l[1][1][0], l[1][1][1],
                                                  fill=colour)
                else:
                    self._frame.canvas.delete(self.col_line)
                    self.col_line = self._frame.canvas.create_line(l[0][0][0], l[0][0][1], l[1][1][0], l[1][1][1],
                                                                   fill=colour)

            else:
                if self.col_line is not None:
                    col_obj = None
                    self._frame.canvas.delete(self.col_line)
                    col_dist = 1000000000
                    self.col_line = None
        return colour

#################################################   Fuzzy Logic End   ##################################################

from more_itertools import flatten

from .Radar import Radar
from Utility.Controller import Controller
from .Enum import *
import itertools as IT


class Object:

    def __init__(self, dna, aicanvas, frame, ObjType, ObjPosX, ObjPosY, ObjLength, ObjWidth, SquareColour, controller=None):
        self._speed_limit = dna.speed_limit
        self._frame = frame
        self._type = ObjType
        self._coordinates = ObjPosY
        self._accelerate = 0

        self._radar1 = None
        self._radar2 = None
        self._radar3 = None
        if dna.ratio is None:
            self._ratio = (0,0,0)
        else:
            self._ratio = dna.ratio

        self._Points = [(ObjPosX, ObjPosY), (ObjPosX + ObjLength, ObjPosY), (ObjPosX + ObjLength, ObjPosY + ObjWidth), (ObjPosX, ObjPosY + ObjWidth)]

        self.centroid(self._Points)
        self.init_radar(dna.radius*dna.ratio[0], dna.radius *dna.ratio[1], dna.radius *dna.ratio[2], aicanvas, "yellow", "green", "red")
        self._Shape = aicanvas.create_polygon(self._Points, fill=SquareColour)


        if controller is None:
            self._controller = Controller(frame.root, frame.canvas, self._Shape, self._radar1, self._radar2, self._radar3, self.speed_limit)
        else:
            self._controller = controller
        self.object_coords()

    def init_radar(self, radius1, radius2, radius3, aicanvas, colour1, colour2, colour3):
        start_angle = 349
        end_angle = 373
        #self._radar1 = Radar(radius1, aicanvas, self._CenterX, self._CenterY).create_arc(fill=colour1, start=start_angle, end=end_angle)
        #self._radar2 = Radar(radius2, aicanvas, self._CenterX, self._CenterY).create_arc(fill=colour2, start=start_angle, end=end_angle)
        #self._radar3 = Radar(radius3, aicanvas, self._CenterX, self._CenterY).create_arc(fill=colour3, start=start_angle, end=end_angle)

    @property
    def speed_limit(self):
        return self._speed_limit

    @speed_limit.setter
    def speed_limit(self, set_speed):
        self._speed_limit = set_speed

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

    @property
    def coordinates(self):
        return self._coordinates

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

    def centroid(self, points):
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

    def changeCoords(self):
        self._frame.canvas.coords(self._Shape,  self._Shape_coords)
        #self._frame.canvas.coords(self._radar1, self._radar1_coords)
        #self._frame.canvas.coords(self._radar2, self._radar2_coords)
        #self._frame.canvas.coords(self._radar3, self._radar3_coords)

    def border_check(self):
        return self._frame.canvas.coords(self._Shape)[0] > self._frame.root.winfo_screenwidth()

    def move(self):
        self._frame.canvas.move(self._Shape,  self._accelerate, 0)
        #self._frame.canvas.move(self._radar1, self._accelerate, 0)
        #self._frame.canvas.move(self._radar2, self._accelerate, 0)
        #self._frame.canvas.move(self._radar3, self._accelerate, 0)
        if self._accelerate < self._speed_limit:
            self._accelerate += .1
        if self.border_check():
            self.changeCoords()

    def object_coords(self):
        self._Shape_coords  = self._frame.canvas.coords(self._Shape)
        #self._radar1_coords = self._frame.canvas.coords(self._radar1)
        #self._radar2_coords = self._frame.canvas.coords(self._radar2)
        #self._radar3_coords = self._frame.canvas.coords(self._radar3)

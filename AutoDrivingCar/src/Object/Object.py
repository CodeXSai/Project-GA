from .Radar import Radar
from Utility.Controller import Controller
from .Enum import *
import itertools as IT


class Object:

    _speed = None
    _controller = None
    _radar1 = None
    _radar2 = None
    _radar3 = None
    _type = None
    _CenterX = None
    _CenterY = None
    _Shape = None
    _Points = None
    _frame = None

    def __init__(self, speed, radius, aicanvas, frame, ObjType, ObjPosX, ObjPosY, ObjLength, ObjWidth, SquareColour,
                 RadarColour,ratio=None, controller=None):
        self._speed = speed
        self._frame = frame
        self._type = ObjType

        if ratio is None:
            self._ratio = (0,0,0)
        else:
            self._ratio = ratio

        self._Points = [(ObjPosX, ObjPosY), (ObjPosX + ObjLength, ObjPosY), (ObjPosX + ObjLength, ObjPosY + ObjWidth), (ObjPosX, ObjPosY + ObjWidth)]

        self.get_center(self._Points)
        self.init_radar(radius, radius * .6, radius * .4, aicanvas, "yellow", "green", "red")
        self._Shape = aicanvas.create_polygon(self._Points, fill=SquareColour)

        if controller is None:
            self._controller = Controller(frame.root, frame.canvas, self._Shape, self._radar1, self._radar2, self._radar3, self.speed)
        else:
            self._controller = controller

    def init_radar(self, radius1, radius2, radius3, aicanvas, colour1, colour2, colour3):
        start_angle = 349
        end_angle = 373
        self._radar1 = Radar(radius1, aicanvas, self._CenterX, self._CenterY).create_arc(fill=colour1, start=start_angle, end=end_angle)
        self._radar2 = Radar(radius2, aicanvas, self._CenterX, self._CenterY).create_arc(fill=colour2, start=start_angle, end=end_angle)
        self._radar3 = Radar(radius3, aicanvas, self._CenterX, self._CenterY).create_arc(fill=colour3, start=start_angle, end=end_angle)

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, set_speed):
        self._speed = set_speed

    @speed.deleter
    def speed(self):
        del self._speed

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
    def radar(self):
        return self._radar

    @radar.setter
    def radar(self, set_radar):
        self._radar = set_radar

    @radar.deleter
    def radar(self):
        del self._radar

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

    def get_center(self, points):
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


from .Radar import Radar
from Utility.Controller import Controller
from .Enum import *


class Object:

    _speed = None
    _controller = None
    _radar = None
    _type = None
    _CenterX = None
    _CenterY = None
    _Shape = None
    _ObjPosX = None
    _ObjPosY = None
    _ObjLength = None
    _ObjWidth = None

    def __init__(self, speed, radius, aicanvas, frame, ObjType, ObjPosX, ObjPosy, ObjLength, ObjWidth, SquareColour, RadarColour, controller=None):
        self._speed = speed
        self._type = ObjType
        self._ObjPosX = ObjPosX
        self._ObjPosY = ObjPosy
        self._ObjLength = ObjLength
        self._ObjWidth = ObjWidth
        self.get_center()
        self._radar = Radar(radius, aicanvas, self._CenterX, self._CenterY).create_circle_arc(fill=RadarColour)
        self._Shape = aicanvas.create_rectangle(self._ObjPosX, self._ObjPosY, self._ObjLength, self._ObjWidth, fill=SquareColour)

        if controller is None:
            self._controller = Controller(frame.root, frame.canvas, self._Shape, self._radar, self.speed)
        else:
            self._controller = controller


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

    def get_center(self):
        if self._type is Type.CAR:
            self._CenterX = (self._ObjLength + self._ObjPosX) / 2
            self._CenterY = (self._ObjWidth + self._ObjPosY) / 2
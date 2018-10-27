from tkinter import *


class Controller:
    _root = NONE
    _canvas = NONE
    _object1 = NONE
    _object2 = NONE
    _speed = 2

    def __init__(self, set_root, set_canvas, set_object1, set_object2, set_speed):
        global _root
        _root = set_root

        global _canvas
        _canvas = set_canvas

        global _object1
        _object1 = set_object1

        global _object2
        _object2 = set_object2

        global _speed
        _speed = set_speed

        self.key_binding()

    @staticmethod
    def UP(zero):
        _canvas.move(_object1, 0, -1 * _speed)
        _canvas.move(_object2, 0, -1 * _speed)

    @staticmethod
    def DOWN(zero):
        _canvas.move(_object1, 0, 1 * _speed)
        _canvas.move(_object2, 0, 1 * _speed)

    @staticmethod
    def RIGHT(zero):
        _canvas.move(_object1, 1 * _speed, 0)
        _canvas.move(_object2, 1 * _speed, 0)

    @staticmethod
    def LEFT(zero):
        _canvas.move(_object1, -1 * _speed, 0)
        _canvas.move(_object2, -1 * _speed, 0)

    def key_binding(self):
        _root.bind("w", self.UP)
        _root.bind("s", self.DOWN)
        _root.bind("d", self.RIGHT)
        _root.bind("a", self.LEFT)
        _root.bind("W", self.UP)
        _root.bind("S", self.DOWN)
        _root.bind("D", self.RIGHT)
        _root.bind("A", self.LEFT)

    @staticmethod
    def get_speed():
        global _speed
        return _speed

    @staticmethod
    def set_speed(set_speed):
        global _speed
        _speed = set_speed
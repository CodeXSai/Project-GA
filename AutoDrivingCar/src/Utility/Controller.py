from Object.Enum import CONST


class Controller:


    def __init__(self, set_root, set_canvas, set_object1, set_object2, set_object3, set_object4, speed_limit):
        global _root
        _root = set_root

        global _canvas
        _canvas = set_canvas

        global _object1
        _object1 = set_object1

        global _object2
        _object2 = set_object2

        global _object3
        _object3 = set_object3

        global _object4
        _object4 = set_object4

        global _speed_limit
        _speed_limit = speed_limit

        global _accelerate
        _accelerate = CONST.INITIALIZE_ZERO

        self.key_binding()

    @staticmethod
    def UP(zero):
        _canvas.move(_object1, 0, -1 * _speed_limit)
        _canvas.move(_object2, 0, -1 * _speed_limit)
        _canvas.move(_object3, 0, -1 * _speed_limit)
        _canvas.move(_object4, 0, -1 * _speed_limit)

    @staticmethod
    def DOWN(zero):
        _canvas.move(_object1, 0, 1 * _speed_limit)
        _canvas.move(_object2, 0, 1 * _speed_limit)
        _canvas.move(_object3, 0, 1 * _speed_limit)
        _canvas.move(_object4, 0, 1 * _speed_limit)

    @staticmethod
    def RIGHT(zero):
        global _accelerate
        _canvas.move(_object1,  _accelerate, 0)
        _canvas.move(_object2,  _accelerate, 0)
        _canvas.move(_object3,  _accelerate, 0)
        _canvas.move(_object4,  _accelerate, 0)
        if _accelerate < _speed_limit:
            _accelerate += .5

    @staticmethod
    def LEFT(zero):
        global _accelerate
        _canvas.move(_object1,  _accelerate, 0)
        _canvas.move(_object2,  _accelerate, 0)
        _canvas.move(_object3,  _accelerate, 0)
        _canvas.move(_object4,  _accelerate, 0)
        if _accelerate > 0:
            _accelerate -= .5

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
        global _speed_limit
        return _speed_limit

    @staticmethod
    def set_speed(speed_limit):
        global _speed_limit
        _speed_limit = speed_limit


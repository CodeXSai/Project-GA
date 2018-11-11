from random import randint
from Utility.Frame import Frame
from Operational_Logic.DNA import DNA
from Operational_Logic.Population import Population
from Object.Object import Object
from Object.Enum import *


if __name__ == '__main__':
        frame = Frame()
        frame.init_frame("fullscreen", "main")
        point = [196.35100000000037, 55.0, 251.3510000000003, 55.0, 251.3510000000003, 72.5, 196.35100000000037, 72.5]
        point1 = [326.13000000000034, 55.0, 381.13000000000034, 55.0, 381.13000000000034, 72.5, 326.13000000000034, 72.5]
        point
        frame.canvas.create_polygon(point, fill="white")
        frame.canvas.create_polygon(point1, fill="white")
        frame.frame_loop()
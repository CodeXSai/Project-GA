from Utility.Frame import Frame
from Object.Object import Object
from Object.Enum import *

if __name__ == '__main__':
    frame = Frame()
    frame.init_frame("fullscreen", "main")
    #frame.canvas.
    car = Object(5, 70, frame.canvas, frame, Type.CAR, 25, 50, 5, 10, "white", "red")
    frame.frame_loop()
from random import randint
from Utility.Frame import Frame
from Operational_Logic.DNA import DNA
from Operational_Logic.Population import Population
from Object.Object import Object
from Object.Enum import *


class Blueprint:

    def __init__(self):
        self._population = Population(200,1).init_population()
        self.count = 50
        self._frame = Frame()
        self._frame.init_frame("fullscreen", "main")
        #self.init_blueprint_test()
        self.init_road()
        self.update()
        self._frame.frame_loop()

    def init_blueprint_test(self):
        l=[]
        dna = DNA(20, 150, (1, 0.5, 0.35))
        car = Object(dna, self._frame.canvas, self._frame, Type.CAR, 50,
                          self.Yaxis(self.car_coordinates_list()[0][0], self.car_coordinates_list()[0][1]), 55, 17.5,
                          "white")



        dna = DNA(20, 150, (1, 0.5, 0.35))
        car1 = Object(dna, self._frame.canvas, self._frame, Type.CAR, 500,
                          self.Yaxis(self.car_coordinates_list()[0][0], self.car_coordinates_list()[0][1]), 55, 17.5,
                          "white")
        l.insert(len(l), car.front_back())
        l.insert(len(l), car1.front_back())
        print(car1.front_back())

        print([l[0][0][0], l[0][0][1], l[1][1][0], l[1][1][1]])
        self._frame.canvas.create_line(l[0][0][0], l[0][0][1], l[1][1][0], l[1][1][1], fill="green")

        '''
        car = Object(5, 150, self._frame.canvas, self._frame, Type.CAR, 0,
                     self.Yaxis(self.car_coordinates_list()[1][0], self.car_coordinates_list()[1][1]), 55, 17.5,
                     "white")
        car = Object(5, 150, self._frame.canvas, self._frame, Type.CAR, 0,
                     self.Yaxis(self.car_coordinates_list()[2][0], self.car_coordinates_list()[2][1]), 55, 17.5,
                     "white")

        car = Object(5, 150, self._frame.canvas, self._frame, Type.CAR, 0,
                     self.Yaxis(self.car_coordinates_list()[3][0], self.car_coordinates_list()[3][1]), 55, 17.5,
                     "white")
        car = Object(5, 150, self._frame.canvas, self._frame, Type.CAR, 0,
                     self.Yaxis(self.car_coordinates_list()[4][0], self.car_coordinates_list()[4][1]), 55, 17.5,
                     "white")
        car = Object(5, 150, self._frame.canvas, self._frame, Type.CAR, 0,
                     self.Yaxis(self.car_coordinates_list()[5][0], self.car_coordinates_list()[5][1]), 55, 17.5,
                     "white")

        car = Object(5, 150, self._frame.canvas, self._frame, Type.CAR, 0,
                     self.Yaxis(self.car_coordinates_list()[6][0], self.car_coordinates_list()[6][1]), 55, 17.5,
                     "white")
        car = Object(5, 150, self._frame.canvas, self._frame, Type.CAR, 0,
                     self.Yaxis(self.car_coordinates_list()[7][0], self.car_coordinates_list()[7][1]), 55, 17.5,
                     "white")
        car = Object(5, 150, self._frame.canvas, self._frame, Type.CAR, -210,
                     self.Yaxis(self.car_coordinates_list()[8][0], self.car_coordinates_list()[8][1]), 55, 17.5,
                     "white")
        '''



    def init_road(self):
        self._frame.canvas.create_rectangle(0, 0, self._frame.root.winfo_screenwidth(),
                                            self._frame.root.winfo_screenheight())
        self._frame.canvas.create_rectangle(0, 0, self._frame.root.winfo_screenwidth(), 25, fill="green")

        self._frame.canvas.create_rectangle(0, 30, self._frame.root.winfo_screenwidth(), 35, fill="white")
        self.print_lane(35, 215)
        self._frame.canvas.create_rectangle(0, 215, self._frame.root.winfo_screenwidth(), 220, fill="white")

        self._frame.canvas.create_rectangle(0, 225, self._frame.root.winfo_screenwidth(), 255, fill="green")

        self._frame.canvas.create_rectangle(0, 260, self._frame.root.winfo_screenwidth(), 265, fill="white")
        self.print_lane(265, 445)
        self._frame.canvas.create_rectangle(0, 445, self._frame.root.winfo_screenwidth(), 450, fill="white")

        self._frame.canvas.create_rectangle(0, 455, self._frame.root.winfo_screenwidth(), 485, fill="green")

        self._frame.canvas.create_rectangle(0, 490, self._frame.root.winfo_screenwidth(), 495, fill="white")
        self.print_lane(495, 675)
        self._frame.canvas.create_rectangle(0, 675, self._frame.root.winfo_screenwidth(), 680, fill="white")

        self._frame.canvas.create_rectangle(0, 685, self._frame.root.winfo_screenwidth(), 715, fill="green")

    def print_lane(self, start, end):
        lane_no = (end - start)/3

        for i in range(2):
            lane_bar = 0
            while lane_bar < self._frame.root.winfo_screenwidth():
                self._frame.canvas.create_rectangle(lane_bar, start + lane_no - 2.5, lane_bar+20,
                                                    start + lane_no + 2.5, fill="white")
                lane_bar += 40
            lane_no += lane_no

    @staticmethod
    def Yaxis(a, b):
        return ((a+b)/2) - 8.75

    @staticmethod
    def car_coordinates_list():
        return [(35, 92.5), (97.5, 152.5), (157.5, 215), (265, 322.5), (327.5, 382.5), (387.5, 445), (495, 552.5), (557.5, 612.5), (617.5, 675)]

    def create_obj(self, obj):
        if self.count == 50 and len(obj) < len(self._population):
            y = randint(0, 8)
            obj.insert( len(obj), Object(self._population[len(obj)], self._frame, Type.CAR, -210,
                              self.Yaxis(self.car_coordinates_list()[y][0], self.car_coordinates_list()[y][1]), 55,
                              17.5, "white", len(obj)))
            self.count = 0
        return obj

    def move(self, objects):
        for i in range(len(objects)):
            objects[i].move(objects)

    def draw(self):
        obj = []
        while True:
            obj = self.create_obj(obj)
            self.move(obj)
            self._frame.root.after_idle(self.update)
            self.count += 1
            yield

    def update(self):
        self.update = self.draw().__next__
        self._frame._root.after(1000, self.update)
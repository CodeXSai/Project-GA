from random import randint
from Utility.Frame import Frame
from Operational_Logic.DNA import DNA
from Operational_Logic.Population import Population
from Object.Object import Object
from Tools.fileio import fileio
from Object.Enum import CONST
from Object.Enum import Type



class Blueprint:

    def __init__(self, cwd):
        self.obj_count = CONST.INITIALIZE_ZERO
        self.Population = Population(500, 1, cwd)
        self._population = self.Population.init_population()
        self._generation = CONST.INITIALIZE_ZERO
        self.count = CONST.OBJECT_CREATION_DELAY
        self._cwd = cwd

        fileio(self._cwd + CONST.GRAPH_OUTPUT_LOCATION).file_flush()
        self._frame = Frame()
        self._frame.init_frame(CONST.FRAME_SIZE, CONST.TITLE)
        #self.init_blueprint_test()
        self.init_road()
        self.update()
        self._frame.frame_loop()

    def init_blueprint_test(self):
        l= []
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

        self._frame.canvas.create_text(652, 730, fill="white", font="Times 15 bold", text="Population : ")
        self._frame.canvas.create_text(648, 760, fill="white", font="Times 15 bold", text="Generation : ")
        self._frame.canvas.create_text(634, 790, fill="white", font="Times 15 bold", text="Mutation Rate : ")
        self._frame.canvas.create_text(666, 820, fill="white", font="Times 15 bold", text="Fitness : ")
        self._frame.canvas.create_text(608, 850, fill="white", font="Times 15 bold", text="Extinguishing Peirod : ")
        self._frame.canvas.create_text(1311, 730, fill="white", font="Times 15 bold", text="Population Created : ")

        self._P = self._frame.canvas.create_text(808, 730, fill="white", font="Times 15 bold", text=self.Population.population)
        self._G = self._frame.canvas.create_text(808, 760, fill="white", font="Times 15 bold", text="210")
        self._M = self._frame.canvas.create_text(808, 790, fill="white", font="Times 15 bold", text= self.Population.mutation_rate)
        self._F = self._frame.canvas.create_text(808, 820, fill="white", font="Times 15 bold", text="224")
        self._EP = self._frame.canvas.create_text(808, 850, fill="white", font="Times 15 bold", text="10000")
        self._GC = self._frame.canvas.create_text(1451, 730, fill="white", font="Times 15 bold", text="0")


    def print_lane(self, start, end):
        lane_no = (end - start)/3

        for i in range(2):
            lane_bar = CONST.INITIALIZE_ZERO
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
        y = randint(CONST.FIRST_LANE, CONST.LAST_LANE)

        if self.count == CONST.OBJECT_CREATION_DELAY and self.obj_count < len(self._population):
            obj[y].insert(len(obj[y]), Object(self._population[self.obj_count], self._frame, Type.CAR, -210,
                              self.Yaxis(self.car_coordinates_list()[y][0], self.car_coordinates_list()[y][1]), 55,
                              17.5, "white", self.obj_count, y, self._cwd))
            self.obj_count += CONST.COUNT_INC
            self.count = CONST.INITIALIZE_ZERO

        return obj

    def move(self, objects):
        for i in range(len(objects)):
            for j in range(len(objects[i])):
                if objects[i][j].is_collide() is not True or objects[i][j].accelerate() >= 0:
                    objects[i][j].move(objects[i])

    def draw(self):
        obj = []
        for i in range(CONST.ROAD_LANE):
            obj.insert(len(obj), [])
        while True:
            obj = self.create_obj(obj)
            self.move(obj)
            self.count += CONST.COUNT_INC
            self._frame.canvas.itemconfig( self._GC, text=self.obj_count)
            self._frame.root.after_idle(self.update)
            yield

    def update(self):
        self.update = self.draw().__next__
        self._frame._root.after(CONST.UPDATE_FRAME_TIME_DELAY, self.update)

    def update_score(self):
        self._frame.canvas.create_text(652, 730, fill="white", font="Times 15 bold", text="Population : ")
        self._frame.canvas.create_text(609, 760, fill="white", font="Times 15 bold", text="Generation Strength : ")
        self._frame.canvas.create_text(611, 790, fill="white", font="Times 15 bold", text="Generation Created : ")
        self._frame.canvas.create_text(666, 820, fill="white", font="Times 15 bold", text="Fitness : ")
        self._frame.canvas.create_text(608, 850, fill="white", font="Times 15 bold", text="Extinguishing Peirod : ")
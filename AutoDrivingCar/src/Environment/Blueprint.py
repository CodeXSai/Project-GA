import datetime
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

        self.Population = Population(500, 1, cwd)
        self._population = self.Population.init_population()

        self._generation = CONST.INITIALIZE_ONE
        self._cwd = cwd

        self._grace = False

        self.count = CONST.OBJECT_CREATION_DELAY
        self.obj_count = CONST.INITIALIZE_ZERO

        fileio(self._cwd + CONST.GENERATION_FITNESS_LOCATION_CACHE).file_flush()
        fileio(self._cwd + CONST.GENERATION_FITNESS_LOCATION_CACHE).write_file("0:00:00.000000,0"+CONST.NEW_LINE)
        fileio(self._cwd + CONST.GRAPH_OUTPUT_LOCATION).file_flush()
        fileio(self._cwd + CONST.DATA_LOCATION)
        self._gen_file = fileio(self._cwd).create_folder(str(datetime.datetime.now()).replace(":", "."), CONST.DATA_LOCATION)

        self._frame = Frame()
        self._frame.init_frame(CONST.FRAME_SIZE, CONST.TITLE)
        self.init_road()
        self.generation()

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
        self._G = self._frame.canvas.create_text(808, 760, fill="white", font="Times 15 bold", text=self._generation)
        self._M = self._frame.canvas.create_text(808, 790, fill="white", font="Times 15 bold", text= self.Population.mutation_rate)
        self._F = self._frame.canvas.create_text(808, 820, fill="white", font="Times 15 bold", text="00:00:00")
        self._EP = self._frame.canvas.create_text(808, 850, fill="white", font="Times 15 bold", text=CONST.EXTINGUISHING_PERIOD)
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
            obj[y].insert(len(obj[y]), Object(self._population[self.obj_count], self._frame, Type.CAR, -1810,
                              self.Yaxis(self.car_coordinates_list()[y][0], self.car_coordinates_list()[y][1]), 55,
                              17.5, "white", self.obj_count, y, self._cwd))
            self.obj_count += CONST.COUNT_INC
            self.count = CONST.INITIALIZE_ZERO

        return obj

    def move(self, objects, obj_count=None, popul_len=None, graph_delay=None):
        if obj_count is None:
            obj_count = self.obj_count

        if popul_len is None:
            popul_len = len(self._population)

        if graph_delay is None:
            graph_delay = self.graph_delay

        for i in range(len(objects)):
            for j in range(len(objects[i])):
                if objects[i][j].is_collide() is not True or objects[i][j].accelerate() >= 0:
                    objects[i][j].move(objects[i], obj_count, popul_len, graph_delay, self._gen_file, self._generation)

    def draw(self):
        obj = []
        self.graph_delay = CONST.INITIALIZE_ZERO
        self.Ep = CONST.EXTINGUISHING_PERIOD
        for i in range(CONST.ROAD_LANE):
            obj.insert(len(obj), [])
        while True:
            obj = self.create_obj(obj)

            self.move(obj)
            self.count += CONST.COUNT_INC
            self._frame.canvas.itemconfig( self._GC, text=self.obj_count)
            self._frame.root.after_idle(self.update)

            if self.obj_count is self.Population.population:

                self._frame.canvas.itemconfig(self._EP, text=self.Ep)
                self.Ep -= CONST.COUNT_DEC

                if self._grace is False:
                    self.graph_delay = CONST.GRAPH_DELAY
                    self._grace = True
                    self.delay = datetime.datetime.now() +datetime.timedelta(seconds=CONST.DELAY_AFTER_ALL_POPULATION)
                else:
                    if self.graph_delay is CONST.GRAPH_DELAY:
                        self.graph_delay = CONST.INITIALIZE_ZERO
                    else:
                        self.graph_delay += CONST.COUNT_INC

                if self.delay <= datetime.datetime.now():
                    self.reset(obj)
            yield

    def update(self):

        self.update = self.draw().__next__
        self._frame._root.after(CONST.UPDATE_FRAME_TIME_DELAY, self.update)
        self._frame.frame_loop()

    def update_score(self):
        self._frame.canvas.create_text(652, 730, fill="white", font="Times 15 bold", text="Population : ")
        self._frame.canvas.create_text(609, 760, fill="white", font="Times 15 bold", text="Generation Strength : ")
        self._frame.canvas.create_text(611, 790, fill="white", font="Times 15 bold", text="Generation Created : ")
        self._frame.canvas.create_text(666, 820, fill="white", font="Times 15 bold", text="Fitness : ")
        self._frame.canvas.create_text(608, 850, fill="white", font="Times 15 bold", text="Extinguishing Period : ")

    def generation(self):
        self.update()

    def destroy_obj(self, obj):
        for i in range(len(obj)):
            for j in range(len(obj[i])):
                self._frame.del_shape(obj[i][j].Shape)
            obj[i] = []
        self.obj_count = CONST.INITIALIZE_ZERO

    def reset(self, obj):
        self.move(obj, len(self._population), len(self._population), CONST.GRAPH_DELAY)
        self.destroy_obj(obj)

        fitness_list = self.Population.Calc_Fitness(self._gen_file, self._generation)
        avg_fitness = self.Population.get_average_fitness(fitness_list)
        self._frame.canvas.itemconfig(self._F, text=str(avg_fitness))

        # Write average fitness value to file
        li = [str(avg_fitness), ",", str(self._generation), CONST.NEW_LINE]
        stri = "".join(li)
        fileio(self._gen_file + CONST.GENERATION_FITNESS_LOCATION + CONST.GENERATION_FITNESS_FILE_EXTENSION).write_file(stri)
        fileio(self._cwd + CONST.GRAPH_OUTPUT_LOCATION).file_flush()
        self.sort_date_in_file()
        self._population = self.Population.next_generate(fitness_list)

        #reset
        self._generation += CONST.COUNT_INC
        self._grace = False
        self.count = CONST.OBJECT_CREATION_DELAY
        self._frame.canvas.itemconfig(self._G, text=self._generation)
        self.Ep = CONST.EXTINGUISHING_PERIOD
        self._frame.canvas.itemconfig(self._EP, text=self.Ep)

    def sort_date_in_file(self):
        file = fileio(self._gen_file + CONST.GENERATION_FITNESS_LOCATION + CONST.GENERATION_FITNESS_FILE_EXTENSION).read_file()
        xs = []
        for line in file.readlines():
            if len(line) > 1:
                line = line.strip()
                x,y = line.split(',')
                xs.insert(len(xs), (self.date_time(x) - self.date_time("00:00:00.000000")))

        xs = sorted(xs)
        fileio(self._gen_file + CONST.GENERATION_FITNESS_LOCATION_SORT + CONST.GENERATION_FITNESS_FILE_EXTENSION).file_flush()

        for i in range(len(xs)):
            fileio(self._gen_file + CONST.GENERATION_FITNESS_LOCATION_SORT + CONST.GENERATION_FITNESS_FILE_EXTENSION).write_file(str(xs[i])+","+str(i)+CONST.NEW_LINE)

    @staticmethod
    def date_time(date):
        return datetime.datetime.strptime(date, "%H:%M:%S.%f")











import datetime
from copy import deepcopy
from random import *
from mpmath import floor
from Tools.fileio import fileio
from .DNA import DNA
from Object.Enum import CONST, COLOUR


class Population:
    
    def __init__(self, populationNo, mutation_rate, cwd):
        self._population = []
        self._mutation_rate = mutation_rate
        self._populationNo = populationNo
        self._fitness_list_template = []
        self._fitness_template = []
        self._cwd = cwd

    @property
    def population(self):
        return self._populationNo

    @property
    def mutation_rate(self):
        return self._mutation_rate

    def Calc_Fitness(self, file_location, gen_no):
        fitness_list = deepcopy(self._fitness_list_template)
        fitness = deepcopy(self._fitness_template)

        file = fileio(file_location + CONST.GRAPH_OUTPUT_LOCATION + str(gen_no) + CONST.GRAPH_OUTPUT_FILE_EXTENSION).read_file()

        for line in file.readlines():
            if len(line) > 1:
                line = line.strip()
                x, y, z, index = line.split(',')
                a = int(index)
                if fitness_list[a][0] is None:
                    fitness_list[a][0] = x
                    fitness_list[a][2] = z
                elif fitness_list[a][0] is not COLOUR.BLACK:
                    fitness_list[a][1] = x
                    fitness_list[a][2] = z

        fileio(self._cwd + CONST.FITNESS_OUTPUT_LOCATION).file_flush()
        for i in range(len(fitness_list)):
            if fitness_list[i][1] is not None:
                fitness[i] = self.date_time(fitness_list[i][1]) - self.date_time(fitness_list[i][0])
            else:
                fitness[i] = datetime.datetime.now() - self.date_time(fitness_list[i][0])

            #Write fitness value to file
            li = [str(fitness[i]),"index",str(i),CONST.NEW_LINE]
            stri = "".join(li)
            fileio(file_location + CONST.FITNESS_OUTPUT_LOCATION + str(gen_no) + CONST.FITNESS_OUTPUT_FILE_EXTENSION).write_file(stri)

        return fitness

    def next_generate(self, lst):
        for i in range(len(self._population)):
            parent1 = self._population[self.Pick_one(self._population, lst)]
            parent2 = self._population[self.Pick_one(self._population, lst)]
            child = parent1.crossover(parent2)
            self._population[i] = child
        self.mutate(self._population, self.mutation_rate)
        return self._population

    @staticmethod
    def mutate(population_list, mutation_rate):
        mutation = floor(mutation_rate * len(population_list) / 100)
        for i in range(int(mutation)):
            pick = randint(0, len(population_list)-1)
            population_list[pick].mutation()


    def init_population(self):
        for i in range(self._populationNo):
            self._population.insert(len(self._population), DNA(randint(10, 20), randint(50, 100), self.init_ratio()))
            self._fitness_list_template.insert(len(self._fitness_list_template), [None, None, None])
            self._fitness_template.insert(len(self._fitness_template), None)
        return self._population

    def init_ratio(self):
        return (1,0.6,0.4)

    def getBest(self):
        print("")

    def Evaluate(self):
        print("")

    def Is_Finish(self):
        print("")

    @staticmethod
    def get_average_fitness(timedeltas):
        #stackoverflow
        # giving datetime.timedelta(0) as the start value makes sum work on tds
        average_timedelta = sum(timedeltas, datetime.timedelta(0)) / len(timedeltas)
        return average_timedelta

    def getGeneration(self):
        print("")

    def Pick_one(self, population, fitness_list):
        score_fitness = fitness_list
        score_fitness.sort()
        while True:
            probability = randint(0, self.val_index(score_fitness, max(score_fitness)))
            index = randint(0, len(population))

            if index < probability:
                return self.val_index(fitness_list, score_fitness[probability])

    @staticmethod
    def date_time(date):
        return datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")

    @staticmethod
    def val_index(lst, ele):
        for i, j in enumerate(lst):
            if j is ele:
                return i
        return None


import datetime
from random import *
from mpmath import floor
from Tools.fileio import fileio
from .DNA import DNA
from Object.Enum import CONST, COLOUR


class Population:
    
    def __init__(self, populationNo, mutation_rate, cwd):
        self._generation = None
        self._population = []
        self._mutation_rate = mutation_rate
        self._populationNo = populationNo
        self._fitness_list = []
        self._fitness = []
        self._cwd = cwd

    @property
    def population(self):
        return self._populationNo

    @property
    def mutation_rate(self):
        return self._mutation_rate

    def Calc_Fitness(self):
        file = fileio(self._cwd + CONST.GRAPH_OUTPUT_LOCATION).read_file()

        for line in file.readlines():
            if len(line) > 1:
                line = line.strip()
                x, y, z, index = line.split(',')
                a = int(index)
                if self._fitness_list[a][0] is None:
                    self._fitness_list[a][0] = x
                    self._fitness_list[a][2] = z
                elif self._fitness_list[a][0] is not COLOUR.BLACK:
                    self._fitness_list[a][1] = x
                    self._fitness_list[a][2] = z

        fileio(self._cwd + CONST.FITNESS_OUTPUT_LOCATION).file_flush()
        for i in range(len(self._fitness_list)):
            self._fitness[i] = self.date_time(self._fitness_list[i][1]) - self.date_time(self._fitness_list[i][0])

            #Write fitness value to file
            li = [str(self._fitness[i]),"index",str(i),CONST.NEW_LINE]
            stri = "".join(li)
            fileio(self._cwd + CONST.FITNESS_OUTPUT_LOCATION).write_file(stri)

    def natural_selection(self):
        print("")

    def generate(self):
        max_fitness = CONST.INITIALIZE_ZERO
        selected_population: None = self.kill_population(self._population)

        for i in range(len(selected_population)):

            if selected_population[i].fitness > max_fitness:
                max_fitness = selected_population.fitness

        for i in range(len(selected_population)):
            parent1 = self.Pick_one(selected_population, max_fitness)
            parent2 = self.Pick_one(selected_population, max_fitness)
            child = parent1.Crossover(parent2)
            child.mutation(self._mutation_rate)
            self._population[i] = child

        self._generation += CONST.COUNT_INC

    def init_population(self):
        for i in range(self._populationNo):
            self._population.append(DNA(randint(5, 10), randint(100, 200), self.init_ratio()))
            self._fitness_list.insert(len(self._fitness_list),[None,None,None])
            self._fitness.insert(len(self._fitness), None)
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
    def get_average_fitness(population):
        total = CONST.INITIALIZE_ZERO
        for i in range(len(population)):
            total += population[i].fitness
        return total / population.length

    def getGeneration(self):
        print("")

    @staticmethod
    def Pick_one(selected_population, max_fitness):
        while True:
            probability = random.choice(max_fitness)
            index = floor(random.choice(len(selected_population)))

            if probability < selected_population[index].calc_fitness():
                return selected_population[index]

    @staticmethod
    def kill_population(population):
        new_population = None
        for i in range(len(population)):
            if population[i].calc_fitness() > -1.00:
                new_population.append(population[i])
        return new_population

    @staticmethod
    def date_time(date):
        return datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")

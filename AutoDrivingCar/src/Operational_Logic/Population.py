from random import *
from mpmath import floor
from .DNA import DNA


class Population:
    
    def __init__(self, populationNo, mutation_rate):
        self._generation = None
        self._population = []
        self._mutation_rate = mutation_rate
        self._populationNo = populationNo

    def Calc_Fitness(self):
        print("")

    def natural_selection(self):
        print("")

    def generate(self):
        max_fitness = 0
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

        self._generation += 1

    def init_population(self):
        for i in range(self._populationNo):
            self._population.append(DNA(randint(5, 10), randint(100, 200), self.init_ratio()))
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
        total = 0
        for i in range(len(population)):
            total += population[i].fitness
        return total / population.length

    def getGeneration(self):
        print("")

    @staticmethod
    def Pick_one(selected_population, max_fitness):
        while 1:
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

import random
from mpmath import floor


class Population:

    _mutation_rate = 0
    _population = 0
    _generation = 0
    _Average_Fitness = 0
    
    def __init__(self, mutation_rate):
        self._mutation_rate = mutation_rate

    def Calc_Fitness(self):


    def natural_selection(self):
        print("")

    def generate(self):

        max_fitness = 0
        selected_population = self.kill_population(self._population)

        for i in len(selected_population):

            if selected_population.fitness > max_fitness:
                max_fitness = selected_population.fitness

        for i in len(selected_population):
            parent1 = self.Pick_one(selected_population, max_fitness)
            parent2 = self.Pick_one(selected_population, max_fitness)
            child = parent1.Crossover(parent2)
            child.Mutation(self._mutation_rate)
            self._population[i] = child

        self._generation += 1


    def getBest(self):


    def Evaluate(self):


    def Is_Finish(self):


    def Get_Average_Fitness(self, population):
        total = 0
        for i in range(population.length):
            total += population[i].fitness
        return total / population.length

    def getGeneration(self):


    def Pick_one(self, selected_population, max_fitness):

        while 1:
            probability = random.choice(max_fitness)
            index = floor(random.choice(len(selected_population)))

            if probability < selected_population[index].fitness:
                return selected_population[index]

    def kill_population(self, population):

        new_population = Population(self._mutation_rate)
        for i in range(population.length):
            if population[i].target_collide_dist > last_arc:
                new_population.push = population[i]
        return new_population
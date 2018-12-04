from random import *


class DNA:

    def __init__(self, speed_limit, arc_radius, arc_ratio):
        self._time = None
        self._speed_limit = speed_limit
        self._arc_radius = arc_radius
        self._arc_ratio = arc_ratio

    @property
    def speed_limit(self):
        return self._speed_limit

    @property
    def radius(self):
        return self._arc_radius

    @property
    def ratio(self):
        return self._arc_ratio

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, set_time):
        self._time = set_time

    def calc_fitness(self):
        return self.time

    def crossover(self, partner):
        if randint(0,1) == 0:
            child = randint(0,2)
            if child == 0:
                newDNA = DNA(self.speed_limit, partner.radius, partner.ratio)
            elif child == 1:
                newDNA = DNA(partner.speed_limit, self.radius, partner.ratio)
            else:
                newDNA = DNA(partner.speed_limit,partner.radius,self.ratio)
        else:
            partner = randint(0,2)
            if partner == 0:
                newDNA = DNA(partner.speed_limit, self.radius, self.ratio)
            elif partner == 1:
                newDNA = DNA(self.speed_limit, partner.radius, self.ratio)
            else:
                newDNA = DNA(self.speed_limit,self.radius,partner.ratio)
        return newDNA

    def mutation(self, percentage):
        random = randint(0, 1)

        if random is 0:
            if randint(0,1) == 0:
                self._speed_limit -= randint(5,10)* percentage
            else:
                self._speed_limit += randint(5,10)* percentage

        else:
            if randint(0,1) == 0:
                self._arc_radius -= randint(1,10)*percentage
            else:
                self._arc_radius += randint(1,10)*percentage











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

        try:
            if randint(0, 1) == 0:
                child = randint(0, 2)
                if child == 0:
                    newDNA = DNA(self.speed_limit, partner.radius, partner.ratio)
                elif child == 1:
                    newDNA = DNA(partner.speed_limit, self.radius, partner.ratio)
                else:
                    newDNA = DNA(partner.speed_limit, partner.radius, self.ratio)
            else:
                partner_selection = randint(0, 2)
                if partner_selection == 0:
                    newDNA = DNA(partner.speed_limit, self.radius, self.ratio)
                elif partner_selection == 1:
                    newDNA = DNA(self.speed_limit, partner.radius, self.ratio)
                else:
                    newDNA = DNA(self.speed_limit, self.radius, partner.ratio)
            return newDNA
        except Exception as e:
            print(e)

    def mutation(self, percentage):
        if randint(0, 100) < percentage:
            self._speed_limit = randint(5, 10)
        elif randint(0, 100) < percentage:
            self._arc_radius = randint(100, 200)











import os

from Operational_Logic.Population import *

p = Population(200, 1, os.getcwd())
p.init_population()
p.Calc_Fitness()
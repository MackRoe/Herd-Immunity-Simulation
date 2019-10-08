from simulation import Simulation
from virus import Virus
import unittest

class xfunction(unittest.TestCase):

     def xtype_of_cases(self):
         # tests normal cases (x,y,z)
         sim = Simulation(100, .9, virus, 1)
         virus = Virus("Ebola", .25, .7)
        assert sim.create_population(1) is []


if __name__ == '__main__':
    unittest.main()
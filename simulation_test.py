from simulation import Simulation
from virus import Virus
import unittest

class xfunction(unittest.TestCase):

     def xtype_of_cases(self):
         # tests normal cases (x,y,z)
         sim = Simulation(100000, .9, virus, 10)
         virus = Virus("Ebola", .25, .7)
          assert Simulation.create_population('') is []


if __name__ == '__main__':
    unittest.main()
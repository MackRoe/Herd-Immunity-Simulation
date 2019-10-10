from simulation import Simulation
from virus import Virus
import unittest
import pytest

class xfunction(unittest.TestCase):

     def xtype_of_cases(self):
         # tests normal cases (x,y,z)
         sim = Simulation(100, .9, virus, 1)
         virus = Virus("Ebola", .25, .7)
        assert sim.create_population(1) is []

    def test_simulation_init():
        sim = Simulation(100, 0.75, 1, AIDS)
        assert pop_size == 100
        assert vacc_percentage == 0.75
        assert initial_infected == 1
        assert virus == AIDS

    def test_create_population():
        assert not self.population == []

    def test_simulation_should_continue():
        assert not dead_count == []

    def test_run():
        assert not self.total_infected == 0

    def test_time_step():
        assert not interaction_count == 0
        assert not self.total_dead == 0

    def test_interaction(person, random_person):
        assert not person.is_alive == False
        assert not random_person.is_alive == False

    def test_infect_newly_infected():
        assert person.infection == self.virus


    
    

    


if __name__ == '__main__':
    unittest.main()
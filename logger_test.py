from logger import Logger
from person import Person
from virus import Virus
import os

virus1 = Virus("Ebola", .25, .5)
virus2 = Virus("HIV", .35, .8)

person = Person(1, False,)
person2 = Person(2, True)
person3 = Person(3, False, virus1)
print(person3.did_survive_infection())
person4 = Person(4, False, virus2)
print(person4.did_survive_infection())



def test_write_metadata(pop_size, vacc_percentage, virus, mortality_rate, repro_rate):
    logger = Logger("tester_log.txt")
    logger.write_metadata(100, .9, "Ebola", .8, .25)

    with open('tester_log.txt', 'r') as file:
        test_value = file.read()
        assert test_value == 'Population Size: 100    Vaccination Percentage: 0.9    Virus: Ebola    Mortality Rate: 0.8    Basic Reproduction Number: 0.25\n'

    os.remove('tester_log.txt')

    
def test_log_interaction(person, random_person, random_person_sick, random_person_vac = None, did_infect = None):
    assert not random_person_sick == None

def test_log_infection_survival(person, did_survive_from_infection):

    assert not file.write("")

def test_log_time_step(time_step_number=352):
    assert time_step_number == 352

    


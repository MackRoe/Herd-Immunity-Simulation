from logger import Logger
from person import Person
from virus import Virus

virus1 = Virus("Ebola", .25, .5)
virus2 = Virus("HIV", .35, .8)

person = Person(1, False,)
person2 = Person(2, True)
person3 = Person(3, False, virus1)
print(person3.did_survive_infection())
person4 = Person(4, False, virus2)
print(person4.did_survive_infection())

logger = Logger()
logger.write_metadata(100, .9, "Ebola", .8, .25)




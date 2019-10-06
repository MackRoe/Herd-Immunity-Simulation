class Virus(object):
    '''Properties and attributes of the virus used in Simulation.'''

    def __init__(self, name, repro_rate, mortality_rate):
        self.name = name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate

    def get_params():
        self.name = input("What disease would you like to use for the simulation?")
        self.repro_rate = input("What is the reproduction rate of the disease?")
        self.mortality_rate = input("What is the mortality rate of the disease?")
        Virus = [self.name, self.repro_rate, self.mortality_rate]


def test_virus_instantiation():
    #TODO: Create your own test that models the virus you are working with
    '''Check to make sure that the virus instantiator is working.'''
    virus = Virus("tuberculosis", 0.1, 0.6)
    assert virus.name == "tuberculosis"
    assert virus.repro_rate == 0.1
    assert virus.mortality_rate == 0.6

from simulation import Simulation
from person import Person
from virus import Virus
from logger import Logger

""" Tests for simulation class """

def test_init_parameters():
    person = Person(1, is_vaccinated=True, infection=None)
    simulation = Simulation(virus="Dysentry", repro_rate=0.5, mortality_rate=0.5, pop_size=1000, percent_pop_vaccinated=0.5, initial_infected=10)
    population = [person]

    assert pop_size == 1000
    assert percent_pop_vaccinated == 0.5
    assert virus is "Dysentry"
    assert mortality_rate == 0.5
    assert repro_rate == 0.5
    assert initial_infected == 10

    assert len(population) == pop_size


def test_logger_created():
    simulation.Simulation.logger = Logger(test_logger.txt)
    assert simulation.Simulation.logger.name == test_logger.txt

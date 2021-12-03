import random, sys
random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
    def __init__(self, virus, pop_size, percent_pop_vaccinated, initial_infected=1):
        self.logger = None
        self.population = self._create_population() # List of Person objects
        self.pop_size = int(pop_size) # Int
        self.next_person_id = 0 # Int
        self.virus = virus # Virus object
        self.initial_infected = int(initial_infected) # Int
        self.total_infected = 0 # Int
        self.current_infected = 0 # Int
        self.percent_pop_vaccinated = float(percent_pop_vaccinated) # float between 0 and 1
        self.total_dead = 0 # Int
        self.file_name = f"{virus.name}_simulation_pop_{pop_size}_vp_{percent_pop_vaccinated}_infected_{initial_infected}.txt"
        self.newly_infected = []

    def _create_population(self):
        # Create array to contain total population and start simulation
        population_array = []
        # Number of people to vaccinate
        start_vaccinated = self.pop_size * self.percent_pop_vaccinated
        # Number of Healthy people 
        start_uninfected = self.pop_size - self.initial_infected - start_vaccinated
        # Number of Infected people
        start_infected = self.initial_infected
        count = 1

        for i in range(0, start_infected):
            count += 1
            person = Person(i, False, self.virus)
            population_array.append(person)

        for i in range(0, start_uninfected):
            count += 1
            person = Person(i, False, None)
            population_array.append(person)

        for i in range(0, start_vaccinated):
            count += 1
            person = Person(i, True, None)
            population_array.append(person)

        return population_array


    def _simulation_should_continue(self):
        
        for person in self.population:
            if person.is_alive == True & person.is_vaccinated == False:
                return True
        return False
 
    def run(self):
        ''' This method should run the simulation until all requirements for ending
        the simulation are met.
        '''
        # TODO: Finish this method.  To simplify the logic here, use the helper method
        # _simulation_should_continue() to tell us whether or not we should continue
        # the simulation and run at least 1 more time_step.

        # TODO: Keep track of the number of time steps that have passed.
        # HINT: You may want to call the logger's log_time_step() method at the end of each time step.
        # TODO: Set this variable using a helper
        time_step_counter = 0
        should_continue = True

        while should_continue:
            # TODO: for every iteration of this loop, call self.time_step() to compute another
            # round of this simulation.
            print(f'The simulation has ended after {time_step_counter} turns.')
            should_continue = self._simulation_should_continue()

    def time_step(self):
        ''' This method should contain all the logic for computing one time step
        in the simulation.

        This includes:
            1. 100 total interactions with a randon person for each infected person
                in the population
            2. If the person is dead, grab another random person from the population.
                Since we don't interact with dead people, this does not count as an interaction.
            3. Otherwise call simulation.interaction(person, random_person) and
                increment interaction counter by 1.
            '''
        # TODO: Finish this method.
        pass

    def interaction(self, person, random_person):
        '''This method should be called any time two living people are selected for an
        interaction. It assumes that only living people are passed in as parameters.

        Args:
            person1 (person): The initial infected person
            random_person (person): The person that person1 interacts with.
        '''
        # Assert statements are included to make sure that only living people are passed
        # in as params
        assert person.is_alive == True
        assert random_person.is_alive == True

        # TODO: Finish this method.
        #  The possible cases you'll need to cover are listed below:
            # random_person is vaccinated:
            #     nothing happens to random person.
            # random_person is already infected:
            #     nothing happens to random person.
            # random_person is healthy, but unvaccinated:
            #     generate a random number between 0 and 1.  If that number is smaller
            #     than repro_rate, random_person's ID should be appended to
            #     Simulation object's newly_infected array, so that their .infected
            #     attribute can be changed to True at the end of the time step.
        # TODO: Call slogger method during this method.
        pass

    def _infect_newly_infected(self):
        ''' This method should iterate through the list of ._id stored in self.newly_infected
        and update each Person object with the disease. '''
        # TODO: Call this method at the end of every time step and infect each Person.
        # TODO: Once you have iterated through the entire list of self.newly_infected, remember
        # to reset self.newly_infected back to an empty list.
        pass


if __name__ == "__main__":
    pop_size = 100
    percent_pop_vaccinated = 0.15
    initial_infected = 10

    name = "Dysentery"
    repro_rate = 0.7
    mortality_rate = 0.2
    virus = Virus(name, repro_rate, mortality_rate)
    sim = Simulation(virus, pop_size, percent_pop_vaccinated, initial_infected)

    sim.run()


# if __name__ == "__main__":

    
#     params = sys.argv[1:]
#     virus_name = str(params[0])
#     repro_num = float(params[1])
#     mortality_rate = float(params[2])

#     pop_size = int(params[3])
#     percent_pop_vaccinated = float(params[4])

#     if len(params) == 6:
#         initial_infected = int(params[5])
#     else:
#         initial_infected = 1
#    # self, name, repro_rate, mortality_rate
#     virus = Virus(name, repro_rate, mortality_rate)
#     sim = Simulation(virus, pop_size, percent_pop_vaccinated, initial_infected)

#     sim.run()

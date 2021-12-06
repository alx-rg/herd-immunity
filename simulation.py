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
        print('App is running (def run(self))')
        time_step_counter = 0
        should_continue = True

        while should_continue:
            # TODO: for every iteration of this loop, call 
            self.time_step() 
            time_step_counter += 1
            self.logger.log_time_step(time_step_counter)            
            should_continue = self._simulation_should_continue()
            print(should_continue)
        print(f'The simulation has ended after {time_step_counter} turns.')

    def choose_random_healthy(self):
        choose_person = random.choice(self.population)
        while choose_person.is_alive == True and choose_person.infection is None:
            choose_person = random.choice(self.population)
        return choose_person

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
        for person in self.population:
            if person.infection is not None and person.is_alive == True:
                print('Time Step')
                interaction_count=0
                while interaction_count < 100:
                    random_person = self.choose_random_healthy()
                    if random_person.is_alive == False:
                        continue
                    elif random_person._id == person._id:
                        continue
                    else:
                        self.interaction(person, random_person)
                        interaction_count += 1
                        print(interaction_count)
        # for person in self.population:
        #     if person.infection is not None and person.is_alive == True:
        #         self.logger.log_infection_survival(person, False)
        self._infect_newly_infected()
                    
        # TODO: Finish this method.
        

    def interaction(self, person, random_person):
        '''This method should be called any time two living people are selected for an
        interaction. It assumes that only living people are passed in as parameters.

        Args:
            person1 (person): The initial infected person
            random_person (person): The person that person1 interacts with.
        '''
        assert person.is_alive == True
        assert random_person.is_alive == True

        # TODO: Finish this method.
        if random_person.is_vaccinated == True:
            self.logger.log_interaction(person, random_person, was_infected=None, person2_vacc=True, person2_sick=None)
        elif random_person.infection != None:
            self.logger.log_interaction(person, random_person, was_infected=None, person2_vacc=None, person2_sick=True)
        else:
            if random.uniform(0,1) < repro_rate:
                self.newly_infected.append(random_person._id)
                self.logger.log_interaction(person, random_person, was_infected=True, person2_vacc=None, person2_sick=None)
            else:
                self.logger.log_interaction(person, random_person, was_infected=False, person2_vacc=None, person2_sick=None)
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
        

    def _infect_newly_infected(self):
        ''' This method should iterate through the list of ._id stored in self.newly_infected
        and update each Person object with the disease. '''
        # TODO: Call this method at the end of every time step and infect each Person.
        # TODO: Once you have iterated through the entire list of self.newly_infected, remember
        
        
        
        # to reset self.newly_infected back to an empty list.             
        self.newly_infected = []


if __name__ == "__main__":
    # pop_size = 100
    # percent_pop_vaccinated = 0.15
    # initial_infected = 10

    # name = "Dysentery"
    # repro_rate = 0.7
    # mortality_rate = 0.2
    # virus = Virus(name, repro_rate, mortality_rate)
    # sim = Simulation(virus, pop_size, percent_pop_vaccinated, initial_infected)

    # sim.run()

    virus1 = Virus("Dysentery", 0.7, 0.2)
    firstSim = Simulation(virus1, 1000, 0.2, 10)
    print(f'first sim create population?: {firstSim._create_population()}')
    print(f'first sim create population?: {firstSim.run()}')
  

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

from math import log
import random, sys
# random.seed(42)
from person import Person
from logger import Logger
from virus import Virus

#======================================================================================================

class Simulation(object):
    def __init__(self, virus, pop_size, percent_pop_vaccinated, initial_infected=1):
        self.logger = Logger('journal.txt')
        self.pop_size = int(pop_size) # Int
        self.next_person_id = 0 # Int
        self.virus = virus # Virus object
        self.initial_infected = int(initial_infected) # Int
        self.total_infected = int(initial_infected) # Int
        self.current_infected = 0 # Int
        self.percent_pop_vaccinated = float(percent_pop_vaccinated) # float between 0 and 1
        self.total_dead = 0 # Int
        self.file_name = f"{virus.name}_simulation_pop_{pop_size}_vp_{percent_pop_vaccinated}_infected_{initial_infected}.txt"
        self.vaccinated = 0
        self.newly_dead = 0
        self.newly_infected = []
        self.population = self._create_population() # List of Person objects
        self.count_time_steps = 0

#======================================================================================================
   
    def _create_population(self):
        # Create array to contain total population and start simulation
        population_array = []
        # Number of people to vaccinate
        start_vaccinated_float = self.pop_size * self.percent_pop_vaccinated
        start_vaccinated = int(start_vaccinated_float)
        # Number of Healthy people 
        start_uninfected = self.pop_size - self.initial_infected - start_vaccinated
        # Number of Infected people
        start_infected = self.initial_infected
        print(f'in Create Population I have x amount of infected : {start_infected}')
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

#======================================================================================================
   
    def _simulation_should_continue(self):
        
        for person in self.population:
            if person.is_alive == True & person.is_vaccinated == False:
                return True
        return False
        

 #======================================================================================================
    
    def run(self):
        ''' This method should run the simulation until all requirements for ending
        the simulation are met.
        '''
        print('App is running (def run(self))')
        should_continue = True

        while should_continue:
            # TODO: for every iteration of this loop, call 
            self.time_step() 
            self.count_time_steps += 1
            # self.logger.log_time_step(count_time_steps)            
            should_continue = self._simulation_should_continue()
            # print(should_continue)
        print(f'The simulation has ended after {self.count_time_steps} turns.')
        total_pop_alive = self.pop_size - self.total_dead
        self.logger.summary(total_pop_alive, self.total_dead, self.vaccinated)

#======================================================================================================
  
    def choose_random_person(self):
        choose_person = random.choice(self.population)
        while choose_person.is_alive == False:
            choose_person = random.choice(self.population)
        return choose_person
        # choose_person = random.choice(self.population)
        # while choose_person.is_alive == True and choose_person.infection is None:
        #     choose_person = random.choice(self.population)
        # return choose_person

#======================================================================================================
   
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
        print('Time Step')
        deaths = 0
        print(self.current_infected)
        for person in self.population:
            if person.infection is not None and person.is_alive == True:
                print(f'infected person: {person._id}')
                print(f'total infected: {self.total_infected}')
                # print('Time Step')
                interaction_count=100
                while interaction_count > 0:
                    random_person = self.choose_random_person()
                    self.interaction(person, random_person)
                    interaction_count -= 1
                if person.did_survive_infection() == True:
                    person.infection = None
                    person.is_vaccinated = True
                    self.current_infected -= 1
                    self.vaccinated += 1
                    self.logger.log_infection_survival(person, True)
                else:
                    self.total_dead +=1 
                    self.total_infected -= 1
                    deaths += 1
                    self.logger.log_infection_survival(person, False)
                        
                        # print(interaction_count)
        # for person in self.population:
        #     if person.infection is not None and person.is_alive == True:
        #         self.logger.log_infection_survival(person, False)
        total_alive = self.pop_size - deaths
        self.logger.log_time_step(self.count_time_steps, len(self.newly_infected), total_alive, deaths, self.vaccinated, self.total_dead)
        self._infect_newly_infected()
       
        #self.current_infected = []
        # TODO: Finish this method.
        
#======================================================================================================
  
    def interaction(self, person, random_person):
        
        '''
        This method should be called any time two living people are selected for an
        interaction. It assumes that only living people are passed in as parameters.

        Args:
            person1 (person): The initial infected person
            random_person (person): The person that person1 interacts with.
        '''
        assert person.is_alive == True
        assert random_person.is_alive == True

        if random_person.is_vaccinated == False and random_person.infection == None:
            if random.uniform(0,1) < person.infection.repro_rate:  
                if random_person._id not in self.newly_infected:
                    self.newly_infected.append(random_person._id)
                    self.total_infected += 1
        elif random_person.infection != None or random_person.is_vaccinated == True:
            print('In the "elif" condition of interaction')
            pass    


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
        
#======================================================================================================
   
   
    def _infect_newly_infected(self):
        ''' This method should iterate through the list of ._id stored in self.newly_infected
        and update each Person object with the disease. '''
        # TODO: Call this method at the end of every time step and infect each Person.
        # TODO: Once you have iterated through the entire list of self.newly_infected, remember
        for id in self.newly_infected:
            for person in self.population:
                if person._id == id:
                    person.infection = self.virus
        newly_infected_set = set(self.newly_infected)
        print("Newly Infected Set Below")
        print(newly_infected_set)     
        print(self.newly_infected)
        # to reset self.newly_infected back to an empty list.             
        self.newly_infected = []
        print(self.newly_infected)
#======================================================================================================

if __name__ == "__main__":
    pop_size = 100
    percent_pop_vaccinated = 0.10
    initial_infected = 10

    name = "Dysentery"
    repro_rate = 0.7
    mortality_rate = 0.2
    virus = Virus(name, repro_rate, mortality_rate)
    sim = Simulation(virus, pop_size, percent_pop_vaccinated, initial_infected)

    sim.run()


    # virus1 = Virus("Dysentery", 0.7, 0.2)
    # firstSim = Simulation(virus1, 1000, 0.2, 10)
    # print(f'first sim create population?: {firstSim._create_population()}')
    # print(f'first sim create population?: {firstSim.run()}')
  

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

#     python3 simulation.py Ebola 0.70 0.25 100 0.10 10

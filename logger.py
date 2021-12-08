from virus import Virus
from simulation import Simulation

class Logger(object):
    ''' Utility class responsible for logging all interactions during the simulation. '''
    # TODO: Write a test suite for this class to make sure each method is working
    # as expected.

    # PROTIP: Write your tests before you solve each function, that way you can
    # test them one by one as you write your class.

    def __init__(self, file_name):
        # TODO:  Finish this initialization method. The file_name passed should be the
        # full file name of the file that the logs will be written to.
        self.file_name = None

    def write_metadata(self, name, repro_rate, mortality_rate, pop_size, percent_pop_vaccinated, initial_infected):
        '''
        The simulation class should use this method immediately to log the specific
        parameters of the simulation as the first line of the file.
        '''
        # TODO: Finish this method. This line of metadata should be tab-delimited
        # it should create the text file that we will store all logs in.
        # TIP: Use 'w' mode when you open the file. For all other methods, use
        # the 'a' mode to append a new log to the end, since 'w' overwrites the file.
        # NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!
        log = open(self.file_name, 'w')
        journal = open('journal.txt', 'w')

        log.write(f'Starting Population size: {pop_size}\n Percentage Vaccinated: {percent_pop_vaccinated}, Initially Infected: {initial_infected}, Virus Name: {name}, Virus Reproduction Rate: {repro_rate}, Virus Mortality Rate: {mortality_rate}')
        
        journal.write(f'Starting Population size: {pop_size}, Percentage Vaccinated: {percent_pop_vaccinated}, Initially Infected: {initial_infected}, Virus Name: {name}, Virus Reproduction Rate: {repro_rate}, Virus Mortality Rate: {mortality_rate}')

    def log_interaction(self, person, random_person, random_person_sick=None,
                        random_person_vacc=None, did_infect=None):
        '''
        The Simulation object should use this method to log every interaction
        a sick person has during each time step.

        The format of the log should be: "{person.ID} infects {random_person.ID} \n"

        or the other edge cases:
            "{person.ID} didn't infect {random_person.ID} because {'vaccinated' or 'already sick'} \n"
        '''
        # TODO: Finish this method. Think about how the booleans passed (or not passed)
        # represent all the possible edge cases. Use the values passed along with each person,
        # along with whether they are sick or vaccinated when they interact to determine
        # exactly what happened in the interaction and create a String, and write to your logfile.


    def log_infection_survival(self, person, did_die_from_infection):
        ''' The Simulation object uses this method to log the results of every
        call of a Person object's .resolve_infection() method.

        The format of the log should be:
            "{person.ID} died from infection\n" or "{person.ID} survived infection.\n"
        '''
        # TODO: Finish this method. If the person survives, did_die_from_infection
        # should be False.  Otherwise, did_die_from_infection should be True.
        # Append the results of the infection to the logfile
        pass

    def log_time_step(self, time_step_number):

        log = open(self.file_name, 'a')
        log.write(f'\nTime step #{time_step_number} ended, beginning time step #{time_step_number + 1}.')

    def summary(self, population, total_infected):
        deaths = 0
        for person in population:
            if person.is_alive == False:
                deaths += 1
            else:
                pass
        print(f'The total number of infected is {total_infected}')
        print(f'The total number of dead is {deaths}')

        journal = open('journal.txt', 'a')
        journal.write(f'\nThe percentage of total infected was {total_infected/len(population) * 100}% \nThe percentage of total dead was {deaths/len(population) * 100}%')

        #log.write('Time Step #{time_step_number} ended. Begin Time Step #{time_step_number + 1}')

        ''' STRETCH CHALLENGE DETAILS:

        If you choose to extend this method, the format of the summary statistics logged
        are up to you.

        At minimum, it should contain:
            The number of people that were infected during this specific time step.
            The number of people that died on this specific time step.
            The total number of people infected in the population, including the newly infected
            The total number of dead, including those that died during this time step.

        The format of this log should be:
            "Time step {time_step_number} ended, beginning {time_step_number + 1}\n"
        '''
        # TODO: Finish this method. This method should log when a time step ends, and a
        # new one begins.
        # NOTE: Here is an opportunity for a stretch challenge!
        pass



# Header
# Initial size of the population
# Initial number of infected people
# Name of the virus
# Stats for the virus
# Date the simulation was run
# For each time step log
# The number of new infections
# The number of deaths
# Statistics for the current state of the population
# Total number of living people
# Total number of dead people
# Total number of vaccinated people
# After simulation ends
# Total living
# Total dead
# Number of vaccinations
# Why the simulation ended
# Total number of interactions that happened in the simulation
# Number of interactions that resulted in vaccination
# Number of interactions that resulted in death

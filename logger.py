from math import log
from person import Person

class Logger(object):
    ''' Utility class responsible for logging all interactions during the simulation. '''
    # TODO: Write a test suite for this class to make sure each method is working
    # as expected.

    # PROTIP: Write your tests before you solve each function, that way you can
    # test them one by one as you write your class.

#======================================================================================================
    def __init__(self, file_name):

        # TODO:  Finish this initialization method. The file_name passed should be the
        # full file name of the file that the logs will be written to.
        self.file_name = file_name

#======================================================================================================
   
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
        # log = open(self.file_name, 'w')
        log = open(self.file_name, 'w')

        # log.write(f'log=Starting Population size: {pop_size}\n Percentage Vaccinated: {percent_pop_vaccinated}, Initially Infected: {initial_infected}, Virus Name: {name}, Virus Reproduction Rate: {repro_rate}, Virus Mortality Rate: {mortality_rate}')
        log.write('=-=-=-=-=-=-=-< Herd Immunity Simulation >-=-=-=-=-=-=-=\n')
        log.write(f'Starting Population size: {pop_size}\n')
        log.write(f'Percentage Vaccinated: {percent_pop_vaccinated}\n')
        log.write(f'Initially Infected: {initial_infected}\n')
        log.write(f'Virus Name: {name}\n')
        log.write(f'Virus Reproduction Rate: {repro_rate}\n')
        log.write(f'Virus Mortality Rate: {mortality_rate}\n')
        log.write('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')
        log.close()

#======================================================================================================
  
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
        log = open(self.file_name, 'a')
        log.write(f'\nInfected Person: #{person._id} Exposed Person #{random_person._id}')

        if did_infect == True:
            log.write(f'\nPerson #{person._id} infected person #{random_person._id}')
        elif random_person_vacc == True:
            log.write(f'\nPerson #{person._id} did not infect Person #{random_person._id} because they are already vaccinated against the infection.')
        elif random_person_sick == True:
            log.write(f'\Person #{person._id} did not infect Person #{random_person._id} since they are already infected')
        else:
            log.write(f'\nPerson #{person._id} tried but did not infect person #{random_person._id}')
        log.close()
            
#======================================================================================================
   
    def log_infection_survival(self, person, did_die_from_infection):
        
        ''' The Simulation object uses this method to log the results of every
        call of a Person object's .resolve_infection() method.

        The format of the log should be:
            "{person.ID} died from infection\n" or "{person.ID} survived infection.\n"
        '''
        # log = open(self.file_name, 'a')
        # death = (f'Person #{person._id} died from the infection\n')
        # survived = (f'Person #{person._id} survived the infection\n')
        # log.write(survived if did_die_from_infection else death)
        # log.close()
        pass

        # TODO: Finish this method. If the person survives, did_die_from_infection
        # should be False.  Otherwise, did_die_from_infection should be True.
        # Append the results of the infection to the logfile
        
#======================================================================================================
    def log_time_step(self, count_time_steps, newly_infected, total_alive, deaths, vaccinated, total_dead):
        
        log = open(self.file_name, 'a')
        log.write(f'\n=-=-=-=-=-=-=-=-=-=-< Time Step {count_time_steps} >-=-=-=-=-=-=-=-=-=-=\n')
        log.write(f'Results of Time Step #{count_time_steps} below:\n')
        log.write(f'New Infections: {newly_infected}\n')
        log.write(f'New Deaths: {deaths}\n')
        log.write(f'Total Alive: {total_alive}\n')
        log.write(f'Total vaccinated: {vaccinated}\n')
        log.write(f'Total dead : {total_dead}\n')
        log.write('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')         
        log.close()
#======================================================================================================
   
    # def summary(self, total_alive, total_dead, vaccinated):
    #     deaths = 0
    #     for person in population:
    #         if person.is_alive == False:
    #             deaths += 1
    #         else:
    #             pass
    #     print(f'The total number of infected is {total_infected}')
    #     print(f'The total number of dead is {deaths}')

    #     log = open('log.txt', 'a')
    #     log.write(f'\nThe percentage of total infected: {total_infected/len(population) * 100}%')
    #     log.write(f'\nThe percentage of total dead: {deaths/len(population) * 100}%')
    #     log.close()

        
    #     ''' STRETCH CHALLENGE DETAILS:

    #     If you choose to extend this method, the format of the summary statistics logged
    #     are up to you.

    #     At minimum, it should contain:
    #         The number of people that were infected during this specific time step.
    #         The number of people that died on this specific time step.
    #         The total number of people infected in the population, including the newly infected
    #         The total number of dead, including those that died during this time step.

    #     The format of this log should be:
    #         "Time step {time_step_number} ended, beginning {time_step_number + 1}\n"
    #     '''
    #     # TODO: Finish this method. This method should log when a time step ends, and a
    #     # new one begins.
    #     # NOTE: Here is an opportunity for a stretch challenge!
        

#======================================================================================================

############################### Developer Notes ################################
##### Commands for the local terminal:
# exec(open('main.py').read())


############################### In-file Readme #################################
# - This is the entry script and is called from the command line to start the
#   game.
# - It imports and initializes the colorama module. The colorama module is used
#   to enable colored text outputs across different operating systems.
# - By importing the local iniPlayer script, the player class object is created
#   in that script. The player class object has to be isolated that way, to
#   both:
#    -- Share it with all other local scripts from the iniPlayer script
#    -- and let the object be created dynamically by the player (since he
#       chooses a class to play) at the same time. Creating the player class
#       beforehand in a "static" manner, would deprive the player of his own
#       choice what class to play.
# - This script then begins a chain of function calls that will ultimately loop
#   the program through all stages of the game. The startGame() function is the
#   first of that chain.


########### Making sure that this script is started using Python 3 #############
#! /usr/bin/python3                                                              # This tells the executing software, that Python 3 should be used to run the code


################################### Imports ####################################
##### Import neccessary modules
from colorama import init; init()                                                # Initialize to filter out ANSI escape sequences (see its module documentation)

##### Import local scripts
# MAIN_ = __import__('main')
INIP_ = __import__('iniPlayer')
# CONS_ = __import__('0_00_constants')
# DB_ = __import__('0_01_databases')
# CC_ = __import__('0_02_creatureClasses')
# UCLA_ = __import__('0_03_utilClasses')
# UFUN_ = __import__('0_04_utilFunctions')
# STOR_ = __import__('1_00_stories')
MENU_ = __import__('2_00_menu')
# BRID_ = __import__('2_01_bridge')
# SETT_ = __import__('3_00_settlement')
# EXPL_ = __import__('3_01_exploration')
# ENC_ = __import__('3_02_encounter')
# COMB_ = __import__('3_03_combat')

##### Import player Class object
# from iniPlayer import player


################################## Functions ###################################
##### Define main function starting the game loop
def main():
    MENU_.startGame()
    return


################################ Execute Code ##################################
##### Call main function to begin the game loop
main()

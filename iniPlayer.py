############################### Developer Notes ################################
##### Commands for the local terminal:
# exec(open('iniPlayer.py').read())


############################### In-file Readme #################################
# - This script imports ressources to be able to call the creation of the player
#   class object.
# - The reason for creating it in this isolated way is stated in the In-file
#   Readme of the main.py script.
# - The createPlayer() function asks the player what class he wants to play and
#   then creates it accordingly.


################################### Imports ####################################
##### Import neccessary modules
# none

##### Import local scripts
# MAIN_ = __import__('main')
# INIP_ = __import__('iniPlayer')
CONS_ = __import__('0_00_constants')
DB_ = __import__('0_01_databases')
CC_ = __import__('0_02_creatureClasses')
# UCLA_ = __import__('0_03_utilClasses')
# UFUN_ = __import__('0_04_utilFunctions')
# STOR_ = __import__('1_00_stories')
# MENU_ = __import__('2_00_menu')
# BRID_ = __import__('2_01_bridge')
# SETT_ = __import__('3_00_settlement')
# EXPL_ = __import__('3_01_exploration')
# ENC_ = __import__('3_02_encounter')
# COMB_ = __import__('3_03_combat')

##### Import player Class object
# from iniPlayer import player


################################## Functions ###################################
##### Define function used to choose and create the player class object          # Code like "{CONS_.cRed}" indicates a certain font style
def createPlayer():
    print('\n=============== Setting up Player Character ==============='
          '\nTo start the game, type in what class you want to play.')
    list__availClasses = [playerClass for playerClass in DB_.playerClassDB]      # Create a list of all player classes stored in the database
    while True:                                                                  # Loop until player input is valid
        print('\n               ..::||Available Classes||::..'
             f'\n                        < {CONS_.cRed}Warrior{CONS_.cResetAll} >')    # This print call has to be adjusted manually in case of player class additions
        chosenPlayerClass = input('\n                        > ').lower()
        if chosenPlayerClass in list__availClasses: break                        # End loop if chosen player class exists
        print("              Sorry, that class doesn't exist.")
    player = CC_.Player(chosenPlayerClass)                                       # Create chosen player class object
    print(f'                    You chose: {CONS_.cRed}{chosenPlayerClass}{CONS_.cResetAll}'
           '\n===========================================================')
    return player


################################## Execute #####################################
##### Create the player class object
player = createPlayer()                                                          # The player class object is stored in the variable "player"

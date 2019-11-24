############################### Developer Notes ################################
##### Commands for the local terminal:
# exec(open('2_01_bridge.py').read())


############################### In-file Readme #################################
# - This script bridges the program between stages of the game and is intended
#   for all transitional functionality.
# - The player is hereby given a choice to steer the game in a wanted direction.
#   To help his decision process, he is given relevant information about the
#   state of his player character.


################################### Imports ####################################
##### Import neccessary modules
# none

##### Import local scripts
# MAIN_ = __import__('main')
# INIP_ = __import__('iniPlayer')
# CONS_ = __import__('0_00_constants')
# DB_ = __import__('0_01_databases')
# CC_ = __import__('0_02_creatureClasses')
# UCLA_ = __import__('0_03_utilClasses')
# UFUN_ = __import__('0_04_utilFunctions')
# STOR_ = __import__('1_00_stories')
MENU_ = __import__('2_00_menu')
# BRID_ = __import__('2_01_bridge')
SETT_ = __import__('3_00_settlement')
# EXPL_ = __import__('3_01_exploration')
ENC_ = __import__('3_02_encounter')
# COMB_ = __import__('3_03_combat')

##### Import player Class object
from iniPlayer import player


################################## Functions ###################################
##### Define functions
#### Let player choose what to do next between stages of the game via input()
def adventureChoice():
    while True:
        print('\n\n................. Where do you want to go? ................'
              '\n[F]ight in the Wild | Search for an [I]nn | [Quit] the Game')   # Indicate valid commands with square brackets
        player.printStats()
        choice = input('\n                           > ').upper()                # Make sure inputs are uppercase to correctly check them
        if choice == 'F': ENC_.randFight1Group()
        elif choice == 'I': SETT_.inn()
        elif choice == 'QUIT': MENU_.endGame()
        else:
            print("              Sorry, that command doesn't exist. ")
            continue
    return

############################### Developer Notes ################################
##### Commands for the local terminal:
# exec(open('2_00_menu.py').read())


############################### In-file Readme #################################
# - This script contains a beginning and closing story as to not just throw the
#   player in and out of the game without context.
# - The player is also given a goal and will be informed about his performance
#   at the end of the game.


################################### Imports ####################################
##### Import neccessary modules
import sys

##### Import local scripts
# MAIN_ = __import__('main')
# INIP_ = __import__('iniPlayer')
CONS_ = __import__('0_00_constants')
# DB_ = __import__('0_01_databases')
# CC_ = __import__('0_02_creatureClasses')
# UCLA_ = __import__('0_03_utilClasses')
# UFUN_ = __import__('0_04_utilFunctions')
# STOR_ = __import__('1_00_stories')
# MENU_ = __import__('2_00_menu')
BRID_ = __import__('2_01_bridge')
# SETT_ = __import__('3_00_settlement')
# EXPL_ = __import__('3_01_exploration')
# ENC_ = __import__('3_02_encounter')
# COMB_ = __import__('3_03_combat')

##### Import player Class object
from iniPlayer import player


################################## Functions ###################################
##### Define functions
#### Tell the player a short backstory and give him a simple goal
def startGame():
    print('\n\n\n====================== Game started! ======================'
         f'\nAlright {CONS_.cGreen}{player.name}{CONS_.cResetAll}, you wake up in the middle of the road.'
          '\nYou have a sword in your hand and an empty purse on your belt.'
         f'\n\n               {CONS_.cMagenta}Make as much money as you can!{CONS_.cResetAll}'
          '\n\n-----------------------------------------------------------')
    BRID_.adventureChoice()
    return


#### Tease, present performance in relation to the goal and end kill the program
def endGame():
    print(f'\n                         {CONS_.cMagenta}You coward!{CONS_.cResetAll}'
           '\n\n-----------------------------------------------------------'
           '\n\nYou retire early and make due with all your aquired riches:'
          f'\nOn your journey, you accumulated a total of {CONS_.cCyan}{player.gold} gold{CONS_.cResetAll}.'
           '\nThis is the end of your story for now. Thank you for playing!'
           '\n\n======================= Game ended! =======================\n\n')
    sys.exit()                                                                   # Exit the program
    return

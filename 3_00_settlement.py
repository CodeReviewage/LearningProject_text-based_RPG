############################### Developer Notes ################################
##### Commands for the local terminal:
# exec(open('3_00_settlement.py').read())


############################### In-file Readme #################################
# - This scripts purpose is to hold all functions that deal with in-game content
#   that would happen inside a settlement (taverns, inns, shops, etc.).


################################### Imports ####################################
##### Import neccessary modules
# none

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
#### Give player context of his stay in the Inn and set his current HP to max HP
def inn():
    print(f'\n_________________________ {CONS_.cMagenta}The Inn{CONS_.cResetAll} _________________________'
         f'\n\nAfter you successfully searched for an Inn, you swiftly\n'
          'retire for the rest of the day.\n'
         f'Rising the next morning, {CONS_.cGreen}you feel completely refreshed{CONS_.cResetAll}.'
          '\n___________________________________________________________')
    player.currentHP = player.maxHP
    BRID_.adventureChoice()
    return

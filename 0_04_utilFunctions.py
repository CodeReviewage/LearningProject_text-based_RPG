############################### Developer Notes ################################
##### Commands for the local terminal:
# exec(open('0_04_utilFunctions.py').read())


############################### In-file Readme #################################
# - This script defines various functions that can be used across all local
#   scripts.
# - Commented out regions can contain code for future use.


################################### Imports ####################################
##### Import neccessary modules
import string
import random

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
# BRID_ = __import__('2_01_bridge')
# SETT_ = __import__('3_00_settlement')
# EXPL_ = __import__('3_01_exploration')
# ENC_ = __import__('3_02_encounter')
# COMB_ = __import__('3_03_combat')

##### Import player Class object
# from iniPlayer import player


################################### Utility ####################################
##### Define utility functions
#### Function to create random unique IDs for creature objects
def idGenerator(size=10, chars=string.ascii_uppercase + string.digits):          # IDs contain 10 characters by default consisting of uppercase ASCII characters and digits. The characters are chosen randomly.
    return ''.join(random.choice(chars) for _ in range(size))                    # Choose characters 10 times and join them together in a single string; then return them


####  Function to create a unique group label for a group of creature objects
def getGroupLabel():                                                             # Used in encounter.py to label created groups for the next encounter (so the program can better distinguish to what group a creature belongs)
    for letter in CONS_.upperAlpha:                                              # Loop over all uppercase letters
        if letter not in CONS_.usedLetters:                                      # Find a letter that was not yet used as a label
            CONS_.usedLetters.append(letter)                                     # Append the current letter to the list of used letters (since the current one will be used right now)
            return letter                                                        # Return the letter (to the group creating function in encounter.py)
    return                                                                       # Return nothing if no valid letter was found; this could lead to buggy names but there will most probably be no more than 26 groups + player group in one combat anyway

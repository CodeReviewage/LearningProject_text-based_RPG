############################### Developer Notes ################################
##### Commands for the local terminal:
# exec(open('0_00_constants.py').read())


############################### In-file Readme #################################
# - This script stores constants that are used across local scripts.
# - There are shortcut variables that will be used to change text
#   output behavior like colored fonts, colored backgrounds and the brightness
#   of the font.
# - Other constants and their purposes are explained throughout this script.


################################### Imports ####################################
##### Import neccessary modules
import string

##### Import local scripts
# MAIN_ = __import__('main')
# INIP_ = __import__('iniPlayer')
# CONS_ = __import__('0_00_constants')
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


############ Font Behavior for Outputs (using the colorama module) #############
##### Assign line-clear behavior
aReset = '\x1b[modeK'

##### Assign default font color and brightness behavior
cResetAll = '\x1b[0;49m'

##### Assign font color behavior
cBlack = '\x1b[30m'
cRed = '\x1b[31m'
cGreen = '\x1b[32m'
cYellow = '\x1b[33m'
cBlue = '\x1b[34m'
cMagenta = '\x1b[35m'
cCyan = '\x1b[36m'
cWhite = '\x1b[37m'
cReset = '\x1b[39m'

##### Assign background color behavior
bBlack = '\x1b[40m'
bRed = '\x1b[41m'
bGreen = '\x1b[42m'
bYellow = '\x1b[43m'
bBlue = '\x1b[44m'
bMagenta = '\x1b[45m'
bCyan = '\x1b[46m'
bWhite = '\x1b[47m'
bReset = '\x1b[49m'

##### Assign combinations of font and backround color behavior
cBlackbWhite = '\x1b[30;47m'



############################### Iterables & Co #################################
##### A list of all uppercase alphabetical characters of the english language
upperAlpha = list(string.ascii_uppercase)                                        # Used to create creature group labels in utilFunctions.py
usedLetters = []                                                                 # Used to memorize what letter was used the last time to label a creature group; it's not a constant but there is no better place to store it


##### List of valid NPC affiliations
validAffiliations = ['controlled', 'ally', 'enemy']


##### Faction IDs
playerFaction = 'ID_playerFaction'
neutralFaction = 'ID_neutralFaction'
monsterFaction = 'ID_monsterFaction'

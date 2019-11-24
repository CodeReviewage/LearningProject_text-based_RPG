############################### Developer Notes ################################
##### Commands for the local terminal:
# exec(open('0_01_databases.py').read())


############################### In-file Readme #################################
# - This script is a place for storing code to create player class objects and
#   NPC class objects.
# - More databases, for items for example, can be stored here as well to share
#   it across local scripts.
# - When adding to existing databases, make sure to adhere to the present
#   format, so other functions/methods/... can access the data correctly.


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
# MENU_ = __import__('2_00_menu')
# BRID_ = __import__('2_01_bridge')
# SETT_ = __import__('3_00_settlement')
# EXPL_ = __import__('3_01_exploration')
# ENC_ = __import__('3_02_encounter')
# COMB_ = __import__('3_03_combat')

##### Import player Class object
# from iniPlayer import player


########################### Player Classes Database ############################
##### Store data of available player classes
playerClassDB = {'warrior':     {'className':   'Warrior',
                                 'maxHP':       10,
                                 'attackDMG':   '1d3 + 2',
                                 'baseArmor':   1,
                                 'ini':         '1d20 + 1',
                                 'gold':        0,
                                 'skills':      {'Reckless Strike':     {'modDMG':          '2',     # An skill system ist not yet implemented but this can be used for inspiration
                                                                         'statusEffect':    ['modArmor', '-2', 1]}}}}



############################## NPC Type Database ###############################
##### Store data of available NPC types
NPC_DB =    {'skeleton':        {'type':        'Skeleton',
                                 'maxHP':       6,
                                 'attackDMG':   '1d2 + 1',
                                 'baseArmor':   0,
                                 'ini':         '1d20 + 5',
                                 'gold':        '1d2',
                                 'skills':      {}},

             'boar':            {'type':        'Boar',
                                 'maxHP':       9,
                                 'attackDMG':   '1d3 + 1',
                                 'baseArmor':   1,
                                 'ini':         '1d20 + 2',
                                 'gold':        '1d3 + 1',
                                 'skills':      {}}}




################################ Item Database ################################# # None of these are implemented yet, but let it stand for future additions
##### Store data of available items
item_DB = {'weapon':    {'sword':           {'name':    'Sword',
                                             'DMG':     '1d8'},
                         'mace':            {'name':    'Mace',
                                             'DMG':     '1d6'}},

           'armor':     {'leather armor':   {'name':    'Leather Armor',
                                             'armor':   1}}}

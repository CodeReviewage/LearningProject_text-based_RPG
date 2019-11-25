############################### Developer Notes ################################
##### Commands for the local terminal:
## exec(open('3_02_encounter.py').read())

# from colorama import init; init()
# g1 = createNPC_group([['random', 3]], affiliation='ally'); g2 = createNPC_group([['random', 4]], affiliation='enemy'); COMB_.combat(player.playerGroup, g1, g2)


############################### In-file Readme #################################
# - This script holds functions that deal with preparing and initializing
#   encounters like combats and more.
# - There is a function to create NPC groups and a quick fight function.


################################### Imports ####################################
##### Import neccessary modules
import random

##### Import local scripts
# MAIN_ = __import__('main')
# INIP_ = __import__('iniPlayer')
CONS_ = __import__('0_00_constants')
DB_ = __import__('0_01_databases')
CC_ = __import__('0_02_creatureClasses')
# UCLA_ = __import__('0_03_utilClasses')
UFUN_ = __import__('0_04_utilFunctions')
# STOR_ = __import__('1_00_stories')
# MENU_ = __import__('2_00_menu')
# BRID_ = __import__('2_01_bridge')
# SETT_ = __import__('3_00_settlement')
# EXPL_ = __import__('3_01_exploration')
# ENC_ = __import__('3_02_encounter')
COMB_ = __import__('3_03_combat')

##### Import player Class object
from iniPlayer import player


################################## Functions ###################################
##### Define functions
#### Creates a group of NPCs as specified by input arguments
def createNPC_group(groupTemplate=[['random', 1]], faction=CONS_.monsterFaction,  affiliation='enemy'):     # INPUT e.g.: "[['Skeleton', 2], ['Boar', 1]]" would create 1 group with the according NPC types and number of NPCs of those types; the optional arguments default to the standard use of creating combat enemies
    if affiliation not in CONS_.validAffiliations:                               # Raise an error if the affiliation argument is not poart of valid affiliations accoring to the list in constants.py
        raise NameError('Invalid affiliation!')
    NPC_group = []                                                               # Create empty list that will be filled with individual groups of NPC class objects
    groupId = UFUN_.idGenerator()                                                # Create an ID for the group of NPCs, to prevent NPCs to target allied NPCs in combat; also for identification purposes
    for NPC_type, number in groupTemplate:                                       # Loop over individual NPC types and the number that tells the script how many of that type are to be created
        for i in range(number):                                                  # Loop a number of times according to the number of NPCs to create of a specified type
            if NPC_type == 'random':                                             # Choose a random NPC type in the database if the input type is 'random'
                NPC_type = random.choice(list(DB_.NPC_DB.keys()))
            # else:                                                              # Otherwise the input NPC type is the actual NPC type to be created
            #     NPC_type = NPC
            newNPC = CC_.NPC(NPC_type, faction, affiliation, groupId, player)    # Create the NPC class object providing its intended type, the faction, affiliation, the group ID of the current group and the player class object (the latter is used for the checkPlayerControl() function)
            newNPC.combatName = (NPC_type.capitalize() + '_'                     # Form the combat name of the just created NPC object (type + group label + NPC number of the current type)
                                 + UFUN_.getGroupLabel() + '_' + str(i + 1))     # UFUN_.getGroupLabel() returns an uppercase letter that was not used to label groups yet; inserted in the combatName, it enables the player to distinguish to what group a NPC belongs and to prevent identical NPC combat names
            NPC_group.append(newNPC)                                             # Append the new NPC to the NPC group list that was created in the beginning
    return NPC_group                                                             # OUTPUT e.g.: "[NPC_class_object_1, NPC_class_object_2, ...]"; return the NPC group


#### Will put player group against one enemy NPC group into combat
def randFight1Group(numEnemies=1, sameType=True):                                # Optionally apecify the number of NPCs and if there is more than one; also optionally specify if all of those NPCs should be of the same type or not
    if sameType == True:                                                         # Create a number of NPCs of the same type if specified so
        NPC_group = createNPC_group([['random', numEnemies]])                    # Call createNPC_group() with the neccesary arguments and return the created NPC group
    else:                                                                        # Create a number of NPCs of randomly determined types if specified so
        NPC_group = createNPC_group([['random', 1]] * numEnemies)                # Call createNPC_group() with the neccesary arguments and return the created NPC group
    playerGroup = player.playerGroup                                             # Create a variable for the player group
    COMB_.combat(playerGroup, NPC_group)                                   # OUTPUT e.g.: "[player_class_obect, controlled_NPC_class_object], [enemy_NPC_class_object_1, enemy_NPC_class_object_2]", call the combat() function with both created groups as arguments to start their combat
    return

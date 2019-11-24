############################### Developer Notes ################################
##### Commands for the local terminal:
## exec(open('3_03_combat.py').read())


############################### In-file Readme #################################
# - This script handles pretty much all combat mechanics and its conclusion
#   (looting etc.).
# - The combat is separated into rounds and every round goes through the same
#   motions.
# - Turns for player controlled creatures and turns for not player controlled
#   creatures are held separate.
# - At the end of the round there are checks for slain creatures and instances
#   of victory/defeat conditions. Those latter conditions can be extended and
#   are checked separate because of those possible extensions.
# - There are a couple of text outputs to the console to let the player know
#   whats happening.


################################### Imports ####################################
##### Import neccessary modules
import random

##### Import local scripts
# MAIN_ = __import__('main')
# INIP_ = __import__('iniPlayer')
CONS_ = __import__('0_00_constants')
# DB_ = __import__('0_01_databases')
# CC_ = __import__('0_02_creatureClasses')
UCLA_ = __import__('0_03_utilClasses')
# UFUN_ = __import__('0_04_utilFunctions')
# STOR_ = __import__('1_00_stories')
# MENU_ = __import__('2_00_menu')
BRID_ = __import__('2_01_bridge')
# SETT_ = __import__('3_00_settlement')
# EXPL_ = __import__('3_01_exploration')
ENC_ = __import__('3_02_encounter')
# COMB_ = __import__('3_03_combat')

##### Import player Class object
from iniPlayer import player


################################## Functions ###################################
##### Define Functions
#### Put the player group and all other supplied/input groups into combat
def combat(*groups):                                                             # INPUT e.g.: "[creature_object_1_of_group_A, creature_object_1_of_group_A], [creature_object_1_of_group_B]"; the combating groups are passed as separate arguments
    print('\n            You have come across some enemies...'                   # Text output to inform the player
          '\n\n\n==========================================================='
          '\n====================== Combat begins! =====================')
    global combatTracker                                                         # Declare the following class object as a global variable so it can be accesed by all functions in ths script
    combatTracker = UCLA_.EncounterTracker(groups)                               # Create the combatTracker class object to manage combat development; pass all the combat groups as they were input
    numRound = 0                                                                 # Create a counter for every combat round (for output purposes benefiting the player)
    while True:                                                                  # Loop over rounds until combat is concluded
        numRound += 1                                                            # Advance round counter every new round
        print(f'\n_________________________ Round: {numRound} ________________________')    # Ouput for a clear overview
        iniOrder = combatTracker.rollInitiative()                                # Create the initiative order
        printIniOrder(iniOrder)                                                  # Call the function to print the initiative order in a clearly formatted fashion for the player
        for combatant in iniOrder:                                               # Loop over every combatant in the initiative order (the order only includes combatants that are still fighting/not dead, fled, ...)
            print('-----------------------------------------------------------') # Ouput for a clear overview
            if combatant in player.playerGroup:                                  # Check if the current combatant is controlled by the player
                playerTurn(combatant)                                            # If the combatant is controlled by the player, call the player turn so the player can choose actions for this combatant
            else:                                                                # If the combatant is not controlled by the player, let the (not player controlled) NPC decide its actions for itself
                NPC_turn(combatant)
            combatTracker.checkTurnDeaths(combatant)                             # After every combatants turn, check if the combatant or its target died (keeping track of those developments)
            combatTracker.updateState()                                          # After every combatants turn, update the combatTracker by managing what creatures have died, fled etc. and create a new initiative order for still active combatants (see utilClasses.py and what it does in detail)
            checkDefeatOrVictory()                                               # After every combatants turn, check if a win or defeat condition has been met (reference the function to see how exactly)
        print('-----------------------------------------------------------')     # Ouput for a clear overview
    return


#### Output the current initiative order in a clear format for the player
def printIniOrder(iniOrder):                                                     # INPUT e.g.: "[creature_object_1_with highest_iniValue, creature_object_2_with_second_highest_iniValue, ...]"; input the current initiative order
    msg = 'Initiative order:'                                                    # First part of the message
    for combatant in iniOrder:                                                   # Loop over every combatant in the initiative order
        if combatant.affiliation in ['controlled', 'ally']:                      # If the combatant is player-controlled or an uncontrolled ally, use the appropiate color coding in the output message
            msg += (f' | {CONS_.cGreen}{combatant.combatName}{CONS_.cResetAll}'  # Add this string to the first part of the message
                    f': {combatant.iniValue}')
        else:                                                                    # If the combatant is an enemy, use the appropiate color coding in the output message
            msg += (f' | {CONS_.cRed}{combatant.combatName}{CONS_.cResetAll}'    # Add this string to the first part of the message
                    f': {combatant.iniValue}')
    print(msg + '\n')                                                            # Add a newline command to the end of the message and print it as text output for the player
    return


#### Let the player decide combat actions for controlled creatures
def playerTurn(combatant):                                                       # Function takes a combatant object as input
    if combatant.target == None or combatant.target.dead == True:                # Check if the combatant has currently no target or if his target is flagged as dead; in this case, he needs a new target and since the player shouldn't have to choose a target every turn, a valid target will be chosen for him
        while True:                                                              # Loop until a valid target was found
            randTarget = random.choice(combatTracker.iniOrder)                   # Choose a random target from the initiative order (since it includes all currently participating creatures)
            if randTarget.affiliation not in ['controlled', 'ally']:             # Use chosen target if it's not an an ally
                combatant.target = randTarget                                    # Set the current random choice as the combatant's new target
                break                                                            # Break out of the loop to continue further with the player's turn; this will not happen if the randomly chosen target is invalid

    while True:                                                                  # Loop until a valid combat action has been chosen by the player
        combatant.printStats()                                                   # Inform the player of the controlled combatants relevant stats, so he can choose an appropiate action
        action = input('Choose an action: ([A]ttack): > ').lower()               # Prompt the player to choose an action; this text output has to be adjusted manually if new combat actions are implemented
        if action not in combatant.combatOptions:                                # Restart the loop if the player's input is not valid
            continue                                                             # Begin the loop from the top again
        # elif action == 't':                                                    # This code snippet is for the future mechanic of letting the player choose the target manually
        #     print(f'Available targets: {}')
        #     target = input('Choose a target: > ').lower()
        #     combatant.object.setTarget(target)
        elif action == 'a':                                                      # If the [A]ttack action was chosen, perform an attack
            combatant.attack()                                                   # Call the attack function of the combatant object
        break                                                                    # Break out of the loop once a valid action has been performed
    return


#### Let the NPC (not controlled by the player) decide its combat acions
def NPC_turn(combatant):                                                         # Function takes a combatant object as input
    if combatant.target == None or combatant.target.dead == True:                # This automatic targeting mechanic is the same as in playerTurn(), so reference that function; only differences from playerTurn() will be explained via comments
        while True:
            randTarget = random.choice(combatTracker.iniOrder)
            if ((combatant.affiliation == 'ally' and randTarget.affiliation in ['enemy']) or     # Check if the randomly chosen target has a valid affiliation in relation to the current combatant; the two coded constellations are valid
               (combatant.affiliation == 'enemy' and randTarget.affiliation in ['controlled', 'ally'])):
                combatant.target = randTarget
                break
    combatant.attack()                                                           # After a valid target has been ensure, always attack the target of the current combatant
    return


#### Check if any victory or defeat condition is met
def checkDefeatOrVictory():                                                      # This function is a wrapper for all relevant conditions that have to be checked
    checkDefeat_playerGroupDeath()                                               # Check if the player group was defeated due to all player controlled creatures being dead; the case of all player-controlled creatures dead but other allies alive is not accounted for yet
    checkVictory_allEnemiesDefeated()                                            # Check if the player was victorious due to all enemy NPCs being dead
    return


#### Check if player group was defeated due to all player-controlled creatures being dead
def checkDefeat_playerGroupDeath():
    for combatant in combatTracker.playerGroup:                                  # Loop over all player-controlled creature objects
        if combatant.dead == False:                                              # Check if the current (player-controlled) creature is NOT dead
            return                                                               # Break out of the function without triggering a defeat
    defeat()                                                                     # If all player controlled creatures are dead, the loop above will run out without returning from checkDefeat_playerGroupDeath() and instread call defeat()
    return


#### Go through the defeat sequence
def defeat():
    for combatant in combatTracker.allCreatures:                                 # Loop over every combatant that was originally in the fight
        combatant.target = None                                                  # Set the current combatants target to None
    for combatant in combatTracker.playerGroup:                                  # Loop over every combatant that is player controlled; the following code resets the creature object's attributes for the next combat
        combatant.gold = 0                                                       # Set the current player-controlled combatant's gold to zero since he is looted by the enemies
        combatant.currentHP = combatant.maxHP                                    # Set HP to the max for all objects in the player group, so the adventuring can continue
        combatant.dead = False                                                   # Set the "dead" flag of objects in the player group to False
        combatant.fled = False                                                   # Set the "fled" flag of objects in the player group to False
    print(f'\n\n_________________________ {CONS_.cRed}DEFEAT{CONS_.cResetAll} __________________________'     # Inform the player of his defeat and the consequences
          f'\n{CONS_.cRed}You lose conciousness and nobody is there to help{CONS_.cResetAll}...'
          f'\nWhen you wake up, {CONS_.cRed}all your gold is gone{CONS_.cResetAll} '
          f'{CONS_.cGreen}but you feel completely refreshed{CONS_.cResetAll}.'
          f'\nYou now have a total of {CONS_.cCyan}{player.gold} gold{CONS_.cResetAll}.'
           '\n\n======================= Combat over! ======================'     # Declare the combat to be over
           '\n===========================================================')
    CONS_.usedLetters = []                                                       # Empty the list this variable holds, so the function UFUN_.getGroupLabel() wont run out of letters that encounter.py uses to label groups with
    BRID_.adventureChoice()                                                      # Leave the combat sequence and let the player again choose what to do next in his adventure
    return


#### Check if the player was victorious due to all enemy NPCs being dead
def checkVictory_allEnemiesDefeated():
    for group in combatTracker.enemyGroups:                                      # Loop over every group that is an enemy to the player
        for combatant in group:                                                  # Loop over every creature object individually in the current enemy group
            if (combatant.dead == False and combatant.fled == False):            # Check if the current combatant is NOT dead and did NOT flee
                return                                                           # Break out of the function without triggering a victory (since a non dead and not fled enemy implies that the combat is not yet over)
    victory()                                                                    # If all enemy NPCs are dead or have fled, call the victory() function
    return


#### Initiate victory sequence of events
def victory():
    for combatant in combatTracker.allCreatures:                                 # Loop over every combatant that was originally in the fight
        combatant.target = None                                                  # Set the current combatant's target to None before another fight starts (an old target would missdirect combat actions)
        combatant.fled = False                                                   # Set the "fled" flag of the current object to False
    print(f'\n\n_________________________ {CONS_.cGreen}VICTORY{CONS_.cResetAll} _________________________'     # Inform player of victory
          f'\nAll enemies are slain.')
    lootSlainEnemies()                                                           # Call for the function that lets the player loot all defeated enemies
    CONS_.usedLetters = []                                                       # Empty the list this variable holds, so the function UFUN_.getGroupLabel() wont run out of letters that encounter.py uses to label groups with
    BRID_.adventureChoice()                                                      # After looting is done, leave the combat sequence and let the player again choose what to do next in his adventure
    return


#### Looting sequence after a victory
def lootSlainEnemies():
    lootedGold = 0                                                               # Create a variable to store gold of individually looted creatures
    for group in combatTracker.enemyGroups:                                      # Loop over every group that is an enemy to the player
        for combatant in group:                                                  # Loop over every creature object individually in the current enemy group
            if (combatant.dead == False or combatant.fled == True):              # Skip over a current combatant if he is not dead and/or has fled; you could decide to let the player loot former allies as well...
                continue
            else:                                                                # If the current combatant is dead and has not fled, roll for his gold to be looted (by calling the corresponding class function of that NPCs object) and add it to the variable that accumulates the looted gold
                lootedGold += combatant.beLooted()
    player.gold += lootedGold                                                    # After every combatant was looped over, add the total looted gold to the player's inventory
    print(f'You search every slain enemy and find {CONS_.cYellow}{lootedGold} gold{CONS_.cResetAll}.'     # Inform the player of the looting result and declare the combat to be over
           '\n\n======================= Combat over! ======================'
           '\n===========================================================')
    return

############################### Developer Notes ################################
##### Commands for the local terminal:
# exec(open('0_03_utilClasses.py').read())


############################### In-file Readme #################################
# - This scrips defines the Encounter Tracker class object. It is used to
#   manage an encounter and keep track of encounter developments like
#   initiative, deaths etc.
# - Such a class has to be created for every encounter and must be supplied with
#   all patricipating groups. The input is a list of those groups.
# - The class organizes the combatants in several groups in order to help
#   determine what each creature objects's role and status is.
# - Things that are kept track of are:
#    -- participating creatures & their group affiliations
#    -- initiative order & each creature's status (dead, ...)
#    -- which creatures die after every turn
# - The information is always kept up to date (the class functions have to be
#   called accordingly).
# - There is also some text ouptut to inform the player of deaths and who killed
#   who.


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
# BRID_ = __import__('2_01_bridge')
# SETT_ = __import__('3_00_settlement')
# EXPL_ = __import__('3_01_exploration')
# ENC_ = __import__('3_02_encounter')
# COMB_ = __import__('3_03_combat')

##### Import player Class object
from iniPlayer import player


################################### Classes ####################################
##### Define encounter tracker class to help manage every encounter
class EncounterTracker:
    #### Define constructor
    def __init__(self, groups):                                                  # Input groups as a list of lists of individual groups: [['playerGroupObject_1', 'playerGroupObject_2'], ['creatureGroup_A_object_1'], ['creatureGroup_B_object_1', 'creatureGroup_B_object_2']]
        ### Assign combatants to their respective groups
        self.groups = groups                                                     # Store what groups are paricipating
        self.playerGroup = []                                                    # Creature objects that are player-controlled
        self.allyGroups = []                                                     # Creature objects that are allied with the player group but not player-controlled
        self.enemyGroups = []                                                    # Creature objects that are enemies to the player; note that this attribute is a list of lists (every list inhabits enemies with the same group ID)
        self.allCreatures = []                                                   # An unpacked list of all creature objects participating in the encounter
        self.initGroups()                                                        # Function to fill the aforementioned groups

        ### Manage initiative and creature status
        self.iniOrder = self.allCreatures.copy()                                 # Tracks currently active combatants and orders them accoridng to their initiative value (highest first)
        self.deadCreatures = []                                                  # Currently dead/unconscious creatures
        self.fledCreatures = []                                                  # Currently fled creatures
        self.updateState()                                                       # Function to get the current state of initiative and creature statuses



    #### Define class functions
    ### All functions
    ## Function to populate the different group attributes
    def initGroups(self):
        for group in self.groups:
            if group[0] in player.playerGroup:                                   # Add group to self.playerGroup if the first object of the looped group is part of the player group stored in the Player class (every looped group inhabits only creatures of the same group; that is how the input this Encounter Tracker class works)
                self.playerGroup = group
            elif group[0].affiliation == 'ally':                                 # Add group to self.allyGroups if the first objects has the 'ally' affiliation
                self.allyGroups.append(group)
            else:                                                                # All other groups are enemies
                self.enemyGroups.append(group)
            for creature in group:                                               # Unpack the current group and add its objects to self.allCreatures individually
                self.allCreatures.append(creature)
        return


    ## Update the population of iniOrder, deadCreatures & fledCreatures
    def updateState(self):
        for creature in self.allCreatures:                                       # Check all creatures
            # Check for dead status and adjust flags, deadCreatures & iniOrder
            if creature.currentHP <= 0:
                creature.dead == True
                if creature not in self.deadCreatures: self.deadCreatures.append(creature)     # Add creature only if it's not already in deadCreatures
                if creature in self.iniOrder: self.iniOrder.remove(creature)     # Remove creature only if it's already in iniOrder
            elif creature.currentHP > 0:
                creature.dead == False
                if creature in self.deadCreatures: self.deadCreatures.remove(creature)      # Remove creature only if it's already in deadCreatures
                if creature not in self.iniOrder: self.iniOrder.append(creature) # Add creature only if it's not already in iniOrder
            # Check fled creatures and adjust fledCreatures
            if creature.fled == True and creature not in self.fledCreatures:     # Add creature only if it's not already in fledCreatures
                self.fledCreatures.append(creature)
            elif creature.fled == False and creature in self.fledCreatures:      # Remove creature only if it's already in fledCreatures
                self.fledCreatures.remove(creature)
        return

    ## Determine new initative order
    def rollInitiative(self):
        for creature in self.iniOrder:                                           # Loop over every active combatant (this function has to be called after updateStat() since the iniOrder should only inhabit active combatants)
            creature.initiative()                                                # Roll initiative for current creature
        self.iniOrder.sort(key=lambda x: x.iniValue, reverse=True)               # Sort the list of objects according to each object's iniValue; begin with the highest value
        return self.iniOrder                                                     # Return the initiative order


    ## Check if the input combatant or its target has died
    def checkTurnDeaths(self, combatant):                                        # Function has to be called after every creatures turn in an encounter
        if combatant.currentHP <= 0:                                             # Check whether the combatant's HP is zero or below
            combatant.dead = True                                                # Set dead-flag to True if the combatant is dead (could happen if DMG is reflected etc.)
            print(f'{CONS_.cCyan}{combatant.combatName}{CONS_.cResetAll} was slain.')     # Inform player per text output
        if combatant.target.currentHP <= 0:                                      # Check if combatant's target is dead
            combatant.target.dead = True                                         # Set dead-flag to True if the combatant's target is dead
            print(f'{CONS_.cCyan}{combatant.target.combatName}{CONS_.cResetAll} was slain.')     # Inform player per text output
        return

############################### Developer Notes ################################
##### Commands for the local terminal:
# exec(open('0_02_creatureClasses.py').read())


############################### In-file Readme #################################
# - This script first defines the player class object. It is only used for
#   creating the playable class for the human player. Not for any kind of NPC.
#   If NPCs using the player class templates are necessary, a separate class
#   should be defined since some attributes and functions in this class are only
#   of use to interact with the human player.
# - Most values like damage to a creature are rolled like dice. The rolldice
#   module enables to determine values by assigning strings that describe dice
#   types, dice number and flat bonus values.
#    -- E.g.: "1d4 + 1" would be randomly evalued like rolling a four-sided die
#       and then adding 1 to the result.
# - Some class attributes are derived from the player class database, others are
#   defined explicitly.
#    -- Identification attributes allow the program to check of what kind a
#       class object is. That is especially usefull in combat situations to
#       determine valid targets for attacks for example. Uses outside of combat
#       are possible as well.
#    -- All attributes can be changed by the program throughout the game.
# - The class functions state their use in their documentation below.
# - Commented out regions can contain code for future features.

# - The second class defines the NPC class object. It is primarily used to
#   create NPCs to fight against. Other use cases are possible of course.
# - The class works very much alike the player class. Differences will be
#   self-explanatory once you go through this script.


################################### Imports ####################################
##### Import neccessary modules
from rolldice import roll_dice as roll                                           # A module to enable dice rolling (as an alternative to other random determinations)

##### Import local scripts
# MAIN_ = __import__('main')
# INIP_ = __import__('iniPlayer')
CONS_ = __import__('0_00_constants')
DB_ = __import__('0_01_databases')
# CC_ = __import__('0_02_creatureClasses')
# UCLA_ = __import__('0_03_utilClasses')
UFUN_ = __import__('0_04_utilFunctions')
# STOR_ = __import__('1_00_stories')
# MENU_ = __import__('2_00_menu')
# BRID_ = __import__('2_01_bridge')
# SETT_ = __import__('3_00_settlement')
# EXPL_ = __import__('3_01_exploration')
# ENC_ = __import__('3_02_encounter')
# COMB_ = __import__('3_03_combat')

##### Import player Class object
# from iniPlayer import player


################################# Player Class #################################
##### Define player class
class Player:
    #### Define constructor
    def __init__(self, playerClassName):
        ### Assign class attributes
        ## Get base stats from player classes database
        self.playerStats = DB_.playerClassDB[playerClassName]

        ## Stats attributes
        self.maxHP = self.playerStats['maxHP']
        self.currentHP = self.maxHP
        self.baseArmor = self.playerStats['baseArmor']                           # Value will be substracted from incoming damage
        self.attackDMG = self.playerStats['attackDMG']                           # Should later correspond to weapon damage
        self.extraDMG = '0'                                                      # Should later be used to add damage bonuses from various sources
        self.ini = self.playerStats['ini']                                       # Initiative stat, the higher the more likely to act first in an encounter
        self.extraIni = '0'                                                      # Should later be used to add initiative bonuses from various sources

        ## Inventar & Equipment attributes
        self.gold = self.playerStats['gold']                                     # Keeping track of gold amount acquired

        ## Identification attributes
        self.name = 'Human Player'                                               # Name of the character; should later on be determined by player input
        self.className = self.playerStats['className']                           # Name of the class the player is playing
        self.combatName = self.name                                              # Name inside combat for a more consice text outout
        self.affiliation = 'controlled'                                          # Informs about the relationship towards the human player
        self.groupId = UFUN_.idGenerator()                                       # Can be used to determine another level of affiliation with another object
        self.faction = CONS_.playerFaction                                       # Simple identification purpose; in the future part of a more fleshed out faction feature
        self.ID = UFUN_.idGenerator()                                            # Used to identify a player class object; also for future functionality to save progress of playing the game
        self.playerGroup = [self]                                                # Used to store controllable NPC objects; for future saveing functionality

        ## Combat attributes
        self.iniValue = None                                                     # Determined initiative value in a round of an encounter
        self.target = None                                                       # Current target for attacks etc.
        self.combatOptions = ['a']                                               # List to check valid player input() for combat actions; should be stored in the player class database...

        ## Flag attributes
        self.dead = False                                                        # Used to indicate if this object is at 0 HP or less and unconscious/dead
        self.fled = False                                                        # Used to indicate if this object has fled an encounter; not really used but Fleeing system is almost implemented and at this point its necessary to not crash the program

        ## Attributes for future use
        # self.skills = self.playerStats['skills']                               # List of available skills
        # self.statusEffects = []                                                # List of active status effects like being poisoned etc.



    #### Define class functions
    ### General functions
    ## Output stats of interest for the player
    def printStats(self):                                                        # Output HP, armor, DMG, Initiative-roll and current gold
        msg = (f'HP: {self.currentHP}/{self.maxHP} | Armor: {self.baseArmor} | '
               f'DMG: {self.attackDMG} | Initiative: {self.ini} | Gold: {self.gold}')
        print(msg)
        return


    ## Determining the initiative value for combat and non-combat encounters
    def initiative(self):
        self.iniValue = roll(self.ini)[0] + roll(self.extraIni)[0]
        return


    ### Combat Functions
    ## Setting a target for attacks etc.
    def setTarget(self, target):
        self.target = target
        return


    ## Execute standard attack and output the result
    def attack(self):
        DMG = roll(self.attackDMG)[0] + roll(self.extraDMG)[0]
        self.target.currentHP -= DMG                                             # Substract DMG from target object immediately
        msg = (f'{CONS_.cGreen}{self.combatName}{CONS_.cResetAll}: Attacking '
               f'{CONS_.cRed}{self.target.combatName}{CONS_.cResetAll} for '
               f'{CONS_.cYellow}{DMG} damage{CONS_.cResetAll}.')
        print(msg)
        return


    ### Class functions for future use (under construction!)
    ## Using a skill
    # def useSkill(self, skillname):
    #     DMG = self.rollAttackDMG()[1] + roll(self.skills[skillname]['modDMG'])[0]
    #     self.statusEffects.append(self.skills[skillname]['statusEffect'])
    #     msg = (f'{cGreen}You{cResetAll} recklessly attack the enemy for {cRed}{DMG}{cResetAll} damage,\n'
    #             'but forgo any defensive bonuses until the end of your next turn.')
    #     return (msg, DMG)


    ## Reseting stats to base values
    # def resetStat(self):   # call this after every round!
    #     statusEffectsDel = []
    #     for i in range(0, len(self.statusEffects)):
    #         self.statusEffects[i][2] -= 1
    #         if self.statusEffects[i][2] <= 0:
    #             statusEffectsDel.append(i)
    #     for i in statusEffectsDel.sort(reverse=True):
    #         del self.statusEffects[i]
    #     return



################################## NPC Class ###################################
##### Define NPC class
class NPC:                                                                       # See Player Class for reference when trying to understand this class
    #### Define constructor
    def __init__(self, NPC_type, faction, affiliation, groupId):
        ### Assign class attributes
        ## Get base stats from NPC type database
        self.NPC_stats = DB_.NPC_DB[NPC_type]

        ## Stats attributes
        self.maxHP = self.NPC_stats['maxHP']
        self.currentHP = self.maxHP
        self.baseArmor = self.NPC_stats['baseArmor']
        self.attackDMG = self.NPC_stats['attackDMG']
        self.extraDMG = '0'
        self.ini = self.NPC_stats['ini']
        self.extraIni = '0'

        ## Inventar & Equipment attributes
        self.gold = self.NPC_stats['gold']

        ## Identification attributes
        self.type = self.NPC_stats['type']
        self.combatName = None
        self.affiliation = affiliation
        self.faction = faction
        self.groupId = groupId
        self.ID = UFUN_.idGenerator()
        self.checkPlayerControl()                                                # Check if the created NPC is part of the player's group; in the future, NPCs can join or leave the player's group arbitrarily


        ## Combat attributes
        self.iniValue = None
        self.target = None
        self.combatOptions = ['a']

        ## Flag attributes
        self.dead = False
        self.fled = False                                                        # Indicates if the NPC class object has fled the current combat

        ## Attributes for later use
        # self.skills = self.NPC_stats['skills']



    #### Define class functions
    ### General Functions
    ## Output stats of interest for the player
    def printStats(self):                                                        # Output HP, armor, DMG, Initiative-roll and current gold
        msg = (f'HP: {self.currentHP}/{self.maxHP} | Armor: {self.baseArmor} | '
               f'DMG: {self.attackDMG} | Initiative: {self.ini} | Gold: {self.gold}')
        print(msg)
        return


    ## Determining the initiative value in combat and non-combat encounters
    def initiative(self):
        self.iniValue = roll(self.ini)[0] + roll(self.extraIni)[0]
        return


    ### Combat Functions
    ## Setting a target for attacks etc.
    def setTarget(self, target):
        self.target = target
        return


    ## Standard attack
    def attack(self):
        DMG = roll(self.attackDMG)[0] + roll(self.extraDMG)[0]
        self.target.currentHP -= DMG
        if self.affiliation in ['controlled', 'ally']:                           # Use the appropiate color coding depending on whether the object is allied with the player or not
            msg = (f'{CONS_.cGreen}{self.combatName}{CONS_.cResetAll}: Attacking '
                   f'{CONS_.cRed}{self.target.combatName}{CONS_.cResetAll} for '
                   f'{CONS_.cYellow}{DMG} damage{CONS_.cResetAll}.')
        else:
            msg = (f'{CONS_.cRed}{self.combatName}{CONS_.cResetAll}: Attacking '
                   f'{CONS_.cGreen}{self.target.combatName}{CONS_.cResetAll} for '
                   f'{CONS_.cYellow}{DMG} damage{CONS_.cResetAll}.')
        print(msg)
        return


    ## Determine loot given once this object is slain
    def beLooted(self):
        gold = roll(self.gold)[0]
        return gold


    ### Class functions for future use (under construction!)
    ## Check if this NPC is under player control and add to player group if so
    # def checkPlayerControl(self):
    #     if self.affiliation == 'controlled':
    #         player.playerGroup.append(self)
    #         self.groupId = player.groupId
    #     return


    ## Chooses an action to perform in combat (not finished)
    # def chooseAction(self):
    #     possibleActions = []
    #     .....


    ## Using a skill
    # def useSkill(self, skillname):
    #     DMG = self.rollAttackDMG()[1] + roll(self.skills[skillname]['modDMG'])[0]
    #     msg = f'The {cYellow}{self.name}{cResetAll} attacks you for {cRed}{DMG}{cResetAll} damage with a poisonous bite.'
    #     return (msg, DMG)

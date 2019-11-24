# A text-based RPG
This is a text-based RPG written in Python 3.7.3.

The motivation behind this project is primarily to apply coding knowledge of Python while learning it.
The game itself is not really supposed to be extraordinarily fun. Instead, the underlying code should
form a good basis so that future features to the game can be implemented with ease.
There is also an attempt to form good coding habits and a clear documentation.




## How to run the Game
### Dependencies
This section mentions what Python version and exact modules are needed to run this code.
Other versions of software may or may not break the code.

- Programming Language and modules of its standard library
    - Python 3.7.3
    - sys
    - string
    - random

- Third party modules
    - colorama 0.4.1
    - py-rolldice 0.3.9
    - regex 2019.11.1 (since it is a dependency of py-rolldice)

- The game was tested only on Windows 7 (64-Bit)


### Step-by-step running the Game
1. Download the files and put them all into one folder
2. Open a terminal of your choice:
    - Windows command line
    - Your IDE environment (e.g. 'Atom 1.41.0' with the 'platformio-ide-terminal 2.10.0' package, ...)
    - ...
    - DO NOT USE Python's IDLE (the game will run but the text output will look horrible since font styles won't be executed)
3. Navigate to the game folder
4. Run 'main.py'
5. Play the game



## Features
### Current Game Features
- Choosing a player class (Warrior)
- Fights with monsters (Goblins or Spiders)
- Looting gold
- Inn mechanic to replenish health
- Very short story elements
- No linear adventuring


### Current Code Features
- Invalid commands don't break the program
- Formatted output with colors
- New player classes and NPCs can easily be added
- Player and NPC class mechanics & attributes can be added
- Player chooses course of the game
- Creation of monsters
    - Groups can be created and will act as simple allies to themselves in combat
    - Number and type can be chosen or random
- Initiative System
- Automatic targeting system in combat
- Quit mechanic


## Code Related Documentation
### How to read documentation in the files themselves
When  reading through the documentation to the scripts to understand how they
operate, read "In-file Readmes" at the top of every script first. That should
be done in the following order:

main.py >> iniPlayer.py >> constants.py >> databases.py >> creatureClasses.py >>
utilFunctions.py >> menu.py >> bridge.py. >> settlement.py >> encounter.py >>
utilClasses.py >> combat.py

Other files might be empty at this time and still subject to addition.
(stories.py , exploration.py)

After reading the in-file Readmes, you are good to read through the code itself
and its comments.


### Glossary
If you read documentation of the code, you will come across regularly mentioned terms.
These are explained here.

- Player                = The human player
- Player class          = Available classes the player can choose from to play in the game (e.g. Warrior, Thief, ...)
- Player class object   = The code object that handles all statistics/attributes and functions of the player
- Class                 = Either a synonym to "Player class" or a specific "Class object" that is a code representation and - should be self-explanatory through the context
- Class object          = An instance of a defined class
- Creature              = Any monster or other NPC inside the game including the player
- Creature class object = Means player class objects AND NPC class objects
- NPC                   = Any creature inside the game that is not the player (Non-Player Character)
- NPC type              = Specifies the type of a NPC (e.g. Goblin, Spider, Skeleton, ...)
- NPC class object      = The code object that handles all statistics/attributes and functions of a NPC
- Monster               = Any NPC inside the game, that is generally considered to be an adversary of the player
- Encounter             = A situation in which the player is challenged in some way. Depending on the player's performance, the outcome will benefit or handicap the player.
- Combat                = A kind of an encounter in which the player is challenged to defeat enemies in martial battle.


### Commands for the Local Terminal
All local scripts will start with some notes that mention commands for the local terminal.
These are terminal commands for the developers convenience and used to quickly test a local
script.
When creating this game, the Atom '1.41.0' IDE in conjunction with the
'platformio-ide-terminal 2.10.0' package was used.


### Imports in Scripts
The imports in the scripts differ from the normal syntax convention because the
filenames begin with a number (so they are listed systematically in a file
directory). Unfortunately, using the syntax:
- "import [module] from [source] as [variable]"

with a file as the source doesn't compute if the name of that file begins with
a number. The reason for that is, that the imports are assigned to a variable
and as soon as that happens, variable naming rules apply (you can't choose
variable names that begin with digits).



## Notes for Code Formatting
These are rules for working on code such as choosing the right variable names etc.
Rules can be broken if it benefits readability. See the code itself to see the rules
in practice.
[Maybe I should use the PEP 8 style guide instead...]

- Names of variables, functions, methods and so on begin with lowercase alphabetical characters.
  When chaining together multiple words as names, every next name starts with an uppercase alphabetical character.
  If the last letter of a chained word is already uppercase, then an underscore is used before the next word and
  the following word begins with a lowercase character unless that next word is an acronym (like DB for database).
  If using digits in between words, the word after the digit should start with an uppercase character.
  - E.g.: thisFunctionName(), thisNPC_variable, NPC_DB, randomFight1Group, ...

  You CAN use descriptive variable prefixes with 2 trailing underscores to indicate the type of the referenced object.
  If the object type has a long name, use an abbreviation. Try to avoid long total variable names though.
  - E.g.: "num_", "str__", "list__", "tup__", "nTup__" (named tuple), "set__", "cl_" (class), ...

- The order of defined functions should reflect the order in which functions are called throughout the program
  as best as possible, and at long as it promotes readability.

- File names begin with a single digit to indicate scripts that include constants, databases, classes etc. that
  will be used across pretty much all other local scripts.
  The next two digits indicate a numbering from most basic scripts to more complicated/involved ones.
  The rest of the file name adheres to the naming rules of variables, functions and so on that were described
  before.
  Here is the systematic order of files as of now (including the order the two-digit-numbering):
  - 0_    = constants, then databases, then general functions, then classes, then everything else
  - 1_    = scripted campaigns, then modular story lines, then a collection of side missions
  - 2_    = menu, then scripts that bridge the gap between the menu and actual parts of the game
  - 3_    = core aspects of the game (from safe places to "a higher degree of danger")
  - 4_    = newly implemented aspects of the game, that don't have a place yet
  - 9_    = copies of older versions of scripts used as reference when implementing new stuff or refactoring
  - iniPlayer.py is a special case that does not adhere to the naming conventions since it has to be imported in a
        special way. Read the In-game Readme of main.py and iniPlayer.py
  - main.py is also a special case just because it is the script that is used to run the game.


- Import names should always be uppercase abbreviations of max. 4 alphabetical characters followed by a single underscore.

- Length of code in one line should not extend over 80 character spaces if possible.
  Comments begin at character space number 81 with a "# " an then the actual comment text.
  Comments can be as long as needed. If code extends over 80 character spaces, then there
  should be buffer of 5 spaces before the comment.

- Every script has to have systematic sections. These are in the right order:
  - Developer Notes, In-file Readme, Imports, Functions, Standalone Variables and then Executing Code
  - More sections can be added and named appropriately. Every section has to placed in form of a heading.
  - E.g.: ############################### In-file Readme #################################
  - The title is always in the middle surrounded by hashtags up until and including character space 80.
  Before every section, there should be 2 empty lines as a buffer. This is only not the case for the
  first section in a script.

- After section headlines, every heading-like comment within the first 80 character spaces
  begins with 5 hashtags. Every sub-heading after that has one less hashtag before it.
  Identical heading levels have the same amount of hashtags before it.

- The Developer Notes section should include the command to call the specific script from the
  command line. Do not include the command for starting Python itself.

- The In-file Readme should summarize the scripts purpose and address necessary long-winded explanations.
  The Readme text has to be ordered into bullet points with dashes ("-").

- All potential imports should be listed in the import section. All that not apply are commented out.

- Include 2 empty lines between functions as a buffer.

- Include empty lines where it aids readability but don't go crazy with it.

- Reference existing code for the right code format.

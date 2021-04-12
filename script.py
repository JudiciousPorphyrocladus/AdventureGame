# Computer science 8.1 adventure game.

import configparser
from os import system
from sys import platform

###############        Stats        ##################
config = configparser.ConfigParser()
config.read("settings.ini")

#################### Variables #######################
firstTime = True
# Basic stats
hunger = config["Stats"]["hunger"] # The level of hunger. Read the manual for more info.
health = config["Stats"]["health"] # Health.
water = config["Stats"]["water"] # The level of water. Read the manual for more info.
xp = config["Stats"]["xp"] # XP. The more XP you have, the higher the level.

# Materials, resources, etc.
coins = config["Stats"]["coins"] # Coins. Read the manual for more info.
gold = config["Stats"]["gold"] # Gold. Read the manual for more info.
iron = config["Stats"]["iron"] # Iron. Read the manual for more info.
emeralds = config["Stats"]["emeralds"] # Emeralds. Read the manual for more info.
carbonCrystals = config["Stats"]["carbonCrystals"] # Carbon crystals. Read the manual for more info.

## Checks if the player is playing for the 1st time ##
if int(config["Player"]["firstTime"]) == 1:
    firstTime = True
else:
    firstTime = False

###################### Test area #####################



##################### Functions ######################

# Save function. If you call it, the changes are written to the .ini file.
def save():
    config["Stats"]["Coins"] = coins
    config["Stats"]["Gold"] = gold
    config["Stats"]["Iron"] = iron
    config["Stats"]["Emeralds"] = emeralds
    config["Stats"]["CarbonCrystals"] = carbonCrystals

    config["Stats"]["Health"] = health
    config["Stats"]["Hunger"] = hunger
    config["Stats"]["Water"] = water
    config["Stats"]["Xp"] = xp

# A function that lets the player see their stats.
def getStats():
    print("Health: ", config["Stats"]["health"])
    print("Hunger: ", config["Stats"]["hunger"])
    print("Water: ", config["Stats"]["water"])

def referenceManual():
    print('''
    This is the game's reference manual. Here you will find the
    information about different stuff inside the game.
    Choose a chapter:
        1. Starting out and levels,
        2. Resources and materials,
        3. Animals,
        4. Quests,
        5. Money and coins,
        6. Villages
    ''')
    Choice = int(input("> "))
    if Choice == 1:
        sys('clear')
        print('''
        Chapter 1 of the reference manual: STARTING OUT.

        1 - When you spawn for the first time, you get a starter pack which
            contains some useful stuff. For example, a few pieces of iron and 10 coins.
        1.1 - When you leave the house, you get 10 XP. XP shows how much you have
              played the game. The more XP you have, the higher your level is. For example:
              level 2 is 100 XP. Level 5 is 300 XP and so on and so forth. At the start of
              the game you have 0 XP.
        1.2 - You can go to different locations. You can view the locations by typing
              viewLocations() while playing the game.
        ''')

def start():
    
    while firstTime == True:
        if firstTime == True:
            print("Hello! This is an adventure game called john cena bobux.")
            print("Choose an option:")
            print("1. Start playing the game,")
            print("2. Open the reference manual (help menu),")
            print("3. View your statistics and inventory")
            choice = iny(input("> "))
            if choice == 1:
                # start the game
                print('ok')
            elif choice == 2:
                # bruh
                print('ok')
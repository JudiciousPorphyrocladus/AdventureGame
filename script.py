# Computer science 8.1 adventure game.

import configparser
from os import system
from sys import platform

###############        Stats        ##################
config = configparser.ConfigParser()
config.read("settings.ini")

#################### Variables #######################
firstTime = True
clear = '' # clear function. Later in the code it will be changed to either 'clear' or 'cls' based on the system.
manual = open("manual.txt")

# Coordinates and location
X = config["Player"]["X"]
Y = config["Player"]["Y"]
area = config["Player"]["area"]

# Basic stats
hunger = config["Stats"]["hunger"] # The level of hunger. Read the help menu for more info.
health = config["Stats"]["health"] # Health.
water = config["Stats"]["water"] # The level of water. Read the help menu for more info.
xp = config["Stats"]["xp"] # XP. The more XP you have, the higher the level.

# Materials, resources, etc.
coins = config["Stats"]["coins"] # Coins. Read the help menu for more info.
gold = config["Stats"]["gold"] # Gold. Read the help menu for more info.
iron = config["Stats"]["iron"] # Iron. Read the help menu for more info.
emeralds = config["Stats"]["emeralds"] # Emeralds. Read the help menu for more info.
bronze = config["Stats"]["bronze"] # Carbon crystals. Read the help menu for more info.
coal = config["Stats"]["coal"] # Coal. Read the help menu for more info.

## Checks if the player is playing for the 1st time ##
if int(config["Player"]["firstTime"]) == 1:
    firstTime = True
else:
    firstTime = False

## Checks the player's operating system ##
if platform == "linux" or platform == "linux2" or platform == "darwin":
    clear = 'clear'
elif platform == "win32":
    clear = 'cls'
else:
    Clear = str(input("Your OS isn't supported. In order to play the game, please enter the clear function of your console: "))
    clear = Clear

##################### Functions ######################

# Save function. If you call it, the changes are written to the .ini file.
def save():
    config["SavedData"]["Coins"] = coins
    config["SavedData"]["Gold"] = gold
    config["SavedData"]["Iron"] = iron
    config["SavedData"]["Emeralds"] = emeralds
    config["SavedData"]["Bronze"] = bronze
    config["SavedData"]["Coal"] = coal

    config["SavedData"]["Health"] = health
    config["SavedData"]["Hunger"] = hunger
    config["SavedData"]["Water"] = water
    config["SavedData"]["Xp"] = xp

    config["SavedData"]["x"] = X
    config["SavedData"]["y"] = Y
    config["SavedData"]["Area"] = area

# A function that lets the player see their stats.
def getStats():
    print("Health: ", config["Stats"]["health"])
    print("Hunger: ", config["Stats"]["hunger"])
    print("Water: ", config["Stats"]["water"])

def help():
    system(clear)
    print(manual.read())

def surroundings():
    print('foo')

def play():
    print('bar')

def viewStats():
    print("========== Character info ==========")
    print("     Health: " + str(health))
    print("     Hunger: " + str(hunger))
    print("     Water: " + str(water))
    print("     XP: " + str(xp))
    print("     Coordinates: (" + str(X) + ", " + str(Y) + ")")
    print("====================================")

    print("============ Inventory ============")
    print("     Coins: " + str(coins))
    print("     Iron: " + str(iron))
    print("     Coal: " + str(coal))
    print("     Bronze: " + str(bronze))
    print("     Gold: " + str(gold))
    print("     Emeralds: " + str(emeralds))
    print("===================================")

def start():
    print("Hello! This is an adventure game called john cena bobux.")
    print("Choose an option:")
    print("1. Start playing the game,")
    print("2. Open the help menu,")
    print("3. View your statistics and inventory,")
    print("4. Open commands reference manual.")
    choice = 0
    f = False
    while f == False:
        choice = int(input("> "))
        if choice == 1:
            play()
            f = True
        elif choice == 2:
            help()
        elif choice == 3:
            viewStats()
        elif choice == 4:
            # I'll make the function soon
            print('foo')
        else:
            print('Please enter a valid number!')

start()
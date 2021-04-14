# Computer science 8.1 adventure game.
# Some variables might seem weird or useless because of their name (e.g. 'G' or 'F'), however they aren't. I just can't come up with a name for a variable that I will not actually use in more than 1 function.

import configparser
import os
import random
from os import system
from sys import platform

### Stats ###########################
config = configparser.ConfigParser()
config.read("settings.ini")

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

# Food - meat
beef = int(config["Stats"]["beef"])
pork = int(config["Stats"]["pork"])
chicken = int(config["Stats"]["chicken"])
# Food - vegetables
carrot = int(config["Stats"]["carrot"])
potato = int(config["Stats"]["potato"])
broccoli = int(config["Stats"]["broccoli"])
# Food - fruits
oranges = int(config["Stats"]["oranges"])
mango = int(config["Stats"]["mango"])
banana = int(config["Stats"]["banana"])

int(beef); int(pork); int(chicken); int(carrot); int(potato); int(broccoli); int(oranges); int(mango); int(banana); int(iron); int(gold); int(coins); int(emeralds); int(coal); int(bronze)

### Variables #######################
firstTime = True
playing = True
startInputActive = True
startChoice = 0
Play = False
playFreezed = False
houseChest = False
clear = '' # Later in the code it will be changed to either 'clear' or 'cls' based on the system.

# HELP AND COMMANDS 
with open("./Manual/manual.txt", 'r') as manual:
    manual = manual.read()
with open("./Manual/manual1.txt", 'r') as manual1:
    manual1 = manual1.read()
with open("./Manual/manual2.txt", 'r') as manual2:
    manual2 = manual2.read()
with open("./Manual/manual3.txt", 'r') as manual3:
    manual3 = manual3.read()
with open("./Manual/manual4.txt", 'r') as manual4:
    manual4 = manual4.read()
with open("./commands.txt", 'r') as commands:
    commands = commands.read()
manual1Input = False
manual2Input = False
manual3Input = False
manual4Input = False
helpInput = False

# Coordinates and location
X = config["Player"]["x"]
Y = config["Player"]["y"]
area = config["Player"]["area"]

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
    # Saving materials and resources.
    config["SavedData"]["savedCoins"] = coins
    config["SavedData"]["savedGold"] = gold
    config["SavedData"]["savedIron"] = iron
    config["SavedData"]["savedEmeralds"] = emeralds
    config["SavedData"]["savedBronze"] = bronze
    config["SavedData"]["savedCoal"] = coal
    # Saving basic stats.
    config["SavedData"]["savedHealth"] = health
    config["SavedData"]["savedHunger"] = hunger
    config["SavedData"]["savedWater"] = water
    config["SavedData"]["savedXp"] = xp
    # Saving coordinates so that the player spawns where they left.
    config["SavedData"]["savedX"] = X
    config["SavedData"]["savedY"] = Y
    config["SavedData"]["savedArea"] = area
    # Saving food so that player doesn't get angry at me because I didn't save it.
    config["Stats"]["savedBeef"] = beef
    config["Stats"]["savedPork"] = pork
    config["Stats"]["savedChicken"] = chicken
    config["Stats"]["savedCarrot"] = carrot
    config["Stats"]["savedPotato"] = potato
    config["Stats"]["savedBroccoli"] = broccoli
    config["Stats"]["savedOranges"] = oranges
    config["Stats"]["savedMango"] = mango
    config["Stats"]["savedBanana"] = banana

# A function that lets the player see their stats.
def getStats():
    print("Health: ", config["Stats"]["health"])
    print("Hunger: ", config["Stats"]["hunger"])
    print("Water: ", config["Stats"]["water"])

# A function that shows the player 1st chapter of the manual.
def Manual1():
    system(clear)
    print(manual1)
    print("Type either 'back' to choose a chapter you want to view or 'menu' to exit the manual.")
    manual1Input = True
    while manual1Input == True:
        choice1 = ''
        choice1 = input("> ").lower()
        if choice1 == 'back':
            manual1Input = False
            help()
            helpInput = True
        elif choice1 == 'menu':
            manual1Input = False
            start()
        else:
            print("Please enter a valid choice. ")

def Manual2():
    system(clear)
    print(manual2)
    print("Type either 'back' to choose a chapter you want to view or 'menu' to exit the manual.")
    manual2Input = True
    while manual2Input == True:
        choice2 = input("> ").lower()
        if str(choice2) == 'back':
            help()
            helpInput = True
            manual2Input = False
        elif str(choice2) == 'menu':
            start()
            manual2Input = False
        else:
            print("Please enter a valid choice. ")

def Manual3():
    system(clear)
    print(manual3)
    print("Type either 'back' to choose a chapter you want to view or 'menu' to exit the manual.")
    manual3Input = True
    while manual3Input == True:
        choice3 = input("> ").lower()
        if str(choice3) == 'back':
            help()
            helpInput = True
            manual3Input = False
        elif str(choice3) == 'menu':
            start()
            manual3Input = False
        else:
            print("Please enter a valid choice. ")

def Manual4():
    system(clear)
    print(manual4)
    print("Type either 'back' to choose a chapter you want to view or 'menu' to exit the manual.")
    manual4Input = True
    while manual4Input == True:
        choice4 = ''
        choice4 = input("> ").lower()
        if str(choice4) == 'back':
            help()
            helpInput = True
            manual4Input = False
        elif str(choice4) == 'menu':
            start()
            manual4Input = False
        else:
            print("Please enter a valid choice.")


# A menu that asks you to enter the number of a desired chapter.
def help():
    system(clear)
    print("============== Chapters ===============")
    print(" Chapter 1 - STARTING OUT\n Chapter 2 - RESOURCES AND MATERIALS\n Chapter 3 - FOOD\n Chapter 4 - LOCATIONS")
    print(" Please choose a chapter")
    print(" To go back press enter")
    helpInput = True
    while helpInput == True:
        helpChoice = 0
        helpChoice = input("> ")

        if helpChoice == '1':
            Manual1()
            helpInput = False
        elif helpChoice == '2':
            Manual2()
            helpInput = False
        elif helpChoice == '3':
            Manual3()
            helpInput = False
        elif helpChoice == '4':
            Manual4()
            helpInput = False
        elif helpChoice == '' and playFreezed == False:
            start()
            startInputActive = True
            helpInput = False
        elif helpChoice == '' and playFreezed == True:
            Play = True
            helpInput = False
            play()
        else:
            print("Please enter a valid choice.")

def look():
    print('foo')

def commands():
    system(clear)
    print(commands)

def commonChest(chanceNum1, chanceNum2):
    global chicken
    global iron
    global carrot
    Play = False
    playFreezed = True
    chestOpening = True

    chestchance = random.randint(chanceNum1, chanceNum2)
    if chestchance == 1:
        print("There is a common chest inside the house. Would you like to open it? (Y/n)")
        chestChoice = ''
        while chestChoice != 'y' or chestChoice != 'yes' or chestChoice != 'n' or chestChoice != 'no' or chestChoice != '':
            chestChoice = input("> ").lower()
            if chestChoice == 'y' or chestChoice == 'yes' or chestChoice == '':
                IRON = random.randint(1, 3)
                if IRON == 1:
                    print("You have found 1 iron! Chance: 33%")
                    iron = iron + 1
                else:
                    pass
                del IRON
                    
                CARROT = random.randint(1, 2)
                if CARROT == 1:
                    print("You have found a carrot! Chance: 50%")
                    carrot = carrot + 1
                else:
                    pass
                del CARROT

                CHICKEN = random.randint(1, 3)
                if CHICKEN == 1:
                    print("You have found a chicken! Chance: 33%")
                    chicken = chicken + 1
                else:
                    pass
                del CHICKEN
            else:
                print("Sorry, but you haven't found anything in the chest. You will be lucky next time!")
                pass
    else:
        print("Sorry, but you haven't found any chests in the house. The chance was: 50%. You will be lucky next time!")
    del chestchance
    Play = False
    playFreezed = False
    chestOpening = False
    play()

def play():
    system(clear)
    startInputActive = False
    Play = True
    playFreezed = False
    if area == "TownHouse":
        print("You were spawned in " + area + ". The town's name is: Johncenangton. Remember: you can get help by typing help() or commands() to view commands!")
        commonChest(1, 2)
    while Play == True:
        bruh = input("> ")
        if bruh == "help()":
            Play = False
            playFreezed = True
            help()

def viewStats():
    system(clear)
    print("========== Character info ==========")
    print("     Health: " + str(health))
    print("     Hunger: " + str(hunger))
    print("     Water: " + str(water))
    print("     XP: " + str(xp))
    print("     Coordinates: (" + str(X) + ", " + str(Y) + ")")
    print("====================================")

    print("============ Inventory ============")
    print("     Coins: " + str(coins))
    print("     Iron: " + str(iron)); int(iron)
    print("     Coal: " + str(coal))
    print("     Bronze: " + str(bronze))
    print("     Gold: " + str(gold))
    print("     Emeralds: " + str(emeralds))
    print("===================================")
    print("press enter when you have finished reading your stats.")
    Exit = input("> ")
    start()
        

def start():
    system(clear)
    print("========================== Menu ==========================")
    print(" Hello! This is an adventure game called john cena bobux.")
    print(" Choose an option:")
    print(" 1. Start playing the game,")
    print(" 2. Open the help menu,")
    print(" 3. View your statistics and inventory,")
    print(" 4. Open commands reference manual.")
    startInputActive = True
    while startInputActive == True:
        startChoice = 0
        startChoice = input("> ")
        if startChoice == '1':
            play()
            startInputActive = False
        elif startChoice == '2':
            help()
            startInputActive = False
        elif startChoice == '3':
            viewStats()
        elif startChoice == '4':
            commands()
            startInputActive = False
        else:
            print('Please enter a valid number!')

start()

while playing == True:
    if Play == False and playFreezed == True and chestOpening == True:
        play()
    else:
        pass
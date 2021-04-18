# Computer science 8.1 adventure game
import json
import os
import random
from os import system
from sys import platform

# Progress file
with open(os.getcwd() + "/stats.json", 'r') as data:
    datastore = json.load(data)

hunger = datastore["data"]["characterInfo"]["hunger"]
health = datastore["data"]["characterInfo"]["health"]
water = datastore["data"]["characterInfo"]["water"]
xp = datastore["data"]["characterInfo"]["xp"]
X = datastore["data"]["characterInfo"]["x"]
Y = datastore["data"]["characterInfo"]["y"]
area = datastore["data"]["characterInfo"]["area"]
hasProgress = datastore["data"]["playerInfo"]["hasProgress"]

# Materials, resources
coins = datastore["data"]["materials"]["coins"]
gold = datastore["data"]["materials"]["gold"]
iron = datastore["data"]["materials"]["iron"]
emeralds = datastore["data"]["materials"]["emeralds"]
bronze = datastore["data"]["materials"]["bronze"]
coal = datastore["data"]["materials"]["coal"]

# Food
beef = datastore["data"]["food"]["meat"]["beef"]
pork = datastore["data"]["food"]["meat"]["pork"]
chicken = datastore["data"]["food"]["meat"]["chicken"]
carrot = datastore["data"]["food"]["vegetables"]["carrot"]
potato = datastore["data"]["food"]["vegetables"]["potato"]
broccoli = datastore["data"]["food"]["vegetables"]["broccoli"]
oranges = datastore["data"]["food"]["fruits"]["oranges"]
mango = datastore["data"]["food"]["fruits"]["mango"]
banana = datastore["data"]["food"]["fruits"]["banana"]

# Beverages
waterBottles = datastore["data"]["food"]["beverages"]["waterBottles"]
seaWaterBottles = datastore["data"]["food"]["beverages"]["seaWaterBottles"]
orangeJuiceBottles = datastore["data"]["food"]["beverages"]["orangeJuiceBottles"]
appleJuiceBottles = datastore["data"]["food"]["beverages"]["appleJuiceBottles"]
tea = datastore["data"]["food"]["beverages"]["tea"]

# Variables
firstTime = True
playing = True
startInputActive = True
startChoice = 0
Play = False
playfreezed = False
houseChest = False
chestOpening = False
houseChestOpened = False

# Input variables (used to loop input() if the correct choice isn't entered)
manualInput = False
helpInput = False

# Manual chapters and commands
with open('Manual/manual.txt') as nmanual:
    manual = nmanual.read()
with open('Manual/manual1.txt') as nmanual1:
    manual1 = nmanual1.read()
with open('Manual/manual2.txt') as nmanual2:
    manual2 = nmanual2.read()
with open('Manual/manual3.txt') as nmanual3:
    manual3 = nmanual3.read()
with open('Manual/manual4.txt') as nmanual4:
    manual4 = nmanual4.read()
with open('commands.txt') as ncommands:
    commands = ncommands.read()

# First time playing check
if datastore["data"]["playerInfo"]["firstTime"]:
    firstTime = True
else:
    firstTime = False

# Operating system check
if platform == "linux" or platform == "linux2" or platform == "darwin":
    clear = 'clear'
elif platform == "win32":
    clear = 'cls'
else:
    print("Your OS isn't supported.")
    Clear = str(input("In order to play the game, please enter the clear function of your console: "))
    clear = Clear

# Functions


def save():  # Save function
    print('foo')


def load():
    global coins
    global gold
    global iron
    global emeralds
    global bronze
    global coal
    global health
    global hunger
    global water
    global xp
    global X
    global Y
    global area
    global beef
    global pork
    global chicken
    global carrot
    global broccoli
    global potato
    global oranges
    global mango
    global banana
    global waterBottles
    global seaWaterBottles
    global orangeJuiceBottles
    global appleJuiceBottles
    global tea
    coins = datastore["data"]["materials"]["coins"]
    gold = datastore["data"]["materials"]["gold"]
    iron = datastore["data"]["materials"]["iron"]
    emeralds = datastore["data"]["materials"]["emeralds"]
    bronze = datastore["data"]["materials"]["bronze"]
    coal = datastore["data"]["materials"]["coal"]
    health = datastore["data"]["characterInfo"]["health"]
    hunger = datastore["data"]["characterInfo"]["hunger"]
    water = datastore["data"]["characterInfo"]["water"]
    xp = datastore["data"]["characterInfo"]["xp"]
    X = datastore["data"]["characterInfo"]["x"]
    Y = datastore["data"]["characterInfo"]["y"]
    area = datastore["data"]["characterInfo"]["area"]
    # i hate coding
    beef = datastore["data"]["food"]["meat"]["beef"]
    pork = datastore["data"]["food"]["meat"]["pork"]
    chicken = datastore["data"]["food"]["meat"]["chicken"]
    carrot = datastore["data"]["food"]["vegetables"]["carrot"]
    potato = datastore["data"]["food"]["vegetables"]["potato"]
    broccoli = datastore["data"]["food"]["vegetables"]["broccoli"]
    oranges = datastore["data"]["food"]["fruits"]["oranges"]
    mango = datastore["data"]["food"]["fruits"]["mango"]
    banana = datastore["data"]["food"]["fruits"]["banana"]
    waterBottles = datastore["data"]["food"]["beverages"]["waterBottles"]
    seaWaterBottles = datastore["data"]["food"]["beverages"]["seaWaterBottles"]
    orangeJuiceBottles = datastore["data"]["food"]["beverages"]["orangeJuiceBottles"]
    appleJuiceBottles = datastore["data"]["food"]["beverages"]["appleJuiceBottles"]
    tea = datastore["data"]["food"]["beverages"]["tea"]


def readManual(manualnum):
    global manualInput
    global helpInput
    system(clear)

    if manualnum == 1:
        print(manual1)
    elif manualnum == 2:
        print(manual2)
    elif manualnum == 3:
        print(manual3)
    elif manualnum == 4:
        print(manual4)
    else:
        return
    print("Type either 'back' to choose a chapter you want to view or 'menu' to exit the manual.")
    manualInput = True
    while manualInput:
        choice1 = input("[Manual] > ").lower()
        if choice1 == 'back':
            manualInput = False
            gameHelp()
            helpInput = True
        elif choice1 == 'menu':
            manualInput = False
            start()
        else:
            print("Please enter a valid choice. ")


def gameHelp():  # A menu that asks you to enter the number of a desired chapter.
    global startInputActive
    global Play
    global helpInput

    system(clear)
    print("============== Chapters ===============")
    print(" Chapter 1 - STARTING OUT\n Chapter 2 - RESOURCES AND MATERIALS\n Chapter 3 - FOOD\n Chapter 4 - LOCATIONS")
    print(" Please choose a chapter")
    print(" To go back press enter")
    helpInput = True
    while helpInput:
        helpChoice = input("[Help menu] > ")
        if helpChoice == '1':
            readManual(1)
            helpInput = False
        elif helpChoice == '2':
            readManual(2)
            helpInput = False
        elif helpChoice == '3':
            readManual(3)
            helpInput = False
        elif helpChoice == '4':
            readManual(4)
            helpInput = False
        elif helpChoice == '' and playfreezed is False:
            start()
            startInputActive = True
            helpInput = False
        elif helpChoice == '' and playfreezed:
            Play = True
            helpInput = False
            play()
        else:
            print("Please enter a valid choice.")


def look():
    if X >= 0 and Y >= 0:
        if X <= 15 and Y <= 15:
            print("There are 2 locations in the chunk: ")


def Commands():
    system(clear)
    print(commands)
    print("Press enter to go back")

    bruh = ' '
    while bruh != '':
        bruh = input("[Commands] > ")

    play()


def addIron(quantity):
    global iron
    iron = iron + quantity


def addCarrot(quantity):
    global carrot
    carrot = carrot + quantity


def addChicken(quantity):
    global chicken
    chicken = chicken + quantity


def chest():
    Bruh = random.randint(1, 2)
    if Bruh < 2:
        return False
    elif Bruh > 1:
        return True
    return


def openChest(chesttype):
    global Play
    global playfreezed
    global chestOpening

    Play = False
    playfreezed = True
    loot = False

    if str(chesttype) == 'common':
        print("\nThere is a common chest inside the house. Would you like to open it? (Y/n)")
        # I can't exit the loop even though chestOpening is set to 0.
        chestInput = " "
        while chestInput not in ['y', 'yes', '']:
            chestInput = input("[Chest opening] > ").lower()
            if chestInput == 'y' or chestInput == 'yes':
                IRON = random.randint(1, 3)
                if IRON == 1:
                    print("You have found 1 iron! Chance: 33%")
                    addIron(1)
                    loot = True
                else:
                    continue
                del IRON

                CARROT = random.randint(1, 2)
                if CARROT == 1:
                    print("You have found a carrot! Chance: 50%")
                    addCarrot(1)
                    loot = True
                else:
                    continue
                del CARROT

                CHICKEN = random.randint(1, 3)
                if CHICKEN == 1:
                    print("You have found a chicken! Chance: 33%")
                    addChicken(1)
                    loot = True
                else:
                    continue
                del CHICKEN

                Play = False
                playfreezed = False
                play()
            else:
                Play = False
                playfreezed = False
                play()
        if not loot:
            print("Nothing in the chest. Don't worry, you will be lucky next time!")


def play():
    global startInputActive
    global playfreezed
    global Play

    startInputActive = False
    Play = True
    playfreezed = False


def goNorth():
    global Y
    Y = Y + 1


def goSouth():
    global Y
    Y = Y - 1


def goEast():
    global X
    X = X + 1


def goWest():
    global X
    X = X - 1


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
    print("     Iron: " + str(iron))
    print("     Coal: " + str(coal))
    print("     Bronze: " + str(bronze))
    print("     Gold: " + str(gold))
    print("     Emeralds: " + str(emeralds))
    print("===================================")
    print("press enter when you have finished reading your stats.")
    input("[Viewing stats] > ")
    start()


def eat(foodType):
    global hunger
    global beef
    global pork
    global chicken
    global carrot
    global potato
    global broccoli
    global oranges
    global mango
    global banana
    global water

    if foodType == 'beef':
        if beef > 0:
            print("Before: hunger - ", hunger, "; water - ", water, ".")
            hunger = hunger + 7
            water = water - 2
            print("After: hunger - ", hunger, "; water - ", water, ".")
            play()
        else:
            print("You have 0 beef chops.")
            play()
    elif foodType == "pork":
        if pork > 0:
            print("Before: hunger - ", hunger, "; water - ", water, ".")
            hunger = hunger + 7
            water = water - 2
            print("After: hunger - ", hunger, "; water - ", water, ".")
            play()
        else:
            print("You have 0 pork chops.")
            play()
    elif foodType == "chicken":
        if chicken > 0:
            print("Before: hunger - ", hunger, "; water - ", water, ".")
            hunger = hunger + 6
            water = water - 1
            print("After: hunger - ", hunger, "; water - ", water, ".")
            play()
        else:
            print("You have 0 chicken chops.")
            play()
    elif foodType == "carrot":
        if carrot > 0:
            print("Before: hunger - ", hunger, "; water - ", water, ".")
            hunger = hunger + 4
            print("After: hunger - ", hunger, "; water - ", water, ".")
            play()
        else:
            print("You have 0 carrots.")
            play()
    elif foodType == "potato":
        if potato > 0:
            print("Before: hunger - ", hunger, "; water - ", water, ".")
            hunger = hunger + 3
            print("After: hunger - ", hunger, "; water - ", water, ".")
            play()
        else:
            print("You have 0 potatoes.")
            play()
    elif foodType == "broccoli":
        if broccoli > 0:
            print("Before: hunger - ", hunger, "; water - ", water, ".")
            hunger = hunger + 3
            print("After: hunger - ", hunger, "; water - ", water, ".")
            play()
        else:
            print("You have 0 broccoli.")
            play()
    elif foodType == "orange":
        if oranges > 0:
            print("Before: hunger - ", hunger, "; water - ", water, ".")
            hunger = hunger + 2
            water = water + 3
            print("After: hunger - ", hunger, "; water - ", water, ".")
            play()
        else:
            print("You have 0 oranges.")
            play()
    elif foodType == "mango":
        if mango > 0:
            print("Before: hunger - ", hunger, "; water - ", water, ".")
            hunger = hunger + 2
            water = water + 3
            print("After: hunger - ", hunger, "; water - ", water, ".")
            play()
        else:
            print("You have 0 mangoes.")
            play()
    elif foodType == "banana":
        if banana > 0:
            print("Before: hunger - ", hunger, "; water - ", water, ".")
            hunger = hunger + 1
            print("After: hunger - ", hunger, "; water - ", water, ".")
            play()
        else:
            print("You have 0 bananas.")
            play()
    else:
        print("Please enter a valid argument for the eat() function!")
        play()


def drink(beverageType):
    print('bar')


def fastTravel(location):
    print('foo')


def start():
    global firstTime
    global hasProgress

    if hasProgress:
        print("You have saved progress! Would you like to load it? (Y, n)")
        userLoadInput = ""
        while userLoadInput not in ['y', 'yes', 'n', 'no']:
            userLoadInput = input("[Loading progress] > ").lower()
            if userLoadInput == 'y':
                load()
            elif userLoadInput == 'yes':
                load()
            elif userLoadInput == 'n':
                break
            elif userLoadInput == 'no':
                break
            else:
                pass

    global startInputActive
    global startChoice
    system(clear)
    print("IT WORKS")
    print("========================== Menu ==========================")
    print(" Hello! This is an adventure game called john cena bobux.")
    print(" Choose an option:")
    print(" 1. Start playing the game,")
    print(" 2. Open the help menu,")
    print(" 3. View your statistics and inventory,")
    print(" 4. Open commands reference manual.")
    startInputActive = True
    while startInputActive:
        startChoice = 0
        startChoice = input("> ")
        if startChoice == '1':
            system(clear)
            play()
            startInputActive = False
        elif startChoice == '2':
            gameHelp()
            startInputActive = False
        elif startChoice == '3':
            viewStats()
        elif startChoice == '4':
            Commands()
            startInputActive = False
        else:
            print('Please enter a valid number!')


start()

while True:
    if Play and not playfreezed:
        if firstTime:
            print("You were spawned in " + area + ". The town's name is: Johncenangton.")
            print("Remember: you can get help by typing gameHelp or commands to view commands!")
            firstTime = False
        while Play:
            if not houseChestOpened:
                chestChance = chest()
                if chestChance:
                    openChest('common')
                else:
                    pass
                houseChestOpened = True
            playInput = ''
            while playInput not in ['gamehelp()', 'gamehelp', 'commands()', 'commands', 'gonorth()', 'gonorth', 'gosouth()', 'gosouth', 'goeast()', 'goeast', 'gowest()', 'gowest', 'exit()', 'exit', 'save()', 'save', 'viewstats()', 'viewstats']:
                playInput = input("[Play] > ").lower()
                if playInput == "gamehelp()" or playInput == "gamehelp":
                    Play = False
                    playfreezed = True
                    gameHelp()
                elif playInput == "commands()" or playInput == "commands":
                    Play = False
                    playfreezed = True
                    Commands()
                elif playInput == "gonorth()" or playInput == "gonorth":
                    goNorth()
                elif playInput == "gosouth()" or playInput == "gosouth":
                    goSouth()
                elif playInput == "goeast()" or playInput == "goeast":
                    goEast()
                elif playInput == "gowest()" or playInput == "gowest":
                    goWest()
                elif playInput == "exit()" or playInput == "exit":
                    save()
                    exit()
                elif playInput == "save()" or playInput == "save":
                    save()
                elif playInput == "viewstats()" or playInput == "viewstats":
                    save()
                    viewStats()
                elif playInput == "eat":
                    foodtype = input("Please enter the argument for function eat(): ")
                    eat(foodtype)
                else:
                    print("I don't know this phrase. Please read the manual.")

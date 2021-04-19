# Computer science 8.1 adventure game
import json
import os
import random
from os import system
from sys import platform

# Progress file
data = open(os.getcwd() + "/stats.json", 'r')
datastore = json.load(data)
data.close()

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
firstTime = datastore["data"]["playerInfo"]["firstTime"]
playing = True
startInputActive = True
startChoice = 0
Play = False
playfreezed = False
houseChest = False
chestOpening = False
houseChestOpened = False
level = 0


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
    del Clear

# Functions


def changeLevel():
    global xp
    global level
    level = round(abs(xp / 100))


def save():  # Save function
    datastore["data"]["materials"]["coins"] = coins
    datastore["data"]["materials"]["gold"] = gold
    datastore["data"]["materials"]["iron"] = iron
    datastore["data"]["materials"]["emeralds"] = emeralds
    datastore["data"]["materials"]["bronze"] = bronze
    datastore["data"]["materials"]["coal"] = coal
    datastore["data"]["characterInfo"]["health"] = health
    datastore["data"]["characterInfo"]["hunger"] = hunger
    datastore["data"]["characterInfo"]["water"] = water
    datastore["data"]["characterInfo"]["xp"] = xp
    datastore["data"]["characterInfo"]["x"] = X
    datastore["data"]["characterInfo"]["y"] = Y
    datastore["data"]["characterInfo"]["area"] = area
    datastore["data"]["food"]["meat"]["beef"] = beef
    datastore["data"]["food"]["meat"]["pork"] = pork
    datastore["data"]["food"]["meat"]["chicken"] = chicken
    datastore["data"]["food"]["vegetables"]["carrot"] = carrot
    datastore["data"]["food"]["vegetables"]["potato"] = potato
    datastore["data"]["food"]["vegetables"]["broccoli"] = broccoli
    datastore["data"]["food"]["fruits"]["oranges"] = oranges
    datastore["data"]["food"]["fruits"]["mango"] = mango
    datastore["data"]["food"]["fruits"]["banana"] = banana
    datastore["data"]["food"]["beverages"]["waterBottles"] = waterBottles
    datastore["data"]["food"]["beverages"]["seaWaterBottles"] = seaWaterBottles
    datastore["data"]["food"]["beverages"]["orangeJuiceBottles"] = orangeJuiceBottles
    datastore["data"]["food"]["beverages"]["appleJuiceBottles"] = appleJuiceBottles
    datastore["data"]["food"]["beverages"]["tea"] = tea
    datastore["data"]["playerInfo"]["firstTime"] = False
    datastore["data"]["playerInfo"]["hasProgress"] = True
    saveddatastore = open("savedstats.json", 'w')
    json.dump(datastore, saveddatastore)
    saveddatastore.close()
    play()


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
    global firstTime
    global hasProgress
    Saveddatastore = open(os.getcwd() + "/savedstats.json", 'r')
    saveddatastore = json.load(Saveddatastore)
    Saveddatastore.close()

    coins = saveddatastore["data"]["materials"]["coins"]
    gold = saveddatastore["data"]["materials"]["gold"]
    iron = saveddatastore["data"]["materials"]["iron"]
    emeralds = saveddatastore["data"]["materials"]["emeralds"]
    bronze = saveddatastore["data"]["materials"]["bronze"]
    coal = saveddatastore["data"]["materials"]["coal"]
    health = saveddatastore["data"]["characterInfo"]["health"]
    hunger = saveddatastore["data"]["characterInfo"]["hunger"]
    water = saveddatastore["data"]["characterInfo"]["water"]
    xp = saveddatastore["data"]["characterInfo"]["xp"]
    X = saveddatastore["data"]["characterInfo"]["x"]
    Y = saveddatastore["data"]["characterInfo"]["y"]
    area = saveddatastore["data"]["characterInfo"]["area"]
    firstTime = saveddatastore["data"]["playerInfo"]["firstTime"]
    hasProgress = saveddatastore["data"]["playerInfo"]["hasProgress"]

    # i hate coding
    beef = saveddatastore["data"]["food"]["meat"]["beef"]
    pork = saveddatastore["data"]["food"]["meat"]["pork"]
    chicken = saveddatastore["data"]["food"]["meat"]["chicken"]
    carrot = saveddatastore["data"]["food"]["vegetables"]["carrot"]
    potato = saveddatastore["data"]["food"]["vegetables"]["potato"]
    broccoli = saveddatastore["data"]["food"]["vegetables"]["broccoli"]
    oranges = saveddatastore["data"]["food"]["fruits"]["oranges"]
    mango = saveddatastore["data"]["food"]["fruits"]["mango"]
    banana = saveddatastore["data"]["food"]["fruits"]["banana"]
    waterBottles = saveddatastore["data"]["food"]["beverages"]["waterBottles"]
    seaWaterBottles = saveddatastore["data"]["food"]["beverages"]["seaWaterBottles"]
    orangeJuiceBottles = saveddatastore["data"]["food"]["beverages"]["orangeJuiceBottles"]
    appleJuiceBottles = saveddatastore["data"]["food"]["beverages"]["appleJuiceBottles"]
    tea = saveddatastore["data"]["food"]["beverages"]["tea"]


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
    print("     Level: " + str(level))
    print("     Coordinates: (" + str(X) + ", " + str(Y) + ")")
    print("====================================")

    print("============ Inventory ============")
    print("     Coins: " + str(coins))
    print("     Iron: " + str(iron))
    print("     Coal: " + str(coal))
    print("     Bronze: " + str(bronze))
    print("     Gold: " + str(gold))
    print("     Emeralds: " + str(emeralds))
    print("     Beef: " + str(beef))
    print("     Pork: " + str(pork))
    print("     Chicken: " + str(chicken))
    print("     Carrots: " + str(carrot))
    print("     Potatoes: " + str(potato))
    print("     Broccoli: " + str(broccoli))
    print("     Oranges: " + str(oranges))
    print("     Mangoes: " + str(mango))
    print("     Bananas: " + str(banana))
    print("===================================")
    print("press enter when you have finished reading your stats.")
    input("[Viewing stats] > ")
    if not Play and playfreezed:
        start()
    else:
        play()


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
    global hunger
    global water
    global waterBottles
    global seaWaterBottles
    global orangeJuiceBottles
    global appleJuiceBottles
    global tea
    if beverageType == 'waterbottle':
        if waterBottles > 0:
            print("Before: water - ", water, ".")
            water = water + 5
            print("After: water - ", water, ".")
            play()
        else:
            print("You have 0 water bottles.")
            play()
    elif beverageType == "seawaterbottle":
        if seaWaterBottles > 0:
            print("Before: water - ", water, ".")
            water = water - 3
            print("After: water - ", water, ".")
            play()
        else:
            print("You have 0 sea water bottles.")
            play()
    elif beverageType == "orangejuicebottle":
        if orangeJuiceBottles > 0:
            print("Before: water - ", water, ".")
            water = water + 3
            print("After: water - ", water, ".")
            play()
        else:
            print("You have 0 orange juice bottles.")
            play()
    elif beverageType == "applejuicebottle":
        if appleJuiceBottles > 0:
            print("Before: water - ", water, ".")
            water = water + 3
            print("After: water - ", water, ".")
            play()
        else:
            print("You have 0 apple juice bottles.")
            play()
    elif beverageType == "tea":
        if tea > 0:
            print("Before: water - ", water, ".")
            water = water + 2
            print("After: water - ", water, ".")
            play()
        else:
            print("You have 0 tea.")
            play()
    else:
        print("Please enter a valid argument for the drink() function!")
        play()


def fastTravel(location):
    global X
    global Y
    if location == 'bandithideout1':
        if level >= 10:
            X = 20
            Y = 20
        else:
            print("You don't have the appropriate level to fast travel here!")
    elif location == 'bandithideout2':
        if level >= 20:
            X = -65
            Y = -65
        else:
            print("You don't have the appropriate level to fast travel here!")
    elif location == 'bandithideout3':
        if level >= 30:
            X = 180
            Y = 180
        else:
            print("You don't have the appropriate level to fast travel here!")
    elif location == 'johncenangton':
        X = 0
        Y = 0
    elif location == 'bobuxbury':
        if level >= 10:
            X = 50
            Y = 50
        else:
            print("You don't have the appropriate level to fast travel here!")
    elif location == 'monkeville':
        if level >= 20:
            X = 35
            Y = -75
        else:
            print("You don't have the appropriate level to fast travel here!")
    elif location == 'walterworth':
        if level >= 30:
            X = -100
            Y = -100
        else:
            print("You don't have the appropriate level to fast travel here!")
    elif location == 'river':
        if level >= 20:
            X = 150
            Y = 150
        else:
            print("You don't have the appropriate level to fast travel here!")


def start():
    global firstTime
    global startInputActive
    global startChoice
    system(clear)
    load()
    changeLevel()
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
h = True

while True:
    if Play and not playfreezed:
        if h:
            print("You were spawned in " + area + ". The town's name is: Johncenangton.")
            print("Remember: you can get help by typing gameHelp or commands to view commands!")
            h = False
        while Play:
            changeLevel()
            if not houseChestOpened:
                chestChance = chest()
                if chestChance:
                    openChest('common')
                else:
                    pass
                houseChestOpened = True
            playInput = ''
            while playInput not in ['gamehelp()', 'gamehelp', 'commands()', 'commands', 'gonorth()', 'gonorth', 'gosouth()', 'gosouth', 'goeast()', 'goeast', 'gowest()', 'gowest', 'exit()', 'exit', 'save()', 'save', 'load()', 'load', 'viewstats()', 'viewstats', 'fasttravel']:
                changeLevel()
                playInput = input("[Play] > ").lower()
                if playInput == "gamehelp()" or playInput == "gamehelp" or playInput == "help()" or playInput == "help":
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
                elif playInput == "load()" or playInput == "load":
                    load()
                elif playInput == "viewstats()" or playInput == "viewstats":
                    Play = False
                    playfreezed = True
                    save()
                    viewStats()
                elif playInput == "eat":
                    print("  Please enter the argument for the function eat()")
                    Foodtype = ""
                    while Foodtype not in['beef', 'pork', 'chicken', 'carrot', 'potato', 'broccoli', 'orange', 'mango', 'banana']:
                        Foodtype = input("  [Eat argument] > ").lower()
                        eat(Foodtype)
                elif playInput == "drink":
                    print("  Please enter the argument for the function drink()")
                    BeverageType = ""
                    while BeverageType not in ['waterbottle', 'seawaterbottle', 'tea', 'orangejuicebottle', 'applejuicebottle']:
                        BeverageType = input("  [Drink argument] > ").lower()
                        drink(BeverageType)
                elif playInput == "clear" or playInput == "clear()":
                    system(clear)
                elif playInput == "fastTravel":
                    print("  Please enter the argument for the function fastTravel()")
                    Location = ""
                    while Location not in ["bandithideout1", "bandithideout2", "bandithideout3", "johncenangton", "bobuxbury", "monkeville", "walterworth", "river"]:
                        Location = input("  [Fast travel] > ").lower()
                        fastTravel(Location)
                else:
                    print("I don't know this phrase. Please read the manual.")

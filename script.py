# Computer science 8.1 adventure game
import json, os, random, sys, time
from os import system
from sys import platform

# Progress file
data = open(os.getcwd() + "/stats.json", 'r')
datastore = json.load(data)
data.close()

# Character statistics
hunger = datastore["data"]["characterInfo"]["hunger"]
health = datastore["data"]["characterInfo"]["health"]
water = datastore["data"]["characterInfo"]["water"]
xp = datastore["data"]["characterInfo"]["xp"]
X = datastore["data"]["characterInfo"]["x"]
Y = datastore["data"]["characterInfo"]["y"]
area = datastore["data"]["characterInfo"]["area"]
hasProgress = datastore["data"]["playerInfo"]["hasProgress"]
prompt = datastore["data"]["playerInfo"]["promptType"]
interval = 0.038

# Materials, resources
coins = datastore["data"]["materials"]["coins"]
gold = datastore["data"]["materials"]["gold"]
iron = datastore["data"]["materials"]["iron"]
bronze = datastore["data"]["materials"]["bronze"]
coal = datastore["data"]["materials"]["coal"]

# Food
beef = datastore["data"]["food"]["meat"]["beef"]
chicken = datastore["data"]["food"]["meat"]["chicken"]
carrot = datastore["data"]["food"]["vegetables"]["carrot"]
potato = datastore["data"]["food"]["vegetables"]["potato"]
oranges = datastore["data"]["food"]["fruits"]["oranges"]
banana = datastore["data"]["food"]["fruits"]["banana"]
sandwiches = datastore["data"]["food"]["other"]["sandwiches"]
# Beverages
waterBottles = datastore["data"]["food"]["beverages"]["waterBottles"]
seaWaterBottles = datastore["data"]["food"]["beverages"]["seaWaterBottles"]
orangeJuiceBottles = datastore["data"]["food"]["beverages"]["orangeJuiceBottles"]
appleJuiceBottles = datastore["data"]["food"]["beverages"]["appleJuiceBottles"]
tea = datastore["data"]["food"]["beverages"]["tea"]

# Variables
firstTime = datastore["data"]["playerInfo"]["firstTime"]
hasUnsavedProgress = False
playing = True
startInputActive = True
startChoice = 0
Play = False
play_freezed = False
houseChest = False
chestOpening = False
houseChestOpened = False
level = 1

# Quests
dining_room_quests = ["Throw away the cake on the table", "Clean up the table"]
kitchen_quests = ["Make a sandwich", "Clean the dishes"]
bathroom_quests = ["Fix the faucet", "Clean the ventilation"]
######
room1_quests = ["Fix the TV", "Close the window"]
bedroom1_quests = ["Kill the monster hiding under the bed", "Tidy up the cupboard"]
######
room2_quests = ["Change the light bulb in the lamp", "Adjust the frequency on the radio"]
bedroom2_quests = ["Sleep", "Clean the dust on the table"]
######
room3_quests = ["Remove cobweb on the ceiling", "Put the clothes inside the cupboard"]
bedroom3_quests = ["Wipe the mirror from dust", "Fix the bedside table"]
######
playroom_quests = ["Take all the toys to the storage"]
attic_quests = ["Unlock the safe", "Open the safe"]
############
# Quests
dining_room_quests_left = ["Throw away the cake on the table", "Clean up the table"]
kitchen_quests_left = ["Make a sandwich", "Clean the dishes"]
bathroom_quests_left = ["Fix the faucet", "Clean the ventilation"]
######
room1_quests_left = ["Fix the TV", "Close the window"]
bedroom1_quests_left = ["Kill the monster hiding under the bed", "Tidy up the cupboard"]
######
room2_quests_left = ["Change the light bulb in the lamp", "Adjust the frequency on the radio"]
bedroom2_quests_left = ["Sleep", "Clean the dust on the table"]
######
room3_quests_left = ["Remove cobweb on the ceiling", "Put the clothes inside the cupboard"]
bedroom3_quests_left = ["Wipe the mirror from dust", "Fix the bedside table"]
######
playroom_quests_left = ["Take all the toys to the storage"]
attic_quests_left = ["Unlock the safe", "Open the safe"]

# Quests taken
quests_in_progress = []


# Input variables
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

# Functions


def changeLevel():
    global xp
    global level
    if round(abs(xp / 50)) > level:
        level = round(abs(xp / 50))


def aprint(TEXT, SECONDS):
    for char in TEXT:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(SECONDS)


# Operating system check
if platform == "linux" or platform == "linux2" or platform == "darwin":
    clear = 'clear'
elif platform == "win32":
    clear = 'cls'
else:
    print("Your OS isn't supported.", 0.04)
    clear = str(input("In order to play the game, please enter the clear function of your terminal: "))


def save():  # Save function
    datastore["data"]["materials"]["coins"] = coins
    datastore["data"]["materials"]["gold"] = gold
    datastore["data"]["materials"]["iron"] = iron
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
    datastore["data"]["food"]["meat"]["chicken"] = chicken
    datastore["data"]["food"]["vegetables"]["carrot"] = carrot
    datastore["data"]["food"]["vegetables"]["potato"] = potato
    datastore["data"]["food"]["fruits"]["oranges"] = oranges
    datastore["data"]["food"]["fruits"]["banana"] = banana
    datastore["data"]["food"]["beverages"]["waterBottles"] = waterBottles
    datastore["data"]["food"]["beverages"]["seaWaterBottles"] = seaWaterBottles
    datastore["data"]["food"]["beverages"]["orangeJuiceBottles"] = orangeJuiceBottles
    datastore["data"]["food"]["beverages"]["appleJuiceBottles"] = appleJuiceBottles
    datastore["data"]["food"]["beverages"]["tea"] = tea
    datastore["data"]["playerInfo"]["firstTime"] = False
    datastore["data"]["playerInfo"]["hasProgress"] = True
    datastore["data"]["playerInfo"]["promptType"] = prompt
    saveddatastore = open("savedstats.json", 'w')
    json.dump(datastore, saveddatastore)
    saveddatastore.close()
    play()


def load():
    global coins, gold, iron, bronze, coal, health, hunger, water, xp, X, Y, area, beef, chicken, carrot, potato, oranges, banana
    global waterBottles, seaWaterBottles, orangeJuiceBottles, appleJuiceBottles, tea, firstTime, hasProgress, level
    saved = open(os.getcwd() + "/savedstats.json", 'r')
    saved_datastore = json.load(saved)
    saved.close()

    coins = saved_datastore["data"]["materials"]["coins"]
    gold = saved_datastore["data"]["materials"]["gold"]
    iron = saved_datastore["data"]["materials"]["iron"]
    bronze = saved_datastore["data"]["materials"]["bronze"]
    coal = saved_datastore["data"]["materials"]["coal"]
    health = saved_datastore["data"]["characterInfo"]["health"]
    hunger = saved_datastore["data"]["characterInfo"]["hunger"]
    water = saved_datastore["data"]["characterInfo"]["water"]
    level = saved_datastore["data"]["characterInfo"]["level"]
    xp = saved_datastore["data"]["characterInfo"]["xp"]
    X = saved_datastore["data"]["characterInfo"]["x"]
    Y = saved_datastore["data"]["characterInfo"]["y"]
    area = saved_datastore["data"]["characterInfo"]["area"]
    firstTime = saved_datastore["data"]["playerInfo"]["firstTime"]
    hasProgress = saved_datastore["data"]["playerInfo"]["hasProgress"]
    beef = saved_datastore["data"]["food"]["meat"]["beef"]
    chicken = saved_datastore["data"]["food"]["meat"]["chicken"]
    carrot = saved_datastore["data"]["food"]["vegetables"]["carrot"]
    potato = saved_datastore["data"]["food"]["vegetables"]["potato"]
    oranges = saved_datastore["data"]["food"]["fruits"]["oranges"]
    banana = saved_datastore["data"]["food"]["fruits"]["banana"]
    waterBottles = saved_datastore["data"]["food"]["beverages"]["waterBottles"]
    seaWaterBottles = saved_datastore["data"]["food"]["beverages"]["seaWaterBottles"]
    orangeJuiceBottles = saved_datastore["data"]["food"]["beverages"]["orangeJuiceBottles"]
    appleJuiceBottles = saved_datastore["data"]["food"]["beverages"]["appleJuiceBottles"]
    tea = saved_datastore["data"]["food"]["beverages"]["tea"]



def readManual(manualnum):
    global manualInput, helpInput, interval
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
    aprint("Type either 'back' to choose a chapter you want to view or 'menu' to exit the manual.\n", interval)
    manualInput = True
    while manualInput:
        choice1 = input("[root@game/manual]$ ").lower()
        if choice1 == 'back':
            manualInput = False
            gameHelp()
            helpInput = True
        elif choice1 == 'menu':
            manualInput = False
            start()
        else:
            aprint("Please enter a valid choice.\n", interval)


def gameHelp():  # A menu that asks you to enter the number of a desired chapter.
    global startInputActive, Play, helpInput, interval

    system(clear)
    print("============== Chapters ===============")
    print(" Chapter 1 - STARTING OUT\n Chapter 2 - RESOURCES AND MATERIALS\n Chapter 3 - FOOD\n Chapter 4 - LOCATIONS")
    aprint(" Please choose a chapter\n", interval)
    aprint(" To go back press enter\n", interval)
    helpInput = True
    while helpInput:
        help_choice = input("[root@game/helpMenu]$ ")
        if help_choice == '1':
            readManual(1)
            helpInput = False
        elif help_choice == '2':
            readManual(2)
            helpInput = False
        elif help_choice == '3':
            readManual(3)
            helpInput = False
        elif help_choice == '4':
            readManual(4)
            helpInput = False
        elif help_choice == '' and play_freezed is False:
            start()
            startInputActive = True
            helpInput = False
        elif help_choice == '' and play_freezed:
            Play = True
            helpInput = False
            play()
        else:
            aprint("Please enter a valid choice.\n", interval)


def look():
    global dining_room_quests_left, kitchen_quests_left, bathroom_quests_left, startInputActive, Play, play_freezed, interval
    hasChosenAQuest = False

    # Dining room quests
    if area == "diningroom":
        lookinput = ' '
        while lookinput not in ['y', 'n', ''] and not hasChosenAQuest:
            look_input = input("Would you like to list all available quests in the current room? [Y/n]:").lower()
            l_num = 1

            if look_input == 'y' or look_input == '':
                print("==-==-==-==-== Dining room quests ==-==-==-==-==")
                l_num = 1
                for i in dining_room_quests_left:
                    aprint(str(l_num) + ". " + i + "\n", interval)
                    l_num = l_num + 1
                print("==-==-==-==-==-==-==-==--==-==-==-==-==-==-==-==")
                quest_input = input("Would you like to take any of these quests? [Y/n] ")
                if quest_input in ['y', '', 'yes']:
                    quest_number = ' '

                    while quest_number not in ['1', '2']:
                        quest_number = input("What quest would you like to take? [1, 2] ").lower()
                        if quest_number == '1':
                            if "Throw away the cake on the table" in dining_room_quests_left:
                                if dining_room_quests_left[0] == "Throw away the cake on the table":
                                    quests_in_progress.append(dining_room_quests_left[0])
                                    del dining_room_quests_left[0]

                                    aprint("Quest taken!\n", interval)
                                    del look_input, quest_number, quest_input, l_num
                                    hasChosenAQuest = True
                                    play()
                                    break
                                else:
                                    quests_in_progress.append(dining_room_quests_left[0])
                                    del dining_room_quests_left[0]

                                    aprint("Quest taken!\n", interval)
                                    del look_input, quest_number, quest_input, l_num
                                    hasChosenAQuest = True
                                    play()
                                    break
                            else:
                                aprint("\n", interval)
                        elif quest_number == '2':
                            if "Clean up the table" in dining_room_quests_left:
                                if dining_room_quests_left[0] == "Clean up the table":
                                    quests_in_progress.append(dining_room_quests_left[0])
                                    del dining_room_quests_left[0]

                                    aprint("Quest taken!\n", interval)
                                    del look_input, quest_number, quest_input, l_num
                                    hasChosenAQuest = True
                                    play()
                                    break
                                else:
                                    quests_in_progress.append(dining_room_quests_left[1])
                                    del dining_room_quests_left[1]

                                    aprint("Quest taken!\n", interval)
                                    del look_input, quest_number, quest_input, l_num
                                    hasChosenAQuest = True
                                    play()
                                    break
                            else:
                                aprint("\n", interval)
                        else:
                            aprint("Please enter a valid quest number!\n", interval)
                        break

                    else:
                        del look_input, quest_number, quest_input, l_num
                        play()
                        break
                else:
                    aprint("There are no quests in this room.\n", interval)
                    del look_input, quest_number, quest_input, l_num
                    play()
                    break
            else:
                break

    # Hallway
    elif area == "hall":
        aprint("You are in the hallway. There are 11 doors.\n", interval)
        play()


    # Kitchen quests
    elif area == "kitchen":
        lookinput = ' '
        while lookinput not in ['y', 'n', ''] and not hasChosenAQuest:
            look_input = input("Would you like to list all available quests in the current room? [Y/n]:").lower()

            for i in kitchen_quests_left:
                if i == kitchen_quests[0]:
                    kitchen1 = True
                    if i == kitchen_quests[1]:
                        kitchen2 = True
                    else:
                        kitchen2 = False
                else:
                    kitchen1 = False

            if look_input == 'y' or look_input == '':
                if kitchen_quests_left[0] and kitchen_quests_left[1]:
                    print("==-==-==-==-== Kitchen quests ==-==-==-==-==")
                    l_num = 1
                    for i in kitchen_quests_left:
                        aprint(str(l_num) + ". " + i + "\n", interval)
                    print("==-==-==-==-==-==-==-==-==-==-==-==-==-==-==")
                    quest_input = input("Would you like to take any of these quests? [Y/n] ")
                    if quest_input in ['y', '', 'yes']:
                        quest_number = ' '

                        while quest_number not in ['1', '2']:
                            quest_number = input("What quest would you like to take? [1, 2] ").lower()
                            if quest_number == '1':
                                if kitchen_quests_left[0] and kitchen1:
                                    quests_in_progress.append(kitchen_quests_left[0])
                                    del kitchen_quests_left[0]

                                    aprint("Quest taken!\n", interval)
                                    del look_input, quest_number, quest_input, l_num
                                    hasChosenAQuest = True
                                    play()
                                    pass
                            elif quest_number == '2':
                                if kitchen_quests_left[1]:
                                    quests_in_progress.append(kitchen_quests_left[1])
                                    del kitchen_quests_left[1]

                                    aprint("Quest taken!\n", interval)
                                    del look_input, quest_number, quest_input, l_num
                                    hasChosenAQuest = True
                                    play()
                                    break
                            else:
                                aprint("Please enter a valid quest number!\n", interval)
                            break
                    else:
                        del look_input, quest_number, quest_input, l_num
                        play()
                        break
                else:
                    aprint("There are no quests in this room.\n", interval)
                    del look_input, quest_number, quest_input, l_num
                    play()
                    break
            else:
                break

    # Bathroom quests
    elif area == "bathroom":
        lookinput = ' '
        while lookinput not in ['y', 'n', ''] and not hasChosenAQuest:
            look_input = input("Would you like to list all available quests in the current room? [Y/n]:").lower()
            l_num = 1

            if look_input == 'y' or look_input == '':
                if bathroom_quests_left[0] and bathroom_quests_left[1]:
                    print("==-==-==-==-== Bathroom quests ==-==-==-==-==")
                    l_num = 1
                    for i in bathroom_quests_left:
                        aprint(str(l_num) + ". " + i + ",\n", interval)
                        l_num = l_num + 1
                    print("==-==-==-==-==-==-==--==-==-==-==-==-==-==-==")
                    quest_input = input("Would you like to take any of these quests? [Y/n] ")
                    if quest_input in ['y', '', 'yes']:
                        quest_number = ' '

                        while quest_number not in ['1', '2']:
                            quest_number = input("What quest would you like to take? [1, 2] ").lower()
                            if quest_number == '1':
                                if bathroom_quests_left[0]:
                                    quests_in_progress.append(bathroom_quests_left[0])
                                    del bathroom_quests_left[0]

                                    aprint("Quest taken!\n", interval)
                                    del look_input, quest_number, quest_input, l_num
                                    hasChosenAQuest = True
                                    play()
                                    pass
                            elif quest_number == '2':
                                if bathroom_quests_left[1]:
                                    quests_in_progress.append(bathroom_quests_left[1])
                                    del bathroom_quests_left[1]

                                    aprint("Quest taken!\n", interval)
                                    del look_input, quest_number, quest_input, l_num
                                    hasChosenAQuest = True
                                    play()
                                    break
                            else:
                                aprint("Please enter a valid quest number!\n", interval)
                            break
                    else:
                        del look_input, quest_number, quest_input, l_num
                        play()
                        break
                else:
                    aprint("There are no quests in this room.\n", interval)
                    del look_input, quest_number, quest_input, l_num
                    play()
                    break
            else:
                break

    # Room 1 quests
    elif area == "room1":
        lookinput = ' '
        while lookinput not in ['y', 'n', ''] and not hasChosenAQuest:
            look_input = input("Would you like to list all available quests in the current room? [Y/n]:").lower()
            l_num = 1

            if look_input == 'y' or look_input == '':
                if room1_quests_left[0] and room1_quests_left[1]:
                    print("==-==-==-==-== Room 1 quests ==-==-==-==-==")
                    l_num = 1
                    for i in room1_quests_left:
                        aprint(str(l_num) + ". " + i, interval)
                    print("==-==-==-==-==-==-==-=-==-==-==-==-==-==-==")
                    quest_input = input("Would you like to take any of these quests? [Y/n] ")
                    if quest_input in ['y', '', 'yes']:
                        quest_number = ' '

                        while quest_number not in ['1', '2']:
                            quest_number = input("What quest would you like to take? [1, 2] ").lower()
                            if quest_number == '1':
                                if room1_quests_left[0]:
                                    quests_in_progress.append(room1_quests_left[0])
                                    del room1_quests_left[0]

                                    aprint("Quest taken!\n", interval)
                                    del look_input, quest_number, quest_input, l_num
                                    hasChosenAQuest = True
                                    play()
                                    pass
                            elif quest_number == '2':
                                if room1_quests_left[1]:
                                    quests_in_progress.append(room1_quests_left[1])
                                    del room1_quests_left[1]

                                    aprint("Quest taken!\n", interval)
                                    del look_input, quest_number, quest_input, l_num
                                    hasChosenAQuest = True
                                    play()
                                    break
                            else:
                                aprint("Please enter a valid quest number!\n", interval)
                            break
                    else:
                        del look_input, quest_number, quest_input, l_num
                        play()
                        break
                else:
                    aprint("There are no quests in this room.\n", interval)
                    del look_input, quest_number, quest_input, l_num
                    play()
                    break
            else:
                break

    # Bedroom 1
    elif area == "bedroom1":
        lookinput = ' '
        while lookinput not in ['y', 'n', ''] and not hasChosenAQuest:
            look_input = input("Would you like to list all available quests in the current room? [Y/n]:").lower()
            l_num = 1

            if look_input == 'y' or look_input == '':
                if bedroom1_quests_left[0] and bedroom1_quests_left[1]:
                    print("==-==-==-==-== Bedroom 1 quests ==-==-==-==-==")
                    l_num = 1
                    for i in bedroom1_quests_left:
                        aprint(str(l_num) + ". " + i, interval)
                    print("==-==-==-==-==-==-==-=-==-==-==-==-==-==-==-==")
                    quest_input = input("Would you like to take any of these quests? [Y/n] ")
                    if quest_input in ['y', '', 'yes']:
                        quest_number = ' '

                        while quest_number not in ['1', '2']:
                            quest_number = input("What quest would you like to take? [1, 2] ").lower()
                            if quest_number == '1':
                                if bedroom1_quests_left[0]:
                                    quests_in_progress.append(bedroom1_quests_left[0])
                                    del bedroom1_quests_left[0]

                                    aprint("Quest taken!\n", interval)
                                    del look_input, quest_number, quest_input, l_num
                                    hasChosenAQuest = True
                                    play()
                                    pass
                            elif quest_number == '2':
                                if bedroom1_quests_left[1]:
                                    quests_in_progress.append(bedroom1_quests_left[1])
                                    del bedroom1_quests_left[1]

                                    aprint("Quest taken!\n", interval)
                                    del look_input, quest_number, quest_input, l_num
                                    hasChosenAQuest = True
                                    play()
                                    break
                            else:
                                aprint("Please enter a valid quest number!\n", interval)
                            break
                    else:
                        del look_input, quest_number, quest_input, l_num
                        play()
                        break
                else:
                    aprint("There are no quests in this room.\n", interval)
                    del look_input, quest_number, quest_input, l_num
                    play()
                    break
            else:
                break

    # Room 2
    elif area == "room2":
        lookinput = ' '
        while lookinput not in ['y', 'n', ''] and not hasChosenAQuest:
            look_input = input("Would you like to list all available quests in the current room? [Y/n]:").lower()
            l_num = 1

            if look_input == 'y' or look_input == '':
                if room2_quests_left[0] and room2_quests_left[1]:
                    print("==-==-==-==-== Room 2 quests ==-==-==-==-==")
                    l_num = 1
                    for i in room2_quests_left:
                        aprint(str(l_num) + "." + i, interval)
                    print("==-==-==-==-==-==-==-=-==-==-==-==-==-==-==")
                    quest_input = input("Would you like to take any of these quests? [Y/n] ")
                    if quest_input in ['y', '', 'yes']:
                        quest_number = ' '

                        while quest_number not in ['1', '2']:
                            quest_number = input("What quest would you like to take? [1, 2] ").lower()
                            if quest_number == '1':
                                if room2_quests_left[0]:
                                    quests_in_progress.append(room2_quests_left[0])
                                    del room2_quests_left[0]

                                    aprint("Quest taken!\n", interval)
                                    del look_input, quest_number, quest_input, l_num
                                    hasChosenAQuest = True
                                    play()
                                    pass
                            elif quest_number == '2':
                                if room2_quests_left[1]:
                                    quests_in_progress.append(room2_quests_left[1])
                                    del room2_quests_left[1]

                                    aprint("Quest taken!\n", interval)
                                    del look_input, quest_number, quest_input, l_num
                                    hasChosenAQuest = True
                                    play()
                                    break
                            else:
                                aprint("Please enter a valid quest number!\n", interval)
                            break
                    else:
                        del look_input, quest_number, quest_input, l_num
                        play()
                        break
                else:
                    aprint("There are no quests in this room.\n", interval)
                    del look_input, quest_number, quest_input, l_num
                    play()
                    break
            else:
                break

    # Bedroom 2
    elif area == "bedroom2":
        lookinput = ' '
        while lookinput not in ['y', 'n', ''] and not hasChosenAQuest:
            look_input = input("Would you like to list all available quests in the current room? [Y/n]:").lower()
            l_num = 1

            if look_input == 'y' or look_input == '':
                if bedroom2_quests_left[0] and bedroom2_quests_left[1]:
                    print("==-==-==-==-== Bedroom 2 quests ==-==-==-==-==")
                    l_num = 1
                    for i in bedroom2_quests_left:
                        aprint(str(l_num) + "." + i + "\n", interval)
                    print("==-==-==-==-==-==-==-=-==-==-==-==-==-==-==-==")
                    quest_input = input("Would you like to take any of these quests? [Y/n] ")
                    if quest_input in ['y', '', 'yes']:
                        quest_number = ' '

                        while quest_number not in ['1', '2']:
                            quest_number = input("What quest would you like to take? [1, 2] ").lower()
                            if quest_number == '1':
                                if bedroom2_quests_left[0]:
                                    quests_in_progress.append(bedroom2_quests_left[0])
                                    del bedroom2_quests_left[0]

                                    aprint("Quest taken!\n", interval)
                                    del look_input, quest_number, quest_input, l_num
                                    hasChosenAQuest = True
                                    play()
                                    pass
                            elif quest_number == '2':
                                if bedroom2_quests_left[1]:
                                    quests_in_progress.append(bedroom2_quests_left[1])
                                    del bedroom2_quests_left[1]

                                    aprint("Quest taken!\n", interval)
                                    del look_input, quest_number, quest_input, l_num
                                    hasChosenAQuest = True
                                    play()
                                    break
                            else:
                                aprint("Please enter a valid quest number!\n", interval)
                            break
                    else:
                        del look_input, quest_number, quest_input, l_num
                        play()
                        break
                else:
                    aprint("There are no quests in this room.\n", interval)
                    del look_input, quest_number, quest_input, l_num
                    play()
                    break
            else:
                break

    # Room 3
    elif area == "room3":
        lookinput = ' '
        while lookinput not in ['y', 'n', ''] and not hasChosenAQuest:
            look_input = input("Would you like to list all available quests in the current room? [Y/n]:").lower()
            l_num = 1

            if look_input == 'y' or look_input == '':
                if room3_quests_left[0] and room3_quests_left[1]:
                    print("==-==-==-==-== Room 3 quests ==-==-==-==-==")
                    l_num = 1
                    for i in room3_quests_left:
                        aprint(str(l_num) + "." + i + "\n", interval)
                    print("==-==-==-==-==-==-==-=-==-==-==-==-==-==-==")
                    quest_input = input("Would you like to take any of these quests? [Y/n] ")
                    if quest_input in ['y', '', 'yes']:
                        quest_number = ' '

                        while quest_number not in ['1', '2']:
                            quest_number = input("What quest would you like to take? [1, 2] ").lower()
                            if quest_number == '1':
                                if room3_quests_left[0]:
                                    quests_in_progress.append(room3_quests_left[0])
                                    del room3_quests_left[0]

                                    aprint("Quest taken!\n", interval)
                                    del look_input, quest_number, quest_input, l_num
                                    hasChosenAQuest = True
                                    play()
                                    pass
                            elif quest_number == '2':
                                if room3_quests_left[1]:
                                    quests_in_progress.append(room3_quests_left[1])
                                    del room3_quests_left[1]

                                    aprint("Quest taken!\n", interval)
                                    del look_input, quest_number, quest_input, l_num
                                    hasChosenAQuest = True
                                    play()
                                    break
                            else:
                                aprint("Please enter a valid quest number!\n", interval)
                            break
                    else:
                        del look_input, quest_number, quest_input, l_num
                        play()
                        break
                else:
                    aprint("There are no quests in this room.\n", interval)
                    del look_input, quest_number, quest_input, l_num
                    play()
                    break
            else:
                break

    # Bedroom 3
    elif area == "bedroom3":
        lookinput = ' '
        while lookinput not in ['y', 'n', ''] and not hasChosenAQuest:
            look_input = input("Would you like to list all available quests in the current room? [Y/n]:").lower()
            l_num = 1

            if look_input == 'y' or look_input == '':
                if bedroom3_quests_left[0] and bedroom3_quests_left[1]:
                    print("==-==-==-==-== Bedroom 3 quests ==-==-==-==-==")
                    l_num = 1
                    for i in bedroom3_quests_left:
                        aprint(str(l_num) + "." + i + "\n", interval)
                    print("==-==-==-==-==-==-==-=-==-==-==-==-==-==-==-==")
                    quest_input = input("Would you like to take any of these quests? [Y/n] ")
                    if quest_input in ['y', '', 'yes']:
                        quest_number = ' '

                        while quest_number not in ['1', '2']:
                            quest_number = input("What quest would you like to take? [1, 2] ").lower()
                            if quest_number == '1':
                                if bedroom3_quests_left[0]:
                                    quests_in_progress.append(bedroom3_quests_left[0])
                                    del bedroom3_quests_left[0]

                                    aprint("Quest taken!\n", interval)
                                    del look_input, quest_number, quest_input, l_num
                                    hasChosenAQuest = True
                                    play()
                                    pass
                            elif quest_number == '2':
                                if bedroom3_quests_left[1]:
                                    quests_in_progress.append(bedroom3_quests_left[1])
                                    del bedroom3_quests_left[1]

                                    aprint("Quest taken!\n", interval)
                                    del look_input, quest_number, quest_input, l_num
                                    hasChosenAQuest = True
                                    play()
                                    break
                            else:
                                aprint("Please enter a valid quest number!\n", interval)
                            break
                    else:
                        del look_input, quest_number, quest_input, l_num
                        play()
                        break
                else:
                    aprint("There are no quests in this room.\n", interval)
                    del look_input, quest_number, quest_input, l_num
                    play()
                    break
            else:
                break

    # Playroom
    elif area == "playroom":
        lookinput = ' '
        while lookinput not in ['y', 'n', ''] and not hasChosenAQuest:
            look_input = input("Would you like to list all available quests in the current room? [Y/n]:").lower()
            l_num = 1

            if look_input == 'y' or look_input == '':
                if playroom_quests_left[0] and playroom_quests_left[1]:
                    print("==-==-==-==-== Playroom 3 quests ==-==-==-==-==")
                    l_num = 1
                    for i in playroom_quests_left:
                        aprint(str(l_num) + "." + i + "\n", interval)
                    print("==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==")
                    quest_input = input("Would you like to take any of these quests? [Y/n] ")
                    if quest_input in ['y', '', 'yes']:
                        quest_number = ' '

                        while quest_number not in ['1', '2']:
                            quest_number = input("What quest would you like to take? [1, 2] ").lower()
                            if quest_number == '1':
                                if playroom_quests_left[0]:
                                    quests_in_progress.append(playroom_quests_left[0])
                                    del playroom_quests_left[0]

                                    aprint("Quest taken!\n", interval)
                                    del look_input, quest_number, quest_input, l_num
                                    hasChosenAQuest = True
                                    play()
                                    pass
                            elif quest_number == '2':
                                if playroom_quests_left[1]:
                                    quests_in_progress.append(playroom_quests_left[1])
                                    del playroom_quests_left[1]

                                    aprint("Quest taken!\n", interval)
                                    del look_input, quest_number, quest_input, l_num
                                    hasChosenAQuest = True
                                    play()
                                    break
                            else:
                                aprint("Please enter a valid quest number!\n", interval)
                            break
                    else:
                        del look_input, quest_number, quest_input, l_num
                        play()
                        break
                else:
                    aprint("There are no quests in this room.\n", interval)
                    del look_input, quest_number, quest_input, l_num
                    play()
                    break
            else:
                break

    # Attic
    elif area == "attic":
        lookinput = ' '
        while lookinput not in ['y', 'n', ''] and not hasChosenAQuest:
            look_input = input("Would you like to list all available quests in the current room? [Y/n]:").lower()
            l_num = 1

            if look_input == 'y' or look_input == '':
                if attic_quests_left[0] and attic_quests_left[1]:
                    print("==-==-==-==-== Attic quests ==-==-==-==-==")
                    l_num = 1
                    for i in attic_quests_left:
                        aprint(str(l_num) + "." + i + "\n", interval)
                    print("==-==-==-==-==-==-==--==-==-==-==-==-==-==")
                    quest_input = input("Would you like to take any of these quests? [Y/n] ")
                    if quest_input in ['y', '', 'yes']:
                        quest_number = ' '

                        while quest_number not in ['1', '2']:
                            quest_number = input("What quest would you like to take? [1, 2] ").lower()
                            if quest_number == '1':
                                if attic_quests_left[0]:
                                    quests_in_progress.append(attic_quests_left[0])
                                    del attic_quests_left[0]

                                    aprint("Quest taken!\n", interval)
                                    del look_input, quest_number, quest_input, l_num
                                    hasChosenAQuest = True
                                    play()
                                    pass
                            elif quest_number == '2':
                                if attic_quests_left[1]:
                                    quests_in_progress.append(attic_quests_left[1])
                                    del attic_quests_left[1]

                                    aprint("Quest taken!\n", interval)
                                    del look_input, quest_number, quest_input, l_num
                                    hasChosenAQuest = True
                                    play()
                                    break
                            else:
                                aprint("Please enter a valid quest number!\n", interval)
                            break
                    else:
                        del look_input, quest_number, quest_input, l_num
                        play()
                        break
                else:
                    aprint("There are no quests in this room.\n", interval)
                    del look_input, quest_number, quest_input, l_num
                    play()
                    break
            else:
                break

    else:
        aprint("what\n", interval)


def Commands():
    global interval
    system(clear)
    print(commands)
    aprint("Press enter to go back... ", interval)
    input("")
    play()


def chest():
    chest_available = random.randint(1, 2)
    if chest_available < 2:
        return False
    elif chest_available > 1:
        return True
    return


def openChest(chesttype):
    global Play, play_freezed, chestOpening, interval, carrot, chicken, iron

    Play = False
    play_freezed = True
    loot = False

    if str(chesttype) == 'common':
        aprint("There is a common chest inside the house. Would you like to open it? (Y/n) ", interval)
        chest_input = " "
        while chest_input not in ['y', 'yes', '']:
            chest_input = input().lower()
            if chest_input == 'y' or chest_input == 'yes':
                chest_carrot = random.randint(1, 2)
                if chest_carrot == 1:
                    aprint("You have found a carrot! Chance: 50%\n", interval)
                    carrot = carrot + 1
                    loot = True
                else:
                    continue
                del chest_carrot

                chest_chicken = random.randint(1, 3)
                if chest_chicken == 1:
                    aprint("You have found a chicken! Chance: 33%\n", interval)
                    chicken = chicken + 1
                    loot = True
                else:
                    continue
                del chest_chicken

                chest_iron = random.randint(1, 4)
                if chest_iron == 1:
                    aprint("You have found an iron ingot! Chance: 25%\n", interval)
                    iron = iron + 1
                    loot = True
                else:
                    continue
                del chest_iron

                Play = False
                play_freezed = False
                play()
            else:
                Play = False
                play_freezed = False
                play()
        if not loot:
            aprint("Nothing in the chest.\n", interval)


def play():
    global startInputActive, play_freezed, Play

    startInputActive = False
    Play = True
    play_freezed = False


def goNorth():
    global Y, X, level, area, interval

    cy = Y + .5

    # The bathroom
    if cy == 2 and X == -1 and level < 2:
        aprint("Your level is too low to enter the bathroom.\n", interval)

    # Primary rooms
    elif cy == 4 and X == -1 and level < 2:
        aprint("Your level is too low to enter the first room.\n", interval)
    elif cy == 4 and X == -2 and level < 2:
        aprint("Your level is too low to enter the first bedroom.\n", interval)

    # Secondary rooms
    elif cy == 6 and X == -1 and level < 3:
        aprint("Your level is too low to enter the second room.\n", interval)
    elif cy == 6 and X == -2 and level < 3:
        aprint("Your level is too low to enter the second bedroom.\n", interval)

    # Tertiary rooms
    elif cy == 8 and X == -1 and level < 4:
        aprint("Your level is too low to enter the third room.\n", interval)
    elif cy == 8 and X == -2 and level < 4:
        aprint("Your level is too low to enter the third bedroom.\n", interval)

    # The play room
    elif cy == 4 and X == 2 and level < 3 or cy == 4 and X == 3 and level < 3:
        aprint("Your level is too low to enter the play room\n", interval)

    # The attic
    elif X == 10 and X == 0 and level < 4 or cy == 10 and X == 1 and level < 4:
        aprint("Your level is too low to enter the attic.\n", interval)

    else:
        Y = Y + .5
        # The bathroom
        if Y == 2 and X == -1:
            area = "bathroom"

        # Primary rooms
        elif Y == 4 and X == -1:
            area = "room1"
        elif Y == 4 and X == -2:
            area = "bedroom1"

        # Secondary rooms
        elif Y == 6 and X == -1:
            area = "room2"
        elif Y == 6 and X == -2:
            area = "bedroom2"

        # Tertiary rooms
        elif Y == 8 and X == -1:
            area = "room3"
        elif Y == 8 and X == -2:
            area = "bedroom3"

        # The kitchen
        elif Y == 1 and X == 2:
            area = "diningroom"
        elif Y == 2 and X == 2:
            area = "kitchen"

        # The play room
        elif Y == 4 and X == 2 and level < 3 or Y == 4 and X == 3 and level < 3:
            area = "playroom"

        # The attic
        elif Y == 10 and X == 0 and level < 4 or Y == 10 and X == 1 and level < 4:
            area = "attic"
        else:
            area = "hall"
    play()


def goSouth():
    global Y, X, level, area, interval

    cy = Y - .5

    # The bathroom
    if cy == 2 and X == -1 and level < 2:
        aprint("Your level is too low to enter the bathroom.\n", interval)

    # Primary rooms
    elif cy == 4 and X == -1 and level < 2:
        aprint("Your level is too low to enter the first room.\n", interval)
    elif cy == 4 and X == -2 and level < 2:
        aprint("Your level is too low to enter the first bedroom.\n", interval)

    # Secondary rooms
    elif cy == 6 and X == -1 and level < 3:
        aprint("Your level is too low to enter the second room.\n", interval)
    elif cy == 6 and X == -2 and level < 3:
        aprint("Your level is too low to enter the second bedroom.\n", interval)

    # Tertiary rooms
    elif cy == 8 and X == -1 and level < 4:
        aprint("Your level is too low to enter the third room.\n", interval)
    elif cy == 8 and X == -2 and level < 4:
        aprint("Your level is too low to enter the third bedroom.\n", interval)

    # The play room
    elif cy == 4 and X == 2 and level < 3 or cy == 4 and X == 3 and level < 3:
        aprint("Your level is too low to enter the play room\n", interval)

    # The attic
    elif X == 10 and X == 0 and level < 4 or cy == 10 and X == 1 and level < 4:
        aprint("Your level is too low to enter the attic.\n", interval)

    else:
        Y = Y - .5
        # The bathroom
        if Y == 2 and X == -1:
            area = "bathroom"

        # Primary rooms
        elif Y == 4 and X == -1:
            area = "room1"
        elif Y == 4 and X == -2:
            area = "bedroom1"

        # Secondary rooms
        elif Y == 6 and X == -1:
            area = "room2"
        elif Y == 6 and X == -2:
            area = "bedroom2"

        # Tertiary rooms
        elif Y == 8 and X == -1:
            area = "room3"
        elif Y == 8 and X == -2:
            area = "bedroom3"

        # The kitchen
        elif Y == 1 and X == 2:
            area = "diningroom"
        elif Y == 2 and X == 2:
            area = "kitchen"

        # The play room
        elif Y == 4 and X == 2 and level < 3 or Y == 4 and X == 3 and level < 3:
            area = "playroom"

        # The attic
        elif Y == 10 and X == 0 and level < 4 or Y == 10 and X == 1 and level < 4:
            area = "attic"
        else:
            area = "hall"
    play()


def goEast():
    global Y, X, level, area, interval

    cx = X + .5

    # The bathroom
    if Y == 2 and X == -1 and level < 2:
        aprint("Your level is too low to enter the bathroom.\n", interval)

    # Primary rooms
    elif Y == 4 and cx == -1 and level < 2:
        aprint("Your level is too low to enter the first room.\n", interval)
    elif Y == 4 and cx == -2 and level < 2:
        aprint("Your level is too low to enter the first bedroom.\n", interval)

    # Secondary rooms
    elif Y == 6 and cx == -1 and level < 3:
        aprint("Your level is too low to enter the second room.\n", interval)
    elif Y == 6 and cx == -2 and level < 3:
        aprint("Your level is too low to enter the second bedroom.\n", interval)

    # Tertiary rooms
    elif Y == 8 and cx == -1 and level < 4:
        aprint("Your level is too low to enter the third room.\n", interval)
    elif Y == 8 and cx == -2 and level < 4:
        aprint("Your level is too low to enter the third bedroom.\n", interval)

    # The play room
    elif Y == 4 and cx == 2 and level < 3 or Y == 4 and cx == 3 and level < 3:
        aprint("Your level is too low to enter the play room\n", interval)

    # The attic
    elif Y == 10 and X == 0 and level < 4 or Y == 10 and X == 1 and level < 4:
        aprint("Your level is too low to enter the attic.\n", interval)

    else:
        X = X + .5
        # The bathroom
        if Y == 2 and X == -1:
            area = "bathroom"

        # Primary rooms
        elif Y == 4 and X == -1:
            area = "room1"
        elif Y == 4 and X == -2:
            area = "bedroom1"

        # Secondary rooms
        elif Y == 6 and X == -1:
            area = "room2"
        elif Y == 6 and X == -2:
            area = "bedroom2"

        # Tertiary rooms
        elif Y == 8 and X == -1:
            area = "room3"
        elif Y == 8 and X == -2:
            area = "bedroom3"

        # The kitchen
        elif Y == 1 and X == 2:
            area = "diningroom"
        elif Y == 2 and X == 2:
            area = "kitchen"

        # The play room
        elif Y == 4 and X == 2 and level < 3 or Y == 4 and X == 3 and level < 3:
            area = "playroom"

        # The attic
        elif Y == 10 and X == 0 and level < 4 or Y == 10 and X == 1 and level < 4:
            area = "attic"
        else:
            area = "hall"
    play()


def goWest():
    global Y, X, level, area, interval

    cx = X - .5

    # The bathroom
    if Y == 2 and X == -1 and level < 2:
        aprint("Your level is too low to enter the bathroom.\n", interval)

    # Primary rooms
    elif Y == 4 and cx == -1 and level < 2:
        aprint("Your level is too low to enter the first room.\n", interval)
    elif Y == 4 and cx == -2 and level < 2:
        aprint("Your level is too low to enter the first bedroom.\n", interval)

    # Secondary rooms
    elif Y == 6 and cx == -1 and level < 3:
        aprint("Your level is too low to enter the second room.\n", interval)
    elif Y == 6 and cx == -2 and level < 3:
        aprint("Your level is too low to enter the second bedroom.\n", interval)

    # Tertiary rooms
    elif Y == 8 and cx == -1 and level < 4:
        aprint("Your level is too low to enter the third room.\n", interval)
    elif Y == 8 and cx == -2 and level < 4:
        aprint("Your level is too low to enter the third bedroom.\n", interval)

    # The play room
    elif Y == 4 and cx == 2 and level < 3 or Y == 4 and cx == 3 and level < 3:
        aprint("Your level is too low to enter the play room\n", interval)

    # The attic
    elif Y == 10 and X == 0 and level < 4 or Y == 10 and X == 1 and level < 4:
        aprint("Your level is too low to enter the attic.\n", interval)

    else:
        X = X - .5
        # The bathroom
        if Y == 2 and X == -1:
            area = "bathroom"

        # Primary rooms
        elif Y == 4 and X == -1:
            area = "room1"
        elif Y == 4 and X == -2:
            area = "bedroom1"

        # Secondary rooms
        elif Y == 6 and X == -1:
            area = "room2"
        elif Y == 6 and X == -2:
            area = "bedroom2"

        # Tertiary rooms
        elif Y == 8 and X == -1:
            area = "room3"
        elif Y == 8 and X == -2:
            area = "bedroom3"

        # The kitchen
        elif Y == 1 and X == 2:
            area = "diningroom"
        elif Y == 2 and X == 2:
            area = "kitchen"

        # The play room
        elif Y == 4 and X == 2 and level < 3 or Y == 4 and X == 3 and level < 3:
            area = "playroom"

        # The attic
        elif Y == 10 and X == 0 and level < 4 or Y == 10 and X == 1 and level < 4:
            area = "attic"
        else:
            area = "hall"

    play()


def viewStats():
    system(clear)
    aprint("========== Character info ===============\n", 0.03)
    aprint("     Health: " + str(health) + "\n", 0.03)
    aprint("     Hunger: " + str(hunger) + "\n", 0.03)
    aprint("     Water: " + str(water) + "\n", 0.03)
    aprint("     XP: " + str(xp) + "\n", 0.03)
    aprint("     Level: " + str(level) + "\n", 0.03)
    aprint("     Coordinates: (" + str(X) + ", " + str(Y) + ")\n", 0.03)
    aprint("     Area: " + str(area) + "\n", 0.03)

    aprint("============ Inventory: Food ============\n", 0.03)
    aprint("     Beef: " + str(beef) + "\n", 0.03)
    aprint("     Chicken: " + str(chicken) + "\n", 0.03)
    aprint("     Carrots: " + str(carrot) + "\n", 0.03)
    aprint("     Potatoes: " + str(potato) + "\n", 0.03)
    aprint("     Oranges: " + str(oranges) + "\n", 0.03)
    aprint("     Bananas: " + str(banana) + "\n", 0.03)
    aprint("     Sandwiches: " + str(sandwiches) + "\n", 0.03)

    aprint("========= Inventory: Beverages ==========\n", 0.03)
    aprint("     Water Bottles: " + str(waterBottles) + "\n", 0.03)
    aprint("     Sea water bottles: " + str(seaWaterBottles) + "\n", 0.03)
    aprint("     Tea: " + str(tea) + "\n", 0.03)
    aprint("     Orange juice bottles: " + str(orangeJuiceBottles) + "\n", 0.03)
    aprint("     Apple juice bottles: " + str(appleJuiceBottles) + "\n", 0.03)
    aprint("Press any key to continue... ", interval)
    input("")
    if not Play and play_freezed is True:
        play()
    else:
        start()


# This function lists all available quests
def listQuests():
    global interval
    aprint("You have " + len(quests_in_progress) + " quests. \n", interval)
    aprint("Would you like to list all quests in progress? [Y/n]\n", interval)
    lq_input = input("$ ").lower()
    if lq_input in ['y', '', 'yes']:
        for i in quests_in_progress:
            aprint(i, interval)
        aprint("Press any key to continue... ", interval)
        input()


def startQuest():
    global xp, interval
    aprint("What quest would you like to start?\n", interval)
    f = 1
    questType = ""

    for i in quests_in_progress:
        aprint(str(f) + ". " + i + "\n", interval)
        f = f + 1

    usrinput = int(input(""))

    try:
        if quests_in_progress[usrinput - 1] == "Throw away the cake on the table":
            questType = "Throw away the cake on the table"
        elif quests_in_progress[usrinput - 1] == "Clean up the table":
            questType = "Clean up the table"
        elif quests_in_progress[usrinput - 1] == "Make a sandwich":
            questType = "Make a sandwich"
        elif quests_in_progress[usrinput - 1] == "Clean the dishes":
            questType = "Clean the dishes"
        elif quests_in_progress[usrinput - 1] == "Fix the faucet":
            questType = "Fix the faucet"
        elif quests_in_progress[usrinput - 1] == "Clean the ventilation":
            questType = "Clean the ventilation"
        elif quests_in_progress[usrinput - 1] == "Fix the TV":
            questType = "Fix the TV"
        elif quests_in_progress[usrinput - 1] == "Close the window":
            questType = "Close the window"
        elif quests_in_progress[usrinput - 1] == "Kill the monster hiding under the bed":
            questType = "Tidy up the cupboard"
        elif quests_in_progress[usrinput - 1] == "Tidy up the cupboard":
            questType = "Tidy up the cupboard"
        elif quests_in_progress[usrinput - 1] == "Change the light bulb in the lamp":
            questType = "Change the light bulb in the lamp"
        elif quests_in_progress[usrinput - 1] == "Adjust the frequency on the radio":
            questType = "Adjust the frequency on the radio"
        elif quests_in_progress[usrinput - 1] == "Sleep":
            questType = "Sleep"
        elif quests_in_progress[usrinput - 1] == "Clean the dust on the table":
            questType = "Clean the dust on the table"
        elif quests_in_progress[usrinput - 1] == "Remove cobweb on the ceiling":
            questType = "Remove cobweb on the ceiling"
        elif quests_in_progress[usrinput - 1] == "Put the clothes inside the cupboard":
            questType = "Put the clothes inside the cupboard"
        elif quests_in_progress[usrinput - 1] == "Wipe the mirror from dust":
            questType = "Wipe the mirror from dust"
        elif quests_in_progress[usrinput - 1] == "Fix the bedside table":
            questType = "Fix the bedside table"
        elif quests_in_progress[usrinput - 1] == "Take all the toys to the storage":
            questType = "Take all the toys to the storage"
        elif quests_in_progress[usrinput - 1] == "Unlock the safe":
            questType = "Unlock the safe"
        elif quests_in_progress[usrinput - 1] == "Open the safe":
            questType = "Open the safe"
    except:
        aprint("ok\n", interval)

    if questType == "Throw away the cake on the table":
        os.system(clear)

        finished = False
        while not finished:
            finished_e = False
            got = False
            Es = 0
            leftY = 5
            leftX = -2
            coordinates = [0, 0]

            aprint("Enter E 5 times to pick up the cake...\n", interval)
            while not finished_e:
                for _ in range(0, 5):
                    usrinput = input("Press > ").lower()
                    if usrinput != "e":
                        aprint("You must press E!\n", interval)
                        time.sleep(1.5)
                        os.system(clear)
                        break
                    elif usrinput == "e":
                        Es = Es + 1
                        continue

                if Es == 5:
                    break

            aprint("Use the WASD keys in order to move...\n", interval)
            time.sleep(2)

            while not got:
                os.system(clear)
                print("Y left: " + str(leftY) + "\nX left: " + str(leftX) + ".")
                key = input("> ").lower()
                if key == "w" and coordinates[1] < 5:
                    leftY = leftY - 1
                    coordinates[1] = coordinates[1] - 1
                    if leftY == 0 and leftX == 0:
                        break
                elif key == "w" and coordinates[1] > 5:
                    leftY = leftY + 1
                    coordinates[1] = coordinates[1] + 1
                    if leftY == 0 and leftX == 0:
                        break
                elif key == "s" and coordinates[1] < 5:
                    leftY = leftY - 1
                    coordinates[1] = coordinates[1] - 1
                    if leftY == 0 and leftX == 0:
                        break
                elif key == "s" and coordinates[1] > 5:
                    leftY = leftY + 1
                    coordinates[1] = coordinates[1] + 1
                    if leftY == 0 and leftX == 0:
                        break
                elif key == "a" and coordinates[0] < -2:
                    leftX = leftX - 1
                    coordinates[0] = coordinates[0] - 1
                    if leftY == 0 and leftX == 0:
                        break
                elif key == "a" and coordinates[0] > -2:
                    leftX = leftX + 1
                    coordinates[0] = coordinates[0] + 1
                    if leftY == 0 and leftX == 0:
                        break
                elif key == "d" and coordinates[0] > -2:
                    leftX = leftX - 1
                    coordinates[0] = coordinates[0] - 1
                    if leftY == 0 and leftX == 0:
                        break
                elif key == "d" and coordinates[0] < -2:
                    leftX = leftX + 1
                    coordinates[0] = coordinates[0] + 1
                    if leftY == 0 and leftX == 0:
                        break
                else:
                    pass

            aprint("Enter E 5 times to throw away the cake\n", interval)

            finished_e = False
            Es = 0
            while not finished_e:
                for _ in range(0, 5):
                    usrinput = input("> ").lower()
                    if usrinput != "e":
                        aprint("You must press E!\n", interval)
                        time.sleep(1.5)
                        os.system(clear)
                        break
                    elif usrinput == "e":
                        Es = Es + 1

                if Es == 5:
                    break

            os.system(clear)

            xp = xp + 50

            for element in quests_in_progress:
                if element == "Throw away the cake on the table":
                    quests_in_progress.remove(element)

            aprint("Successfully finished the quest! +50XP\n", interval)
            aprint("Press any key to continue... \n", interval)
            input()
            break

    elif questType == "Clean up the table":
        done = False
        os.system(clear)

        aprint("Use the Q and E keys to wipe the table\n", interval)

        wipesLeft = random.randint(5, 10)
        while not done:
            os.system(clear)
            print("Wipes left: " + str(wipesLeft) + ".")
            usrinput = input("> ").lower()
            if usrinput == "q":
                wipesLeft = wipesLeft - 1
                if wipesLeft == 0:
                    os.system(clear)
                    aprint("Wipes left: 0\n", 0.07)
                    xp = xp + 50
                    aprint("Successfully finished the quest! +50XP\n", interval)
                    time.sleep(1)
                    break
            elif usrinput == "e":
                wipesLeft = wipesLeft - 1
                if wipesLeft == 0:
                    os.system(clear)
                    print("Wipes left: 0")
                    xp = xp + 50

                    aprint("Successfully finished the quest! +50XP\n", interval)
                    time.sleep(1)
                    break
            else:
                aprint("You have to enter either Q or E\n", interval)
                time.sleep(1)

    elif questType == "Make a sandwich":
        done = False
        os.system(clear)
        ingredients_left = ["bread", "cucumbers", "cheese", "butter", "meat"]

        aprint("Take the ingredients from the fridge by typing their name", interval)

        while not done:
            os.system(clear)
            print("Ingredients left:")
            for ingredient in ingredients_left:
                print(ingredient)
            usrinput = input("> ").lower()
            if usrinput == "bread" and any("bread" in s for s in ingredients_left):
                ingredients_left.remove("bread")
                if not ingredients_left:
                    os.system(clear)
                    xp = xp + 50
                    aprint("Successfully finished the quest! +50XP\n", interval)

                    aprint("Enter any key to continue... ", interval)
                    input()
                    play()
                    break
            elif usrinput == "cucumbers" and any("cucumbers" in s for s in ingredients_left):
                ingredients_left.remove("cucumbers")
                if not ingredients_left:
                    os.system(clear)
                    xp = xp + 50
                    aprint("Successfully finished the quest! +50XP\n", interval)

                    input("Enter any key to continue... ")
                    play()
                    break
            elif usrinput == "cheese" and any("cheese" in s for s in ingredients_left):
                ingredients_left.remove("cheese")
                if not ingredients_left:
                    os.system(clear)
                    xp = xp + 50
                    aprint("Successfully finished the quest! +50XP\n", interval)

                    aprint("Enter any key to continue... ", interval)
                    input()
                    play()
                    break
            elif usrinput == "butter" and any("butter" in s for s in ingredients_left):
                ingredients_left.remove("butter")
                if not ingredients_left:
                    os.system(clear)
                    xp = xp + 50
                    aprint("Successfully finished the quest! +50XP\n", interval)

                    aprint("Enter any key to continue... ", interval)
                    input()
                    play()
                    break
            elif usrinput == "meat" and any("meat" in s for s in ingredients_left):
                ingredients_left.remove("meat")
                if not ingredients_left:
                    os.system(clear)
                    xp = xp + 50
                    aprint("Successfully finished the quest! +50XP\n", interval)

                    aprint("Enter any key to continue... ", interval)
                    input()
                    play()
                    break
            else:
                aprint("Please enter a valid ingredient\n", interval)

                time.sleep(1)

    elif questType == "Clean the dishes":
        done = False
        os.system(clear)
        obj_num = 1

        aprint("Complete the objectives by typing their number\n", interval)

        objectives = ["take soap", "take a sponge"]
        while not done:
            os.system(clear)
            print("Objectives left:\n", interval)

            for objective in objectives:
                print(str(obj_num) + objective)
                obj_num = obj_num + 1
            usrinput = input ("> ")
            if usrinput == "take soap":
                objectives.remove("take soap")
                if not objectives:
                    continue
            elif usrinput == "take a sponge":
                objectives.remove("take soap")
                if not objectives:
                    continue

            dishesLeft = 10
            cleanDone = False

            aprint("Use the A and D keys to clean the dishes...\n", interval)
            time.sleep(1)

            while not cleanDone:
                os.system(clear)
                print("Dishes left: " + str(dishesLeft) + "\n", interval)
                usrinput = input("> ").lower()
                if usrinput == "a":
                    dishesLeft = dishesLeft - 1
                    if dishesLeft == 0:
                        os.system(clear)
                        aprint("Successfully finished the quest! +50XP\n", interval)

                elif usrinput == "d":
                    dishesLeft = dishesLeft - 1
                    if dishesLeft == 0:
                        os.system(clear)
                        aprint("Successfully finished the quest! +50XP\n")
                else:
                    aprint("Enter either A or D.\n", interval)
                    time.sleep(1)
    elif questType == "Fix the faucet":
        done = False
        os.system(clear)
        left = 10

        aprint("Enter E to use the wrench\n", interval)

        while not done:
            os.system(clear)
            print("Left: " + str(left))
            usrinput = input("> ").lower()
            if usrinput == "e":
                left = left - 1
                if left == 0:
                    os.system(clear)
                    xp = xp + 50
                    aprint("Successfully finished the quest! +50XP\n", interval)
                    time.sleep(1)
                    break
            else:
                aprint("You have to enter E to use the wrench\n", interval)



def eat(foodtype):
    global hunger, beef, chicken, carrot, potato, oranges, banana, water, interval

    if foodtype == 'beef':
        if beef > 0:
            aprint("Before: hunger - " +  hunger +  "; water - " +  water +  ".\n", interval)
            hunger = hunger + 7
            water = water - 2
            aprint("After: hunger - " +  hunger +  "; water - " +  water +  ".\n", interval)
            play()
        else:
            aprint("You have 0 beef chops.")
            play()
    elif foodtype == "chicken":
        if chicken > 0:
            aprint("Before: hunger - " +  hunger + "; water - " + water + ".\n", interval)
            hunger = hunger + 6
            water = water - 1
            aprint("After: hunger - " + hunger + "; water - " + water + ".\n", interval)
            play()
        else:
            aprint("You have 0 chicken chops.\n", 0.07)
            play()
    elif foodtype == "carrot":
        if carrot > 0:
            aprint("Before: hunger - " +  hunger +  "; water - " +  water +  ".\n", interval)
            hunger = hunger + 4
            aprint("After: hunger - " +  hunger +  "; water - " +  water +  ".\n", interval)
            play()
        else:
            aprint("You have 0 carrots.\n", 0.07)
            play()
    elif foodtype == "potato":
        if potato > 0:
            aprint("Before: hunger - " +  hunger +  "; water - " +  water +  ".\n", interval)
            hunger = hunger + 3
            aprint("After: hunger - " +  hunger +  "; water - " +  water +  ".\n", interval)
            play()
        else:
            aprint("You have 0 potatoes.\n", 0.07)
            play()
    elif foodtype == "orange":
        if oranges > 0:
            aprint("Before: hunger - " +  hunger +  "; water - " +  water +  ".\n", interval)
            hunger = hunger + 2
            water = water + 3
            aprint("After: hunger - " +  hunger +  "; water - " +  water +  ".\n", interval)
            play()
        else:
            aprint("You have 0 oranges.\n", 0.07)
            play()
    elif foodtype == "banana":
        if banana > 0:
            aprint("Before: hunger - " +  hunger +  "; water - " +  water +  ".\n", interval)
            hunger = hunger + 1
            aprint("After: hunger - " +  hunger +  "; water - " +  water +  ".\n", interval)
            play()
        else:
            aprint("You have 0 bananas.\n", interval)
            play()
    else:
        aprint("Please enter a valid argument.\n", interval)
        play()


def drink(beveragetype):
    global hunger, water, waterBottles, seaWaterBottles, orangeJuiceBottles, appleJuiceBottles, tea, interval
    if beveragetype == 'waterbottle':
        if waterBottles > 0:
            aprint("Before: water - " + water + ".\n", interval)
            water = water + 5
            aprint("After: water - " + water + ".\n", interval)
            play()
        else:
            aprint("You have 0 water bottles.")
            play()
    elif beveragetype == "seawaterbottle":
        if seaWaterBottles > 0:
            aprint("Before: water - " + water + ".\n", interval)
            water = water - 3
            aprint("After: water - " + water +  ".\n", interval)
            play()
        else:
            aprint("You have 0 sea water bottles.\n", interval)
            play()
    elif beveragetype == "orangejuicebottle":
        if orangeJuiceBottles > 0:
            aprint("Before: water - " + water + ".\n", interval)
            water = water + 3
            aprint("After: water - " + water + ".\n", interval)
            play()
        else:
            aprint("You have 0 orange juice bottles.\n", interval)
            play()
    elif beveragetype == "applejuicebottle":
        if appleJuiceBottles > 0:
            aprint("Before: water - " + water + ".\n", interval)
            water = water + 3
            aprint("After: water - " + water + ".\n", interval)
            play()
        else:
            aprint("You have 0 apple juice bottles.\n", interval)
            play()
    elif beveragetype == "tea":
        if tea > 0:
            aprint("Before: water - " + water + ".\n", interval)
            water = water + 2
            aprint("After: water - " + water + ".\n", interval)
            play()
        else:
            aprint("You have 0 tea.\n", 0.07)
            play()
    else:
        aprint("Please enter a valid argument for the drink() function!\n", interval)
        play()


def start():
    global firstTime, startInputActive, startChoice, clear, prompt, interval
    startInputActive = True

    while startInputActive:
        system(clear)
        if hasProgress:
            aprint("Would you like to load your progress? [Y/n] ", interval)
            pin = input().lower()
            if pin == 'y':
                load()
            else:
                pass

        changeLevel()
        print("========================== Menu ==========================")
        print("Hello!")
        print("Choose an option:")
        print(" 1. Start playing the game,")
        print(" 2. Open the help menu,")
        print(" 3. View your statistics and inventory,")
        print(" 4. Open commands reference manual.")
        print(" 5. Customize the game")
        startChoice = 0
        startChoice = input("[root@game/start]$ ")
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
        elif startChoice == '5':
            os.system(clear)
            aprint("Choose the thing you want to change: \n", interval)
            print("1. The prompt")
            print("2. The interval between printing letters")
            aprint("Enter an option [1, 2] ", interval)
            cin = input()
            if cin == '1':
                os.system(clear)
                aprint("There are currently 4 types of prompts you can choose.\n", interval)
                print("1. [root@game/LOCATION LVL | XY(0, 0)]$ - bash")
                print("2. PS C:\game\LOCATION\LVL\XY(0,0) - windows powershell")
                print("3. C:\game\LOCATION\LVL\XY(0,0) - windows command line")
                print("4. Game-LVL-XY(0,0):~ LOCATION$ - mac command line")
                aprint("Choose the one you like... ", interval)
                pin = ""
                while pin not in ['1', '2', '3', '4']:
                    pin = input()
                    if pin == '1':
                        prompt = 1
                    elif pin == '2':
                        prompt = 2
                    elif pin == '3':
                        prompt = 3
                    elif pin == '4':
                        prompt = 4
                    else:
                        aprint("Enter a valid number\n", interval)
            elif cin == '2':
                os.system(clear)
                aprint("Enter the interval in seconds between each printed letter (default: 0.038)... ", 0.038)
                pin = float(input())
                interval = pin
                aprint("Successfully set interval! Enter any key to continue... ", interval)
                input()
                os.system(clear)
        else:
            aprint('Please enter a valid number!\n', interval)


start()
h = True

while True:
    if Play and not play_freezed:
        if h:
            aprint("You were spawned in the " + area + ".\n", interval)
            aprint("Remember: you can get help by typing gameHelp or commands to view commands!\nEnjoy!\n", interval)
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
            while playInput not in ['gamehelp()', 'gamehelp', 'help', 'help()', 'commands()',
                                    'commands', 'gonorth()', 'gonorth', 'gosouth()', 'gosouth',
                                    'goeast()', 'goeast', 'gowest()', 'gowest', 'exit()', 'exit',
                                    'save()', 'save', 'load()', 'load', 'viewstats()', 'viewstats',
                                    "look", "look()", "lookaround", "lookaround()", "startquest()",
                                    "startquest", 'listquests', 'listquests()']:
                changeLevel()
                if prompt == 1:
                    playInput = input("[root@game/" + area + " lvl" + str(level) + " | XY(" + str(X) + ", " + str(Y) + ")]$ ").lower()
                    pass
                elif prompt == 2:
                    playInput = input("PS C:\\game\\" + str(area) + "\\lvl" + str(level) + "\\XY(" + str(X) + "," + str(Y) + ") ")
                    pass
                elif prompt == 3:
                    playInput = input("C:\\game\\" + str(area) + "\\lvl" + str(level) + "\\XY(" + str(X) + "," + str(Y) + ") ")
                    pass
                elif prompt == 4:
                    playInput = input("Game-lvl" + str(level) + "-XY(" + str(X) + "," + str(Y) + "):~ " + area + "$ ")
                    pass

                if playInput in ["help", "gamehelp", "help()", "gamehelp()"]:
                    Play = False
                    play_freezed = True
                    gameHelp()

                elif playInput in ["commands", "commands()"]:
                    Play = False
                    play_freezed = True
                    Commands()

                elif playInput in ["gonorth", "gonorth()"]:
                    goNorth()

                elif playInput in ["gosouth", "gosouth()"]:
                    goSouth()

                elif playInput in ["goeast", "goeast()"]:
                    goEast()

                elif playInput in ["gowest", "gowest()"]:
                    goWest()

                elif playInput in ["exit", "exit()"]:
                    aprint("You have unsaved progress. Would you like to save it? [Y/n] ", interval)
                    usrinput = input()
                    if usrinput in ["y", "yes", ""]:
                        save()
                        exit()
                    else:
                        exit()

                elif playInput in ["save", "save()"]:
                    save()

                elif playInput in ["load", "load()"]:
                    load()

                elif playInput in ["look", "look()", "lookaround", "lookaround()"]:
                    look()

                # Prints out all the quests that were taken and not completed
                elif playInput in ["listquests", "listquests()"]:
                    blabla = False
                    # Checks whether the player has a quest active
                    try:
                        quests_in_progress[0]
                    # If yes,
                    except:
                        try:
                            quests_in_progress[1]
                        except:
                            aprint("You don't have any quests.\n", interval)
                            blabla = True
                        break

                    if not blabla:
                        for i in quests_in_progress:
                            print(i)
                    else:
                        pass

                elif playInput == "viewstats()" or playInput == "viewstats":
                    Play = False
                    play_freezed = True
                    usrinput = "123"
                    while usrinput not in ['y', 'n', '']:
                        aprint("Would you like to save your progress before viewing your stats? [Y/n] ", interval)
                        usrinput = input()
                        if usrinput == 'y' or usrinput == '':
                            save()
                        else:
                            break
                    viewStats()

                elif playInput == "eat":
                    aprint("  Please enter the type of food (can be found in commands list) ", interval)
                    Foodtype = ""
                    while Foodtype not in ['beef', 'chicken', 'carrot',
                                           'potato', 'orange', 'banana',
                                           "sandwiches"]:
                        Foodtype = input("").lower()
                        eat(Foodtype)

                elif playInput == "drink":
                    print("  Please enter the type of beverage (can be found in commands list) ", interval)
                    BeverageType = ""
                    while BeverageType not in ['waterbottle', 'seawaterbottle', 'tea', 'orangejuicebottle',
                                               'applejuicebottle']:
                        BeverageType = input("").lower()
                        drink(BeverageType)

                elif playInput in ["clear", "clear()"]:
                    system(clear)

                elif playInput in ["startquest", "startquest()"]:
                    startQuest()

                else:
                    aprint("I don't know the phrase '" + playInput + "'. Please read the manual.\n", interval)

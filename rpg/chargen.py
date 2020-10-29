import sys
import os
import time
from clint.textui import colored
from random import randint
from chillfunc import clear
clear()
print (' ')
print (' ')
print (' ')
print (' ')
print (' ')
print (' ')
print (' ')
print (' ')
print (' ')
print (' ')
print ('********************************************************************************')
print ('*                                                                              *')
print ('*                                                                              *')
print ('*                                                                              *')
print ("*                     Chill's RPG Engine Character Generator                   *")
print ('*                                                                              *')
print ('*                                 Version 0.6                                  *')
print ('*                                                                              *')
print ('*                                                                              *')
print ('*                                                                              *')
print ("*                                                                              *")
print ('********************************************************************************')
print (' ')
print (' ')
print (' ')
print (' ')
print (' ')



randy = input('Do you want to roll a random character? y/n: ')

clear()
    
print (' ')
print (' ')
print (' ')
print (' ')
print (' ')
print (' ')
print (' ')
    
if randy == "y":
    stats = randint(1,6)
    statp = randint(1,6)
    state = randint(1,6)
    statc = randint(1,6)
    stati = randint(1,6)
    stata = randint(1,6)
    statl = randint(1,6)
    
if randy == "n":
    print (' ')
    print (' ')
    print('You Have chosen to set your stats.')
    print (' ')
    stats = input('Please enter a number for Strength: ')
    statp = input('Please enter a number for Perception: ')
    state = input('Please enter a number for Endurance: ')
    statc = input('Please enter a number for Charisma: ')
    stati = input('Please enter a number for Intelligence: ')
    stata = input('Please enter a number for Agility: ')
    statl = input('Please enter a number for Luck: ')
    print('---------------------------------')
    print (' ')


playername = input('Enter a name: ');



clear()
print (' ')
print (' ')
print (' ')
print (' ')
print (' ')
print (' ')
print (' ')
print (' ')
print (' ')
print (' ')
print (' ')
print (' ')
print (' ')
print (' ')
print (' ')
print (' ')
print (' ')
print (' ')
print (' ')
print (' ')
print (' ')

print("Name: ", playername)
print ('-------------------------')
print ('Stats are: ')
print ('----------')
print ("Strength:", stats)
print ("Perception:", statp)
print ("Endurance:", state)
print ("Charisma:", statc)
print ("Intelligence:", stati)
print ("Agility:", stata)
print ("Luck:", statl)
print (' ')
print (' ')
print (' ')

print ('Keep', playername, "?")
reroll = input("y/n: ")

if reroll == "y":
    print('Saving Character...')
    filesavename = "." + playername + ".txt"
    fo = open(filesavename, "w")
    
    fo.write('xp: ')
    fo.write("1000")
    fo.write(',')
    
    fo.write('Name: ')
    fo.write(playername)
    fo.write(',')

    fo.write('Strength: ')
    fo.write(str(stats))
    fo.write(',')

    fo.write('Perception: ')
    fo.write(str(statp))
    fo.write(',')

    fo.write('Endurance: ')
    fo.write(str(state))
    fo.write(',')

    fo.write('Charisma: ')
    fo.write(str(statc))
    fo.write(',')

    fo.write('Intelligence: ')
    fo.write(str(stati))
    fo.write(',')

    fo.write('Agility: ')
    fo.write(str(stata))
    fo.write(',')

    fo.write('Luck: ')
    fo.write(str(statl))
    fo.write(',')

    fo.close()

if reroll == "n":
    os.execl(sys.executable, sys.executable, *sys.argv)
clear()
print (' ')
print (' ')
print (' ')
print (' ')
print (' ')
print (' ')
print (' ')
print (' ')
print (' ')
print (' ')
print ('********************************************************************************')
print ('*                                                                              *')
print ('*                                                                              *')
print ('*                                                                              *')
print ("*                     Chill's RPG Engine Inventory Creator                     *")
print ('*                                                                              *')
print ('*                                 Version 0.6                                  *')
print ('*                                                                              *')
print ('*                                                                              *')
print ('*                                                                              *')
print ("*                                                                              *")
print ('********************************************************************************')
print (' ')
print (' ')
print (' ')
print (' ')
print (' ')
print (' ')
time.sleep(2)
clear()



with open(filesavename, "r") as ins:
    array = []
    for line in ins:
        array.append(line)

lst = array


        
ins.close()







print (' ')
print (' ')
print (' ')
print (' ')
print (' ')
print (' ')
print (' ')
print (' ')
print (' ')
print (' ')
print ('********************************************************************************')
print ('*                                                                              *')
print ('*                        Choose a starting loadout:                            *')
print ('*                                                                              *')
print ("*                                                                              *")
print ('*            1.) Light                        2.) Medium                       *')
print ('*                                                                              *')
print ('*            3.) Heavy                        4.) Epic                         *')
print ('*                                                                              *')
print ('*                                                                              *')
print ("*                                                                              *")
print ('********************************************************************************')
print (' ')
print (' ')
print (' ')
print (' ')
print (' ')
print (' ')
option = input("Please choose an option: ")

if option == "1":
    print('Giving Loadout...')
    fo = open(filesavename, "a")
    fo.write("INVENTORY1")
    fo.write(',')
    fo.write("Money 50")
    fo.write(',')
    fo.write("Pistol_9mm")
    fo.write(',')
    fo.write("SMG_9mm")
    fo.write(',')
    fo.write("9mm Ammo 50")
    fo.close()
    import start.py
    

if option == "2":    
    print('Giving Loadout...')
    fo = open(filesavename, "a")
    fo.write("INVENTORY2")
    fo.write(',')
    fo.write("Money 100")
    fo.write(',')
    fo.write("Pistol_45")
    fo.write(',')
    fo.write("SMG_45")
    fo.write(',')
    fo.write(".45 Ammo 50")
    fo.close()
    import start.py
    
if option == "3":
    print('Giving Loadout...')
    fo = open(filesavename, "a")
    fo.write("INVENTORY3")
    fo.write(',')
    fo.write("Money 150")
    fo.write(',')
    fo.write("Pistol_45")
    fo.write(',')
    fo.write("AR_556")
    fo.write(',')
    fo.write("5.56 Ammo 50")
    fo.write(',')
    fo.write(".45 Ammo 20")
    fo.close()
    import start.py
    
if option == "4":    
    print('Good Luck...')
    fo = open(filesavename, "a")
    fo.write("INVENTORY4")
    fo.write(',')
    fo.write("Money 10")
    fo.write(',')
    fo.write("Knife_1")
    fo.close()
    import start.py

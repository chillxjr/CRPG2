import os
import sys
import time
from clint.textui import colored
from chillfunc import clear
from chillfunc import die


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
print ("*                    Chill's RPG Engine Character Sheet                        *")
print ('*                                                                              *')
print ('*                                Version 0.6                                   *')
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
charfile = input("Character's Name: ")
charfilefinal = "." + charfile + ".txt"

in_file = open(charfilefinal, "r") # open file lorem.txt for reading text data
contents = in_file.read() # read the entire file into a string variable 
in_file.close() # close the file 
 # print contents
#print(contents)
exp = contents[0:8]
level = exp[4]
expint = int(exp[4:8])

clear()
time.sleep(2)

def usescreen():
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
	print ("*               	          USE SCREEN			                  *")
	print ('*                                                                              *')
	print ('*                                Version 0.6                                   *')
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
	choice = input('Option: ')
	clear()
	charsheet()

def adventure():
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
	print ("*               	          Adventure Mode 		                  *")
	print ('*                                                                              *')
	print ('*                                Loading...                                    *')
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
	import adventure
	
def charsheet():
	#XP display
	clear()
	exp = contents[0:8]
	level = exp[4]
	expint = int(exp[4:8])
	print (' ')
	print (' ')
	print (' ')
	print (' ')
	print (' ')
	print (' ')
	print (' ')
	print (' ')
	print (colored.red("Character Name: ") + colored.blue(charfile))
	print (' ')
	print (colored.yellow(exp))
	print (colored.yellow('Level: ') + colored.yellow(level))



	stripn = len(charfile)
	stripf = 16 + stripn


	contents1 = contents.replace(contents[:stripf], '')


	print (' ')

	stripstat = 86
	contents2 = contents1.replace(contents1[:stripstat], '')




	inventype = contents2[0:10]
	invlook = stripf + 86 + 11
	actinv = contents.replace(contents[:invlook], '')
	inventory = actinv.split(",")

  
	statlist = contents1[0:86]
	statlist2 = statlist.split(',')

	hp = 5
	hpcalc = statlist2[2]
	hpcalc2 = hpcalc[11]
	hpcalc3 = int(hpcalc2)
	hpfinal = hpcalc3 * hp 


	if hpfinal > 24:
	    print ('HP:' + colored.green(str(hpfinal)))
    
	elif hpfinal > 14:
	    print ('HP: ' + colored.yellow(str(hpfinal)))
    
	elif hpfinal > 1:
	    print ('HP: ' + colored.red(str(hpfinal)))


	print (' ')
	print (colored.white(statlist2[0]))#strength
	print (colored.white(statlist2[1]))#perception
	print (colored.white(statlist2[2]))#endurance
	print (colored.white(statlist2[3]))#charisma
	print (colored.white(statlist2[4]))#inteligence
	print (colored.white(statlist2[5]))#agility
	print (colored.white(statlist2[6]))#luck




	print (' ')
	print (' ')

	if inventype == "INVENTORY4":
	    print("Inventory size: Survival (6 Slots)")
	    print (' ')
	    print(inventory)
    
    
   
    
	if inventype == "INVENTORY2":
	    print("Inventory size: Medium (15 Slots)")
	    print (' ')
	    print(inventory)
    
    
	if inventype == "INVENTORY1":
	    print("Inventory size: Light (10 Slots)")
	    print (' ')
	    print(inventory)
    
    
	if inventype == "INVENTORY3":
	    print("Inventory size: Heavy (20 Slots)")
	    print (' ')
	    print(inventory)
    
	
	menu()
    


def menu():    
	print('--------------------------------------------------------------------------------')
	print('Type "help" for a list of commands.')
	select = input(':')
	while select == "help":
	    	print('go')
	    	print('use')
	    	print('add')
	    	print('remove -soon')
	    	print('add-exp')
	    	print('help')
	    	print('exit')
	    	print('die')
	    	select = input(':')
    
	if select == "use":
	    usescreen()

	if select == "exit":
	    print("Exiting")
	    time.sleep(1)
	    return(0)
	    system.quit()
	
	if select == "go":
	    os.system('python3 adventure.py')
	
	if select == "add":
	    itemchoice = input('please name the item: ')
	    print(itemchoice)
	    print("workdamnit" + inventory)
	    time.sleep(1000)
	    charsheet()

	if select == "add-exp": #Adds XP points to XP of char. Dont go over 9999 or it'll break.
	    choice = input("How much to add: ")
	    newxp = expint + int(choice)
	    print ("Adding " + choice + " experience, and the new total will be: " + str(newxp))
	    #need to pull fresh string from file to modify and save back to it.
	    updatexp = contents.replace(contents[0:8], 'xp: ' + str(newxp))
	    #print (updatexp)
	    fo = open(charfilefinal, "w")
	    fo.write(updatexp)
	    time.sleep(2)
	    fo.close()
	    charsheet()
	    #os.execl(sys.executable, sys.executable, *sys.argv)
    
	if select == "die":
	    die(charfilefinal)
	else:
		charsheet()
charsheet()

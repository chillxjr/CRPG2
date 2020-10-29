import os
import sys
import time
from clint.textui import colored
from chillfunc import clear
from chillfunc import die

name = (sys.argv[1])

clear()

def amenu():
	print("")
	print("You head out of town and come to a burned bus blocking a crossroads.")
	print("The bridge heading north is blown out. You can only go east or west.")
	print("")
	print("")
	print("")
	print("")
	choice = input("You go... ")
	
	
	if choice == "east":
		clear()
		print("east and I walk for 1 mile.")
		time.sleep(3)
	
	if choice == "west":
		print("west, and you stepped on a landmine. It went off.")
		time.sleep(3)
		print(colored.red('You Have Died.'))
		time.sleep(3)
		die(name)
		sys.exit("Exiting") 
		

amenu()
#clear()
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
print ('*                 	     Adventure Mode     		                  *')
print ('*                                                                              *')
print ('*                            Version 0.7                                       *')
print ('*                                                                              *')
print ('*                                                                              *')
print ('*                                                                              *')
print ('*                                                                              *')
print ('********************************************************************************')
print (' ')
print (' ')
print (' ')
print (' ')
print (' ')
print (' ')
time.sleep(1)
#amenu()



#choice = input('Option: ')
#os.system('python3 rpg.py')

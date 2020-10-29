import os
import sys
import time
from clint.textui import colored
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
print ("*                              Chill's RPG Engine                              *")
print ('*                                                                              *')
print ('*                                  Version 0.6                                 *')
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
print ("*     1.) Create a Character                   2.) Start Sheet                 *")
print ('*                                                                              *')
print ('*                                                                              *')
print ('*     3.) Character Manager                                                    *')
print ('*                                                                              *')
print ('*                                                                              *')
print ("* Note: If you enter anything other than a list item, The application will die *")
print ('********************************************************************************')
print (' ')
print (' ')
print (' ')
print (' ')
print (' ')
option = input("Please enter a list number: ")

if option == "1":
    import chargen

    
if option == "2":
    import rpg

if option == "3":
    import charmanager
    

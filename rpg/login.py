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

clear()
print(charfile)
time.sleep(2)

import sheet



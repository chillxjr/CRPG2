import os
import sys
import time
from clint.textui import colored

def clear():
	if os.name == 'nt':
		_ = os.system('cls')
	
	else:
		_ = os.system('clear')
		

def die(charfilefinal):
	
	print('You have ' + colored.red("died") + '.')
	print('Your character sheet has been deleted.')
	os.remove(charfilefinal)
	os.system('python3 start.py')
    	
	

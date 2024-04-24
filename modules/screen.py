import os 
import sys

def cleanScreen(): 
    if sys.platform == 'windows':
        os.system('cls')
    elif sys.platform == 'linux':
        os.system('clear')

def pauseScreen():
    if sys.platform == 'windows':
        os.system('pause')
    elif sys.platform == 'linux':
        input('Press any key to continue...')

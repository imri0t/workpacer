'''aplication: work pacer

   this application will pace work in specified intervals
   
   5 minutes of work ---> 30 second break
   30 minutes of work ---> 5 minute break
   
   this will be run in the background while working on high
   workload tasks in order to promote healthier work patterns
'''
#source written by im.ri0t

#if changes to the time between working and break intervals
#are desired then changes to the sleep values should be made

from time import sleep
from datetime import datetime
from random import choice
import sys
import os
import platform

from termcolor import colored, cprint
try:
    import colorama
    colorama.init()
except ImportError:
    pass

motive_line = [
    'you got this', 'you can do this dude', 'stay focused', 'it\'ll be done with soon, my guy', 'just keep at it', 'pace yourself'
]

def rep():
    '''loop reset'''
    five_min()

def five_min_b():
    '''five minute break block'''
    cprint(datetime.now().time(), 'cyan')
    cprint('\n\n! BREAK TIME !', 'red')
    print('\n\ntake a 5 minute break dude')
    print('the cycle resets afetr this')
    sleep(240)
    print('1 minute left\n\n')
    sleep(60)
    rep()

def thirty_min():
    '''thirty minute work block'''
    cprint(datetime.now().time(), 'cyan')
    cprint('\n\n! 30 minute block begin !\n\n', 'green')
    cho = choice(motive_line)
    print(cho,'\n\n')
    sleep(1800)
    five_min_b()

def thirty_sec():
    '''thirty second break block'''
    cprint(datetime.now().time(), 'cyan')
    cprint('\n\n! BREAK TIME !', 'red')
    print('\n\ntake a 30 second break dude')
    sleep(20)
    print('10 seconds left\n\n')
    sleep(10)
    thirty_min()

def five_min():
    '''five minute work block'''
    cprint(datetime.now().time(), 'cyan')
    cprint('\n\n! 5 minute block begin !\n\n', 'green')
    cho = choice(motive_line)
    print(cho,'\n\n')
    sleep(300)
    thirty_sec()

def main():
    cprint(datetime.now(), 'cyan')
    print('workpacer application for productivity [backend dev]')
    cprint('# made by im.ri0t #', 'magenta')
    print('\n\nwork session will begin after hitting enter')
    input()
    five_min()

if __name__ == '__main__':
    main()

#!/bin/python3

from random import randint

player = input('choose rock(r), paper(p), scissors(s): ')
print(player, 'vs', end = ' ')

comp_choose = randint(0,3)

if comp_choose == 0:
    comp_choose = 'r'
elif comp_choose == 1:
    comp_choose = 'p'
else:
    comp_choose = 's'
    
print(comp_choose)

if comp_choose == 'r' and player == 'p':
    print('player win!')
elif comp_choose == 'p' and player == 's':
    print('player win!')
elif comp_choose == 's' and player == 'r':
    print('player win')
elif comp_choose == 'r' and player == 's':
    print('computer win!')
elif comp_choose == 'p' and player == 'r':
    print('computer win!')
elif comp_choose == 's' and player == 'p':
    print('computer win!')
    

    
    
    
    
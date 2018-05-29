"""
Programmability Black Belt Apprentice (Level1)
https://github.com/Devanampriya/DevNet_vCC_Team0/blob/master/Camp1_Day2_assign2
Participant: ALBREN ALCORIN

Assignment
Write a program (in Python 3) to guess a randomly generated number between 1 and 10.
For Example:

Guess the number: 4
Wrong, try again!

Guess the number: 8
Correct!

Hint: Figure out which library the “randint” function belongs to.
"""

#Code
from random import randint
number=(randint(1, 10))

while  True:
    numinput = input('Guess the number: ')
    if str(number) != numinput:
        print ('Wrong, try again!')
    else:
        print('Correct!')
        break

__author__ = 'leeh7'
import random

def diceRoller(die_size, rolls):

    results = 0
    dice_sum = 0

    for i in range(0,rolls):
        results = random.randint(1,die_size)
        print("Die %d rolled %d." % (i+1,results))
        dice_sum += results

    print("Total of %d dice rolls is: %d" % (rolls,dice_sum))

    return None

x = int(input("Enter the number of faces on the dice: "))
y = int(input("Enter the number of rolls: "))
diceRoller(x,y)
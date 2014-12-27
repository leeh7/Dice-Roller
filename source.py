__author__ = 'leeh7'
import random

def diceRoller(dieSize, rolls):

    results = 0
    diceSum = 0

    for i in range(0,rolls):
        results = random.randint(1,dieSize)
        print("Die %d rolled %d." % (i+1,results))
        diceSum += results

    print("Total of %d dice rolls is: %d" % (rolls,diceSum))

    return None

x = int(input("Enter the number of faces on the dice: "))
y = int(input("Enter the number of rolls: "))
diceRoller(x,y)
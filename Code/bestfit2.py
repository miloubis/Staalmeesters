
from helper import *
from load_orders import *
import numpy as np

# define order
orderlist = order1.orderlist

# create roll
rollC = np.zeros((order1.maxLengthRoll, ROLL_C))

def Skyline(roll):
    """ Find the lowest skyline. The row in which this skyline is located, the column at which the skyline starts
    and how many columns the skyline covers. """
    row = 0
    startingCol = 0
    columns = 0
    skyline = []
    for i in range(roll.shape[0]):
        row = i
        for j in range(roll.shape[1]):
            if columns == 0:
                startingCol = j
            if roll[i, j] == 0:
                columns += 1
            if columns != 0 & roll[i, j] != 0:
                skyline.append(row)
                skyline.append(startingCol)
                skyline.append(columns)
            break
        if ...:
            break
    return skyline

def pack(roll, skyline, bestFit, orderNum):
    """ Pack the best fitting sub-order in the roll """
    row = skyline[0]
    startingCol = skyline[1]
    for i in range(bestFit.shape[0]):
        for j in range(bestFit.shape[1]):
            roll[row + i, startingCol + j] = orderNum
    return roll



remainingOrders = orderlist
orderNum = 0

# place all orders
for i in range(len(orderlist)):
    orderNum += 1
    skyline = Skyline(rollC)
    possibleWidth = skyline[2]
    bestFit = search(possibleWidth, remainingOrders)
    rollC = pack(rollC, skyline, bestFit, orderNum)

    # Remove the just placed order from list of remaining orders.
    for j in range(len(remainingOrders)):
        if remainingOrders[j][0] == bestFit.shape[0] & remainingOrders[j][1] == bestFit.shape[1]:
            del remainingOrders[j]

print rollC



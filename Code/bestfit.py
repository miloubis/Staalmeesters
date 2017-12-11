from helper import *
from load_orders import *
import numpy as np


# define order, list of remaining orders and order number
orderlist = order1.orderlist
remainingOrders = orderlist
orderNum = 0

# create roll
maxLength = order1.maxLengthRoll
rollC = create_roll(maxLength, ROLL_C)

# place all orders, therefore looping until remainingOrders is an empty list
while remainingOrders:
    j = 0

    # get the skyline
    skyline = Skyline(rollC)
    possibleWidth = skyline[2]

    # search for the best fitting sub order
    bestFit = search(possibleWidth, remainingOrders)

    # fill the unusable space with a filler
    if not bestFit.size:
        rollC = fill(rollC, skyline)

    # place the best fitting order in the roll
    elif bestFit.size:
        orderNum += 1
        rollC = pack(rollC, skyline, bestFit, orderNum)

        # Remove the just placed order from list of remaining orders.
        for j in range(len(remainingOrders)):
            if remainingOrders[j][0] == bestFit.shape[0] and remainingOrders[j][1] == bestFit.shape[1]:
                del remainingOrders[j]
                break
            elif remainingOrders[j][0] == bestFit.shape[1] and remainingOrders[j][1] == bestFit.shape[0]:
                del remainingOrders[j]
                break

# calculate the cost
cost = cost(rollC)
visualisation(rollC)


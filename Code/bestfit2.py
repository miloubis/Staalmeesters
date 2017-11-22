from helper import *
from load_orders import *
import numpy as np

# define order, list of remaining orders and order number
orderlist = order1.orderlist
remainingOrders = orderlist
orderNum = 0

# create roll
rollC = np.zeros((order1.maxLengthRoll, ROLL_C))
np.set_printoptions(edgeitems=500, linewidth=10000)
# place all orders
for i in range(len(orderlist)):
    orderNum += 1
    skyline = Skyline(rollC)
    print skyline
    possibleWidth = skyline[2]
    bestFit = search(possibleWidth, remainingOrders)
    rollC = pack(rollC, skyline, bestFit, orderNum)

    # Remove the just placed order from list of remaining orders.
    for j in range(len(remainingOrders)):
        if remainingOrders[j][0] == bestFit.shape[0] & remainingOrders[j][1] == bestFit.shape[1]:
            del remainingOrders[j]

# print rollC



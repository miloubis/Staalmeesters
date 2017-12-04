from helper import *
from load_orders import *
import numpy as np
import matplotlib.pylab as plt

# define order, list of remaining orders and order number
orderlist = order1.orderlist
remainingOrders = orderlist
orderNum = 0

# create roll
rollC = np.zeros((order1.maxLengthRoll, ROLL_C))

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
<<<<<<< Updated upstream
# calculate the cost
cost = cost(rollC)
print(cost)
np.set_printoptions(threshold=np.inf, linewidth=3000)
# print(rollC)
# print(np.where(rollC == 6))

plt.imshow(rollC)
plt.show()
=======
np.set_printoptions(threshold=10000000, linewidth=4000)
print(rollC)
>>>>>>> Stashed changes

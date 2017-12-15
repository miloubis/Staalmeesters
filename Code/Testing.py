from helper import *
from load_orders import *


# for exercise A
# create roll C
maxLength = combinedOrders234.maxLengthRoll
rollC = create_roll(maxLength, ROLL_C)

# create roll B
rollB = create_roll(maxLength, ROLL_B)

for i in range(10):
    # empty roll
    rollC =
    # define order, list of remaining orders and order number
    orderlist = sorted_orders(combinedOrders234.orderlist)

    # first half of the orderlist
    remainingOrdersB = orderlist[0:31]

    # second half of the orderlist
    remainingOrdersC = orderlist[31:62]


    # place all orders in assigned roll
    rollB = bestfit(remainingOrdersB, rollB)
    rollC = bestfit(remainingOrdersC, rollC)

    # calculate the cost
    costB = cost(rollB)
    costC = cost(rollC)
    total = costB[1] + costC[1]
    print(costB)
    print(costC)
    print(total)

# visualize the rolls of steel
visualisation(rollB)
visualisation(rollC)
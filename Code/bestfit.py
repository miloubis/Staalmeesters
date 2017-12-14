from helper import *
from load_orders import *


# for exercise A

# define order, list of remaining orders and order number
orderlist = sorted_orders(order1.orderlist)
remainingOrders = orderlist

# create roll C
maxLength = order1.maxLengthRoll
rollC = create_roll(maxLength, ROLL_C)

# place all orders in roll
rollC = bestfit(remainingOrders, rollC)

# Calculate the cost
costC = cost(rollC)
print(costC)

# visualize roll with placed orders
visualisation(rollC)


# # for exercise B
# # define order, list of remaining orders and order number
# orderlist = sorted_orders(combinedOrders234.orderlist)
# remainingOrdersC = orderlist[0:31]
# remainingOrdersB = orderlist[31:62]
#
# # create roll C
# maxLength = combinedOrders234.maxLengthRoll
# rollC = create_roll(maxLength, ROLL_C)
#
# # create roll B
# rollB = create_roll(maxLength,ROLL_B)
#
# # place all orders in assigned roll
# rollB = bestfit(remainingOrdersB, rollB)
# rollC = bestfit(remainingOrdersC, rollC)
#
# # calculate the cost
# costB = cost(rollB)
# costC = cost(rollC)
# print(costB)
# print(costC)
#
# # visualize the rolls of steel
# visualisation(rollB)
# visualisation(rollC)


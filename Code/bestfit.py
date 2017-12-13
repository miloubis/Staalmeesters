from helper import *
from load_orders import *

# define order, list of remaining orders and order number
# orderlist = order1.orderlist
# orderlist = combinedOrders234.orderlist
orderlist = sorted_orders(combinedOrders234.orderlist)
remainingOrdersC = orderlist[0:31]
remainingOrdersB = orderlist[31:62]

# create roll C
maxLength = combinedOrders234.maxLengthRoll
rollC = create_roll(maxLength, ROLL_C)

# create roll B
rollB = create_roll(maxLength,ROLL_B)

# place all orders in assigned roll
rollB = bestfit(remainingOrdersB, rollB)
rollC = bestfit(remainingOrdersC, rollC)

# # place all orders: looping until remainingOrders is an empty list
# while remainingOrdersB:
#
#     # reset j for each iteration
#     j = 0
#
#     # get the skyline
#     skyline = skyline(rollB)
#     possibleWidth = skyline[2]
#
#     # search for the best fitting sub order
#     bestFit = search(possibleWidth, remainingOrdersB)
#
#     # fill the unusable space with a filler
#     if not bestFit.size:
#         rollB = fill(rollB, skyline)
#
#     # place the best fitting order in the roll
#     elif bestFit.size:
#         orderNum += 1
#         rollB = pack(rollB, skyline, bestFit, orderNum)
#
#         # Remove the just placed order from list of remaining orders.
#         for j in range(len(remainingOrdersB)):
#             if remainingOrdersB[j][0] == bestFit.shape[0] and remainingOrdersB[j][1] == bestFit.shape[1]:
#                 del remainingOrdersB[j]
#                 break
#             elif remainingOrdersB[j][0] == bestFit.shape[1] and remainingOrdersB[j][1] == bestFit.shape[0]:
#                 del remainingOrdersB[j]
#                 break


# calculate the cost
costB = cost(rollB)
costC = cost(rollC)
print(costB)
print(costC)

# visualize the rolls of steel
visualisation(rollB)
visualisation(rollC)


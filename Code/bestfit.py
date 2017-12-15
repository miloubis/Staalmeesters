from helper import *
from load_orders import *
import random


# # for exercise A
#
# # define orderlist
# remainingOrders = sorted_orders(order1.orderlist)
#
# # create roll C
# maxLength = order1.maxLengthRoll
# rollC = create_roll(maxLength, ROLL_C)
#
# # place all orders in roll
# rollC = bestfit(remainingOrders, rollC)
#
# # Calculate the cost
# costC = cost(rollC)
# print(costC)
#
# # visualize roll with placed orders
# visualisation(rollC)


# # for exercise B
# # define order, list of remaining orders and order number
# orderlist = sorted_orders(combinedOrders234.orderlist)

# # first half of the orderlist
# remainingOrdersB = orderlist[0:31]

# # second half of the orderlist
# remainingOrdersC = orderlist[31:62]
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
# total = costB[1] + costC[1]
# print(costB)
# print(costC)
# print(total)
#
# # visualize the rolls of steel
# visualisation(rollB)
# visualisation(rollC)

# for exercise C

# define order
orderlist = order5.orderlist
remainingOrdersA = []
remainingOrdersB = []
remainingOrdersC = []

# divide the sub orders for each type of steel
for i in range(len(orderlist)):
    if orderlist[i][2] == 'Type I':
        remainingOrdersC.append(orderlist[i])
    elif orderlist[i][2] == 'Type II':
        remainingOrdersB.append(orderlist[i])
    elif orderlist[i][2] == 'Type III':
        remainingOrdersA.append(orderlist[i])

print(remainingOrdersA)
# print(remainingOrdersB)
# print(remainingOrdersB)
# sort the order lists
# remainingOrdersA = sorted_orders(remainingOrdersA)
# remainingOrdersB = sorted_orders(remainingOrdersB)
# remainingOrdersC = sorted_orders(remainingOrdersC)

# create rolls of steel
maxLength = order5.maxLengthRoll
rollA = create_roll(maxLength, ROLL_A)
rollB = create_roll(maxLength, ROLL_B)
rollC = create_roll(maxLength, ROLL_C)

# place all orders in assigned roll
rollA = bestfit(remainingOrdersA, rollA)
rollB = bestfit(remainingOrdersB, rollB)
rollC = bestfit(remainingOrdersC, rollC)

# calculate the cost
costA = cost(rollA)
costB = cost(rollB)
costC = cost(rollC)
total = costA[1] + costB[1] + costC[1]
print(costA)
print(costB)
print(costC)
print(total)

# visualize the rolls of steel
visualisation(rollA)
visualisation(rollB)
visualisation(rollC)



from helper import *
from load_orders import *
import numpy as np
import random
import sys

sys.setrecursionlimit(10000)

# Define following variables for all exercises
orderNum = 0
rowPos = 0
rowPos2 = 0
columnPos = 0
columnPos2 = 0

# # EXERCISE A

# # Define orderlist and shuffle sub orders
# remainingOrders = order1.orderlist
# random.shuffle(remainingOrders)

# # Create roll C
# maxLength = order1.maxLengthRoll
# rollC = create_roll(maxLength, ROLL_C)

# # Run random function for 500 times
# rollC = simulate(remainingOrders, orderNum, rowPos, rowPos2, columnPos, columnPos2, rollC)

# # Calculate the cost
# costC = cost(rollC)
# print"For exercise A, using the random algorithm, the length of roll C used (in meters) is: ", costC[0]
# print"The cost for exercise A, using the random algorithm is: ", costC[1]

# # Visualise roll with placed orders
# visualisation(rollC)


# # EXERCISE B

# # Shuffle sub orders in orderlist
# orderlist = combinedOrders234.orderlist
# random.shuffle(orderlist)

# # First half of the orderlist
# remainingOrdersB = orderlist[0:31]

# # Second half of the orderlist
# remainingOrdersC = orderlist[31:62]

# # Create roll B
# maxLength = combinedOrders234.maxLengthRoll
# rollB = create_roll(maxLength, ROLL_B)

# # Create roll C
# maxLength = combinedOrders234.maxLengthRoll
# rollC = create_roll(maxLength, ROLL_C)

# # Run random function for 500 times using roll B
# rollB = simulate(remainingOrdersB, orderNum, rowPos, rowPos2, columnPos, columnPos2, rollB)

# # Run random function for 500 times using roll C
# rollC = simulate(remainingOrdersC, orderNum, rowPos, rowPos2, columnPos, columnPos2, rollC)

# # Calculate the cost
# costB = cost(rollB)
# costC = cost(rollC)
# total = costB[1] + costC[1]
# print"For exercise B, using the random algorithm, the length of roll B used (in meters) is: ", costB[0]
# print"\r\n"
# print"The length of roll C used (in meters) is: ", costC[0]
# print"\r\n"
# print"The total costs for exercise B, using the random algorithm, are equal to: ", total

# # Visualise rolls with placed orders
# visualisation(rollB)
# visualisation(rollC)


# EXERCISE C

# Define orderlist
orderList = order5.orderlist
remainingOrdersA = []
remainingOrdersB = []
remainingOrdersC = [] 

# Divide the sub orders for each type of steel
for i in range(len(orderList)):
    if orderList[i][2] == 'Type I':
         remainingOrdersC.append(orderList[i])
    elif orderList[i][2] == 'Type II':
         remainingOrdersB.append(orderList[i])
    elif orderList[i][2] == 'Type III':
         remainingOrdersA.append(orderList[i])

# Create rolls of steel
maxLength = order5.maxLengthRoll
rollA = create_roll(maxLength, ROLL_A)
rollB = create_roll(maxLength, ROLL_B)
rollC = create_roll(maxLength, ROLL_C)

# Place all orders in assigned roll
rollA = simulate(remainingOrdersA, orderNum, rowPos, rowPos2, columnPos, columnPos2, rollA)
rollB = simulate(remainingOrdersB, orderNum, rowPos, rowPos2, columnPos, columnPos2, rollB)
rollC = simulate(remainingOrdersC, orderNum, rowPos, rowPos2, columnPos, columnPos2, rollC)

# Calculate the cost
costA = cost(rollA)
costB = cost(rollB)
costC = cost(rollC)
total = costA[1] + costB[1] + costC[1]
print"For exercise C, using the random algorithm, the length of roll A used (in meters) is: ", costA[0]
print"\r\n"
print"the length of roll B used (in meters) is: ", costB[0],
print"and the length of roll C used (in meters) is: ", costC[0]
print"The total costs for exercise C, using the random algorithm, are equal to: ", total

# Visualise rolls with placed orders
visualisation(rollA)
visualisation(rollB)
visualisation(rollC)






















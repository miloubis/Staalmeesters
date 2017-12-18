from helper import *
from load_orders import *
import random


# # For exercise A
#
# # Define orderlist
# remainingOrders = sorted_orders(order1.orderlist)
#
# # Create roll C
# maxLength = order1.maxLengthRoll
# rollC = create_roll(maxLength, ROLL_C)
#
# # Place all orders in roll
# rollC = bestfit(remainingOrders, rollC)
#
# # Calculate the cost
# costC = cost(rollC)
# print(costC)
#
# # Visualize roll with placed orders
# visualisation(rollC)


# # For exercise B
# # Define order, list of remaining orders and order number
# orderlist = sorted_orders(combinedOrders234.orderlist)

# # First half of the orderlist
# remainingOrdersB = orderlist[0:31]

# # Second half of the orderlist
# remainingOrdersC = orderlist[31:62]
#
# # Create roll C
# maxLength = combinedOrders234.maxLengthRoll
# rollC = create_roll(maxLength, ROLL_C)
#
# # Create roll B
# rollB = create_roll(maxLength,ROLL_B)
#
# # Place all orders in assigned roll
# rollB = bestfit(remainingOrdersB, rollB)
# rollC = bestfit(remainingOrdersC, rollC)
#
# # Calculate the cost
# costB = cost(rollB)
# costC = cost(rollC)
# total = costB[1] + costC[1]
# print("For exercise B, using the random algorithm, the length of roll B used (in meters) is: ", costB[0])
# print("\r\n")
# print("The length of roll C used (in meters) is: ", costC[0])
# print("\r\n")
# print("The total costs for exercise B, using the random algorithm, are equal to: ", total)
#
# # Visualise rolls with placed orders
# visualisation(rollB)

# for exercise C

# Define order
orderlist = order5.orderlist
remainingOrdersA = []
remainingOrdersB = []
remainingOrdersC = []

# Divide the sub orders for each type of steel
for i in range(len(orderlist)):
    if orderlist[i][2] == 'Type I':
        remainingOrdersC.append(orderlist[i])
    elif orderlist[i][2] == 'Type II':
        remainingOrdersB.append(orderlist[i])
    elif orderlist[i][2] == 'Type III':
        remainingOrdersA.append(orderlist[i])

# Sort the order lists
# remainingOrdersA = sorted_orders(remainingOrdersA)
# remainingOrdersB = sorted_orders(remainingOrdersB)
# remainingOrdersC = sorted_orders(remainingOrdersC)

# Create rolls of steel
maxLength = order5.maxLengthRoll
rollA = create_roll(maxLength, ROLL_A)
rollB = create_roll(maxLength, ROLL_B)
rollC = create_roll(maxLength, ROLL_C)

# Place all orders in assigned roll
rollA = bestfit(remainingOrdersA, rollA)
rollB = bestfit(remainingOrdersB, rollB)
rollC = bestfit(remainingOrdersC, rollC)

# Calculate the cost
costA = cost(rollA)
costB = cost(rollB)
costC = cost(rollC)
total = costA[1] + costB[1] + costC[1]
print("For exercise C, using the random algorithm, the length of roll A used (in meters) is: ", costA[0])
print("\r\n")
print("the length of roll B used (in meters) is: ", costB[0],)
print("\r\n")
print("and the length of roll C used (in meters) is: ", costC[0])
print("\r\n")
print("The total costs for exercise C, using the random algorithm, are equal to: ", total)

print(costA)

# Visualise rolls with placed orders
visualisation(rollA)
visualisation(rollB)
visualisation(rollC)


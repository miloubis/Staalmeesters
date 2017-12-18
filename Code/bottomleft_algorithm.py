from helper import *
from load_orders import *

# # EXERCISE A
# # Initialize orderlist, remainingorders, maxlength and create grid of zeroes
# orderlist = sorted_orders(order1.orderlist)
# remainingOrders = orderlist
#
# # Subtract 3000 to make running time a bit faster
# maxLength = order1.maxLengthRoll - 3000
# rollC = create_roll(maxLength, ROLL_C)
#
# # Loop through remaining orders and delete suborder if suborder is packed
# rollC = pack_bottomleft(remainingOrders, rollC)
#
# costC = cost(rollC)
# print("For exercise A, using the random algorithm, the length of roll C used (in meters) is: ", costC[0])
# print("The cost for exercise A, using the random algorithm is: ", costC[1])
#
# # Visualise roll with placed orders
# visualisation(rollC)


# # EXERCISE B
# # Define order, list of remaining orders and order number
# orderlist = sorted_orders(combinedOrders234.orderlist)
#
# # First half of the orderlist
# remainingOrdersB = orderlist[0:31]
#
# # Second half of the orderlist
# remainingOrdersC = orderlist[31:62]
#
# # Create roll C subtract 5000 to make running time a bit faster
# maxLength = combinedOrders234.maxLengthRoll - 8000
# rollC = create_roll(maxLength, ROLL_C)
#
# # Create roll B
# rollB = create_roll(maxLength,ROLL_B)
#
# # Place all orders in assigned roll
# rollB = pack_bottomleft(remainingOrdersB, rollB)
# rollC = pack_bottomleft(remainingOrdersC, rollC)
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
# visualisation(rollC)


# EXERCISE C

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
remainingOrdersA = sorted_orders(remainingOrdersA)
remainingOrdersB = sorted_orders(remainingOrdersB)
remainingOrdersC = sorted_orders(remainingOrdersC)

# Create rolls of steel subtract 5000 of maxLengthRoll to make runtime a bit faster
maxLength = order5.maxLengthRoll - 5000
rollA = create_roll(maxLength, ROLL_A)
rollB = create_roll(maxLength, ROLL_B)
rollC = create_roll(maxLength, ROLL_C)

# Place all orders in assigned roll
rollA = pack_bottomleft(remainingOrdersA, rollA)
rollB = pack_bottomleft(remainingOrdersB, rollB)
rollC = pack_bottomleft(remainingOrdersC, rollC)

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

# Visualise rolls with placed orders
visualisation(rollA)
visualisation(rollB)
visualisation(rollC)
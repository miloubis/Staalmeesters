from helper import *
from load_orders import *


# Exercise A
# Pack steel roll(rolltype, ordernumber, exercise)
packedRoll1 = pack_bottom_left(ROLL_C, order1, 1)

# Calculate the cost
costC = cost(packedRoll1)
print("For exercise A, using the random algorithm, the length of roll C used (in meters) is: ", costC[0])
print("The cost for exercise A, using the random algorithm is: ", costC[1])

# Visualise roll with placed orders
visualisation(packedRoll1)

# # Exercise B
# # Pack steel roll(rolltype, ordernumber, exercise)
# packedRoll1 = pack_bottom_left(ROLL_C, combinedOrders234, 2)
# packedRoll2 = pack_bottom_left(ROLL_B, combinedOrders234, 3)

# # Calculate the cost
# costB = cost(packedRoll2)
# costC = cost(packedRoll1)
# total = costB[1] + costC[1]
# print("For exercise B, using the random algorithm, the length of roll B used (in meters) is: ", costB[0])
# print("\r\n")
# print("The length of roll C used (in meters) is: ", costC[0])
# print("\r\n")
# print("The total costs for exercise B, using the random algorithm, are equal to: ", total)
#
# # Visualise rolls with placed orders
# visualisation(packedRoll2)
# visualisation(packedRoll1)


# # Exercise C
# # Pack steel roll(rolltype, ordernumber, exercise)
# packedRoll1 = pack_bottom_left(ROLL_C, order5, 4)
# packedRoll2 = pack_bottom_left(ROLL_B, order5, 5)
# packedRoll3 = pack_bottom_left(ROLL_A, order5, 6)

# # Calculate the cost
# costA = cost(packedRoll3)
# costB = cost(packedRoll2)
# costC = cost(packedRoll1)
# total = costA[1] + costB[1] + costC[1]
# print("For exercise C, using the random algorithm, the length of roll A used (in meters) is: ", costA[0])
# print("\r\n")
# print("the length of roll B used (in meters) is: ", costB[0],)
# print("\r\n")
# print("and the length of roll C used (in meters) is: ", costC[0])
# print("\r\n")
# print("The total costs for exercise C, using the random algorithm, are equal to: ", total)
#
# # Visualise rolls with placed orders
# visualisation(packedRoll3)
# visualisation(packedRoll2)
# visualisation(packedRoll1)

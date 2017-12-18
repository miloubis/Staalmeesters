from helper import *
from load_orders import *
import random
import sys

sys.setrecursionlimit(10000)


# Place the randomly shuffled subOrders in the roll



# Define orderlist
orderlist = order1.orderlist
maxLength = order1.maxLengthRoll

# Initiate starting positions in the numpy array to loop through
orderNum = 0
rowPos = 0
rowPos2 = 0
columnPos = 0
columnPos2 = 0


# Create roll
roll = create_roll(maxLength, ROLL_C)


pack_random(orderlist, orderNum, rowPos, rowPos2, columnPos, columnPos2, roll)
visualisation(roll)



# roll = pack_random(orderlist, orderNum, row, row2, col, col2, roll)

# def pack2_random(subOrder, orderNum, row, col, roll):
#     """
#     If the suborder does not fit into the same row using pack_random, find a place for it in another row, recursively
#     :param subOrder: the order in remainingOrders that must be placed
#     :param orderNum: the number of the order being placed
#     :param row: int to keep track of the roll's row in which the function is placing
#     :param col: int to keep track of the roll's column in which the function is placing
#     :param roll: numpy array in which each order must be placed
#     """
#     for k in range(1000):
#         if roll[row][k] == 0:
#             count = k
#             if subOrder[1] <= roll.shape[1] - count:
#                 for o in range(subOrder[0]):
#                     for p in range(subOrder[1]):
#                         roll[row + o][count + p] = orderNum
#             else:
#                 row += 100
#                 pack2_random(subOrder, row, orderNum, col, roll)

# pack_random(orderlist, orderNum, row, col, roll)

# Simulate for 500 times and save the best outcome
#costs = []
#for i in range(500):
#    costs.append((i, pack_random(orderlist, orderNum, row, col, roll))
#x = np.array(costs)
#index = np.where(x==x.min))[0]
#minimalcosts = costs[index]
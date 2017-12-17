from helper import *
from load_orders import *
import numpy as np
import random
import sys



# Define orderlist
orderlist = [[2,2], [2,3], [4,5]]
# Create starting values for orderNum, row and col to keep track of
orderNum = 0
row = 0
row2 = 0
col = 0
col2 = 0


# Create roll
roll = np.zeros((1000, 10))


# Place the randomly shuffled subOrders in the roll
def pack_random(remainingOrders, orderNum, row, row2, col, col2, roll):
    """
    Shuffle the remaining orders randomly and place them in the roll
    :param remainingOrders: a list of lists of the remaining orders and their specifications
    :param roll: numpy array in which each order must be placed
    :param row: int to keep track of the roll's row in which the function is placing
    :param col: int to keep track of the roll's column in which the function is placing
    :param orderNum: the number of the order being placed
    :return: visualisation of roll with placed orders using visualisation
    """

    while remainingOrders:
        count = 0
        subOrder = remainingOrders[0]
        for j in range(roll.shape[1]):
            temp = j
            if roll[row][j] == 0 and count == 0:
                col = temp
                count = 1
                print "count = ", count
                break
            elif j == roll.shape[1] - 1 and count == 0:
                row += 1
                pack_random(remainingOrders, orderNum, row, row2, col, col2, roll)
        if count == 1:
            orderNum += 1
            print "orderNum= ", orderNum
            for k in range(roll.shape[1]):
                if col + k == roll.shape[1] - 1 or roll[row][col + k] != 0:
                    col2 = col + k - 1
                    break
                else:
                    col2 = col + subOrder[1] -1
            colSpace = col2 - col + 1
            print "colSpace = ", colSpace
            for l in range(subOrder[0]):
                    if roll[row + l - 1][col] != 0 or roll[row + l - 1][col2] != 0:
                        break
                    else:
                        row2 = row + subOrder[0] - 1
            rowSpace = row2 - row
            print "rowSpace= ", rowSpace
            if subOrder[0] <= rowSpace:
                if subOrder[1] <= colSpace:
                    for m in range(subOrder[0]):
                        for n in range(subOrder[1]):
                            roll[row + m][col + n] = orderNum
                    remainingOrders.remove(subOrder)
                    print "remainingOrders= ", remainingOrders
                    break
                else: 
                    row2 = 0
                    col2 = 0
                    col = 0
                    row += 1
                    pack_random(remainingOrders,orderNum,row,row2,col,col2,roll)

    print roll

    # return roll

pack_random(orderlist, orderNum, row, row2, col, col2, roll)
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
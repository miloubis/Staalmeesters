from helper import *
from load_orders import *
import numpy as np
import random

# Define orderlist
orderlist = [[200, 200], [200, 300], [100, 300], [400, 400], [200, 200]]

# Create starting values for orderNum, row and col to keep track of
orderNum = 1
row = 0
col = 0


# Create roll
roll = np.zeros((100000, 1000))

# Place the randomly shuffled subOrders in the roll
def pack_random(remainingOrders, orderNum, row, col, roll):
    """
    Shuffle the remaining orders randomly and place them in the roll
    :param remainingOrders: a list of lists of the remaining orders and their specifications
    :param roll: numpy array in which each order must be placed
    :param row: int to keep track of the roll's row in which the function is placing
    :param col: int to keep track of the roll's column in which the function is placing
    :param orderNum: the number of the order being placed
    :return: visualisation of roll with placed orders using visualisation
    """
    random.shuffle(remainingOrders)
    for j in range(len(remainingOrders)):
        subOrder = remainingOrders[j]
        orderNum += 1
        if subOrder[1] <= 1000 - col:
            for n in range(subOrder[0]):
                for m in range(subOrder[1]):
                    roll[row + n][col + m] = orderNum
            col += subOrder[1]
        else:
            col = 0
            row += 100
            pack2_random(remainingOrders[j], orderNum, row, col, roll)
            col += subOrder[1]
            
    visualisation(roll)


def pack2_random(subOrder, orderNum, row, col, roll):
    """
    If the suborder does not fit into the same row using pack_random, find a place for it in another row, recursively
    :param subOrder: the order in remainingOrders that must be placed
    :param orderNum: the number of the order being placed
    :param row: int to keep track of the roll's row in which the function is placing
    :param col: int to keep track of the roll's column in which the function is placing
    :param roll: numpy array in which each order must be placed
    """
    for k in range(1000):
        if roll[row][k] == 0:
            count = k
            if subOrder[1] <= 1000-count:
                for o in range(subOrder[0]):
                    for p in range(subOrder[1]):
                        roll[row + o][count + p] = orderNum
            else:
                row += 100
                pack2_random(subOrder, row, orderNum, col, roll)


# Simulate for 500 times and save the best outcome
#for i in range(500):
#    costs = [pack_random(orderlist, orderNum, row, col, roll), ]

    

















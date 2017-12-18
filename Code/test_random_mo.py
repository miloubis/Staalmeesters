from helper import *
from load_orders import *
import numpy as np
import random
import sys

sys.setrecursionlimit(10000)


# Place the randomly shuffled subOrders in the roll
def pack_random(remainingOrders, orderNum, rowPos, rowPos2, columnPos, columnPos2, roll):
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
    while remainingOrders:
        subOrder = remainingOrders[0]
        for column in range(roll.shape[1]):
            if roll[rowPos][column] == 0:
                columnPos = column
                break
            elif column == roll.shape[1] - 1:
                rowPos += 10
                pack_random(remainingOrders, orderNum, rowPos, rowPos2, columnPos, columnPos2, roll)

        for column2 in range(roll.shape[1]):
            if columnPos + column2 == roll.shape[1] - 1 or roll[rowPos][columnPos + column2] != 0:
                columnPos2 = columnPos + column2
                break
        columnSpace = columnPos2 - columnPos + 1

        if roll[rowPos + subOrder[0] - 1][columnPos] == 0  and roll[rowPos + subOrder[0] - 1][columnPos2] == 0:

            for row in range(subOrder[0]):
                if roll[rowPos + row + 1][columnPos] != 0 or roll[rowPos + row + 1][columnPos2] != 0:
                    rowPos2 = rowPos + row
                    break

                if row == subOrder[0] - 1:
                    rowPos2 = rowPos + subOrder[0] - 1

        else:
            rowPos += 10
            columnPos = 0
            columnPos2 = 0
            rowPos2 = 0
            pack_random(remainingOrders, orderNum, rowPos, rowPos2, columnPos, columnPos2, roll)

        rowSpace = rowPos2 - rowPos + 1

        if subOrder[0] <= rowSpace and subOrder[1] <= columnSpace:
            orderNum += 1
            for rows in range(subOrder[0]):
                for columns in range(subOrder[1]):
                    roll[rowPos + rows][columnPos + columns] = orderNum
            remainingOrders.remove(subOrder)
            rowPos = 0
            rowPos2 = 0
            columnPos = 0
            columnPos2 = 0
        else:
            rowPos += 10
            pack_random(remainingOrders, orderNum, rowPos, rowPos2, columnPos, columnPos2, roll)

    return(roll)


# Define orderlist and maximum length of roll
orderlist = order1.orderlist
maxLength = order1.maxLengthRoll
roll = create_roll(maxLength, ROLL_C)

# Create starting values for orderNum, row and col to keep track of
orderNum = 0
rowPos = 0
rowPos2 = 0
columnPos = 0
columnPos2 = 0


pack_random(orderlist, orderNum, rowPos, rowPos2, columnPos, columnPos2, roll)
visualisation(roll)

from helper import *
from load_orders import *
import numpy as np
import random

# Define order, list of remaining orders and order number
orderlist = order1.orderlist


# Create roll
rollC = np.zeros((order1.maxLengthRoll, ROLL_C))
random.shuffle(remainingOrders)

# Place sub orders from an order randomly for 500 times
def pack(remainingOrders, roll):
    orderNum = 0
    row = 0
    col = 0
    for i in range(len(remainingOrders)):
        subOrder = remainingOrders[i]
        orderNum += 1
        for j in range(col, ROLL_C):
            if roll[row][j] == 0:
                col = j

            else:
                pack2(remainingOrder[j], (row + 1), orderNum, 0, roll)


    visualisation(roll)


def pack2(subOrder, row, orderNum, col, roll):
    for k in range(col, ROLL_C):
        if roll[row][k] != 0:
            space = k - col
            if subOrder[1] <= space:
                for l in range(subOrder[0]):
                    for m in range(subOrder[1]):
                        roll[row+l][col+m] = orderNum
            else:
                pack2(remainingOrder[j], (row + 1), orderNum, roll)


pack(orderlist, rollC)



















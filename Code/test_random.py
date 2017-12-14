from helper import *
from load_orders import *
import numpy as np
import random

# Define order, list of remaining orders and order number
orderlist = [[200, 200], [200, 300], [100, 300], [700, 700], [400, 700], [800, 800], [200, 300], [400, 500]]


# Create roll
roll = np.zeros((1000, 1000))

# Place sub orders from an order randomly for 500 times


def pack(remainingOrders, roll):
    orderNum = 0
    row = 0
    col = 0
    count = 0
    for j in range(0, len(remainingOrders)):
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
            pack2(remainingOrders[j], row, orderNum, col)

    visualisation(roll)


def pack2(subOrder, row, orderNum, col):
    for k in range(subOrder[1]):
        if roll[row][k] == 0:
            count = k
            if subOrder[1] <= 1000-count:
                for o in range(subOrder[0]):
                    for p in range(subOrder[1]):
                        roll[row + o][count + p] = orderNum
            else:
                row += 100
                pack2(subOrder, row, orderNum, col)





pack(orderlist, roll)

















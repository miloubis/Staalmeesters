from helper import *
from load_orders import *
import numpy as np
import random

# Define order, list of remaining orders and order number
orderlist = [[100, 200], [200, 300], [100, 100]]


# Create roll
roll = np.zeros((15000, 1000))


# Place sub orders from an order randomly for 500 times
def random(remainingOrders, roll):
    orderNum = 0
    row = 0
    col = 0
    for i in range(len(remainingOrders)):
        orderNum += 1
        subOrder = remainingOrders[i]
        if subOrder[1] <= ROLL_C-col:
            pack(remainingOrders[i], orderNum, row, col, roll)
            col += subOrder[1]
        else:
            pack(remainingOrders[i], orderNum, row+1, col, roll)


    visualisation(roll)


def pack(subOrder, orderNum, row, col, roll):
    for l in range(subOrder[0]):
        for m in range(subOrder[1]):
            roll[row+l][col+m] = orderNum
def pack2(subOrder, row, orderNum, col, roll):
    for k in range(col, 1000):
        if roll[row][k] != 0:
            space = k - col
            if subOrder[1] <= space:
                for l in range(subOrder[0]):
                    for m in range(subOrder[1]):
                        roll[row+l][col+m] = orderNum
            else:
                pack2(remainingOrder[i], (row + 1), orderNum, roll)


pack(orderlist, roll)
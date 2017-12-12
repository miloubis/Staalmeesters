from helper import *
from load_orders import *
import numpy as np
import random

# Define order, list of remaining orders and order number
orderlist = order1.orderlist
remainingOrders = orderlist
orderNum = 1

# Create roll
rollC = np.zeros((order1.maxLengthRoll, ROLL_C))

# Place sub orders from an order randomly for 500 times
row = 0
col = 0
height = 0
random.shuffle(remainingOrders)
for j in range(len(remainingOrders)):
    subOrder = remainingOrders[j]
    for n in range(subOrder[0]):
    	for m in range(subOrder[1]):
    		if subOrder[0] <= 55 - col:
    			rollC[row + n][col + m] = orderNum
    			col += m
                orderNum += 1
    		elif subOrder[0] > 55 - col:
    			col = 0
                row += 1
                for k in range(55):
                    if rollC[row][k]==0:
                        for p in range(55):
                            if rollC[row][p] != 0:
                                rollC[row][55-]                                



  				row += height 
    			rollC[row + n][col + m] = orderNum
    height = subOrder[1]



visualization(rollC)
















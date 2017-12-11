from helper import *
from load_orders import *
import numpy as np
import random

# Define order, list of remaining orders and order number
orderlist = order1.orderlist
remainingOrders = orderlist
orderNum = 0

# Create roll
rollC = np.zeros((order1.maxLengthRoll, ROLL_C))

# Place sub orders from an order randomly for 500 times
	row = 0
  	col = 0
    random.shuffle(remainingOrders)
    for j in range(len(remainingOrders)):
    	subOrder = remainingOrders[j]
    	for n in range(subOrder[0]):
    		for m in range(subOrder[1]):
    			if subOrder[0] <= 55 - row:
    				rollC[row + n][col + m] = orderNum*100
    				col += m
    			elif subOrder[0] >= 55 - row:
    				col = 0
  					row += height 
    				rollC[row + n][col + m] = orderNum*100
    	height = subOrder[1]



    	(rollC)













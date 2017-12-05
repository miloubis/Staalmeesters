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
for i in range(500):
    random.shuffle(remainingOrders)

    # Place all suborders
    while remainingOrders:


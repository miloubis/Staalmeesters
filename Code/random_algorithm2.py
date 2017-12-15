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



pack(orderlist, rollC)



















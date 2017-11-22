from helper import *
from load_orders import *
import numpy as np

# define order, list of remaining orders and order number
orderlist = order1.orderlist
remainingOrders = orderlist
orderNum = 0

# create grid for steel roll
maxLengthRoll = int(order1.maxLengthRoll/10)
widthRoll = int(ROLL_C/10)
rollC = np.zeros((maxLengthRoll,widthRoll))

# search for empty space

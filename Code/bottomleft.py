from helper import *
from load_orders import *
import numpy as np

# load orderlist
orderlist = order1.orderlist

# create grid for steel roll
maxLengthRoll = int(order1.maxLengthRoll/10)
widthRoll = int(ROLL_C/10)
rollC = np.zeros((maxLengthRoll,widthRoll))

# divide orderlist by 10
dividedOrderlist = []
for i in range(len(orderlist)):
    order1 = int(orderlist[i][0] / 10)
    order2 = int(orderlist[i][1] / 10)
    dividedOrderlist.append([order1,order2])

print(dividedOrderlist)

# search for empty space
def bottom_left(roll):
    """ 
    Find the next bottom left corner to place a suborder. 

    """

    row = 0
    column = 0
    counter = 0
    bottomleft = []

    for i in range(widthRoll):
    	if roll[0][i]==0:
    		column += i+1
    		for j in range(widthRoll):
    			if roll[0][j] != 0 or roll[0][j] is out of range:
    				possibleWidth = j+1
    		for n in range(maxLengthRoll):
    			if 
    		







# print(rollC.shape[1])

# iterate through orderlist
# for i in range(len(orderlist)):
#     print(orderlist[i])

# length = rollC.shape[0]
# width = rollC.shape[1]


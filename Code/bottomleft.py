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
# print(rollC.shape[1])

# iterate through orderlist
# for i in range(len(orderlist)):
#     print(orderlist[i])

# length = rollC.shape[0]
# width = rollC.shape[1]


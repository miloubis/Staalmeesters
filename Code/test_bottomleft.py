from helper import *
from load_orders import *
from classes import *
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

# sort orderlist
sortedlist = sort_area(dividedOrderlist)

def pack_bottom_left(m,sortedlist,zeropos):
    """
    Pack sub-order in the roll
    """
    rowpos = zeropos[0]
    columnpos = zeropos[1]
    possibleWidth = zeropos[2]

    if possibleWidth >= sortedlist[1]:
        width = sortedlist[0]
        height = sortedlist[1]
        rollC[rowpos: height, columnpos: width] = m + 1


for i in range(len(orderlist)):
    startposition = Skyline(rollC)
    print(startposition)
    pack_bottom_left(i,sortedlist[i],Skyline(rollC))
    print(Skyline(rollC))

np.set_printoptions(threshold=100000, linewidth=350)
print(rollC.shape[1])


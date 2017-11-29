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

# search for empty space
def bottom_left(roll):
    """ 
    Find the next bottom left corner to place a suborder. 

    """

    row = 0
    column = 0
    possibleWidth = 0
    find = False
    columnpos = 0
    rowpos = 0

    for i in range(widthRoll):
        if roll[columnpos][i] == 0:
            break
        columnpos += 1
        rowpos = i+1
    for j in range(columnpos, widthRoll):
        if roll[rowpos][j] != 0 or j == widthRoll-columnpos:
            possibleWidth = j-columnpos
            break
    return possibleWidth, rowpos, columnpos

sortedlist = sortarea(dividedOrderlist)

def pack(sortedlist, possibleWidth, rowpos, columnpos):
    """
    Pack the best fitting sub-order in the roll
    """
    print(sortedlist)
    for i in range(len(sortedlist)):
        if possibleWidth >= sortedlist[i][1]:
            width = sortedlist[i][0]
            height = sortedlist[i][1]
            rollC[rowpos: height, columnpos: width] = i + 1
    # return [rowpos:width, columnpos:length]

bottom_left(rollC)
pack(sortedlist, possibleWidth, rowpos, columnpos)

np.set_printoptions(threshold=100000, linewidth=350)
# print(rollC)


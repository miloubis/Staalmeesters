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

rollC[0:2,0:5] = 1
print(rollC[0][4])

# search for empty space
def find_zero_indexes(roll):
    """
    Find the next bottom left corner to place a suborder.
    """
    print('ai')
    row = 0
    column = 0
    possibleWidth = 0
    columnpos = 0
    rowpos = 0
    indexes = []

    for i in range(rollC.shape[0]):
        for j in range(rollC.shape[1]):
            if roll[i][j] == 0:
                break
        break
    columnpos = j
    rowpos = i
    print(rowpos)
    print(columnpos)
    indexes.append([rowpos,columnpos])

    print(indexes)

find_zero_indexes(rollC)

    # for i in range(rollC.shape[1]):
    #     if roll[columnpos][i] == 0:
    #         break
    #     columnpos += 1
    #     rowpos = i+1
    # for j in range(columnpos, rollC.shape[1]):
    #     if roll[rowpos][j] != 0 or j == rollC.shape[1] - columnpos:
    #         possibleWidth = j - columnpos
    #         break
    # zeropos = []
    # zeropos.append(possibleWidth)
    # zeropos.append(rowpos)
    # zeropos.append(columnpos)
    # return zeropos

sortedlist = sort_area(dividedOrderlist)
# print(sortedlist)

def pack(sortedlist, zeropos):
    """
    Pack sub-order in the roll
    """
    possibleWidth = zeropos[0]
    rowpos = zeropos[1]
    columnpos = zeropos[2]
    width = sortedlist[i][0]
    height = sortedlist[i][1]
    rollC[rowpos: height, columnpos: width] = 1
    # for i in range(len(sortedlist)):
    #     if possibleWidth >= sortedlist[i][1]:
    #         width = sortedlist[i][0]
    #         height = sortedlist[i][1]
    #         rollC[rowpos: height, columnpos: width] = i + 1

    # return [rowpos:width, columnpos:length]

# bottom_left(rollC)
# pack(sortedlist, bottom_left(rollC))

np.set_printoptions(threshold=100000, linewidth=350)
print(rollC)
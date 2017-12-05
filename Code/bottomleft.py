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

sortedlist = sort_long(dividedOrderlist)

rollC[0:2,0:5] = 1


# search for empty space
def empty_space(roll):
    """
    Find the next bottom left corner to place a suborder.
    """

    indexes = []
    indexLength = 5

    for i in range(rollC.shape[0]):
        for j in range(rollC.shape[1]):
            if roll[i][j] == 0:
                break
        columnpos = j
        rowpos = i
        indexes.append([rowpos,columnpos])
        if columnpos == 0:
            break

    return indexes

def width(indexes):

    possibleWidths = []

    for i in range(rollC.shape[0]):
        if i == len(indexes):
            break
        counter = 0
        for j in range(rollC.shape[1]):
            if rollC[i][j] == 0 and j != 55:
                counter += 1
        possibleWidths.append(counter)

    return possibleWidths


# def pack_bottom_left(roll, ordernum, rowpos, heigth, columnpos, width):
#
#     roll[rowpos:heigth,columnpos,width] = ordernum


subOrder = []
for i in range(len(sortedlist)):
    for j in range(len(width(empty_space(rollC)))):
        if sortedlist[i][1] <= width(empty_space(rollC))[j]:
            break
        else:
            # continue in loop --> try next empty space
            print('ai')
    subOrder.append([i,sortedlist[i][0],sortedlist[i][1], (empty_space(rollC))[j][0], (empty_space(rollC))[j][1]])
    break
print(subOrder)

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


# def pack(sortedlist, zeropos):
#     """
#     Pack sub-order in the roll
#     """
    # possibleWidth = zeropos[0]
    # rowpos = zeropos[1]
    # columnpos = zeropos[2]
    # width = sortedlist[i][0]
    # height = sortedlist[i][1]
    # rollC[rowpos: height, columnpos: width] = 1
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
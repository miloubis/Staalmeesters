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
        for j in range(indexes[i][1],rollC.shape[1]):
            if rollC[i][j] != 0:
                break
            elif rollC[i][j] == 0 and j != 55:
                counter += 1
        possibleWidths.append(counter)

    return possibleWidths

rollC[0:34,0:18] = 1
rollC[0:33,18:32] = 2
rollC[0:32,32:42] = 3
rollC[32:32,32:] = 4

print(sortedlist)



# def pack_bottom_left(roll, ordernum, rowpos, heigth, columnpos, width):
#     roll[rowpos:heigth,columnpos,width] = ordernum


# remainingOrders = sortedlist
# subOrder = []
# for i in range(len(sortedlist)):
#     possibleWidth = width(empty_space(rollC))[0]
#     if remainingOrders[i][1] <= possibleWidth:
#         subOrder.append([i, remainingOrders[i][0], remainingOrders[i][1], (empty_space(rollC))[0][0], (empty_space(rollC))[0][1]])
#         rollC[subOrder[i][3]:subOrder[i][1], subOrder[i][4]:subOrder[i][2]] = subOrder[i][0] + 1
#     elif remainingOrders[i][1] >= possibleWidth:
#         # try next zero position
#         nextzero = empty_space(rollC)[1]
#         nextwidth = width(empty_space(rollC))[1]
#         if remainingOrders[i][1] >= nextwidth:
#             subOrder.append([i, remainingOrders[i][0], remainingOrders[i][1], (empty_space(rollC))[1][0], (empty_space(rollC))[1][1]])
#             rollC[subOrder[i][3]:subOrder[i][1], subOrder[i][4]:subOrder[i][2]] = subOrder[i][0] + 1

#
# print(subOrder)


np.set_printoptions(threshold=100000, linewidth=350)
print(rollC)
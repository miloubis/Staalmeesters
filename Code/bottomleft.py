from helper import *
from load_orders import *
import numpy as np

# load orderlist
orderlist = sorted_orders(order1.orderlist)
maxLength = order1.maxLengthRoll
rollC = np.zeros((maxLength, ROLL_C))


# search for empty space
def empty_space(roll):
    """
    Find the next bottom left corner to place a suborder.
    """
    i = 0
    j = 0
    indexes = []
    # for i in range(rollC.shape[0]):
    #     for j in range(rollC.shape[1]):
    #         if roll[i][j] == 0:
    #             break
    #     columnpos = j
    #     rowpos = i
    #     if columnpos == 0 or rowpos == 0:
    #         indexes.append([rowpos, columnpos])
    #     if columnpos == 0:
    #         break

    for i in range(rollC.shape[0]):
        for j in range(rollC.shape[1]):
            if rollC[i - 1][j] < 0:
                if roll[i][j] == 0:
                    columnpos = j
                    rowpos = i
                    indexes.append([rowpos, columnpos])
                    break
            else:
                if roll[i][j] == 0 and roll[i - 1][j] > 0:
                    columnpos = j
                    rowpos = i
                    indexes.append([rowpos, columnpos])
                    break
            if roll[i][j] == 0:
                break
    return indexes

def width(indexes):

    possibleWidths = []

    for i in range(rollC.shape[0]):
        if i == len(indexes):
            break
        counter = 0
        for j in range(indexes[i][1], rollC.shape[1]):
            if rollC[i][j] != 0:
                break
            elif rollC[i][j] == 0 and j != rollC.shape[0]:
                counter += 1
        possibleWidths.append(counter)
    return possibleWidths


# lengte = 10
# breedte = 10
# for i in range(lengte):
#     for j in range(breedte):
#         rollC[i][j] = 1

print(rollC.shape[0], rollC.shape[1])
rollC[0:10, 0:30] = 1
print(empty_space(rollC))
rollC[0:10,30:40] = 2
print(empty_space(rollC))
rollC[10:20,0:20] = 3
print(empty_space(rollC))


# for i in range(len(orderlist)):
#     position = empty_space(rollC)
#     possibleWidth = width(empty_space(rollC))
#
#     for j in range(len(position)):
#         if possibleWidth[j] >= orderlist[i-1][1]:
#             subOrder = []
#             subOrder.append([position[j][0],orderlist[i-1][0],position[j][1],orderlist[i-1][1]])
#             break
#     print(subOrder)
#     print("----")
#     print(i)
#     rollC[subOrder[0][0]:subOrder[0][1],subOrder[0][2]:subOrder[0][3]] = i





# print(empty_space(rollC))
# print(width(empty_space(rollC)))

#
# count = 0
# while count != 22:
#     position = empty_space(rollC)
#     print(position[0:4])
#     possibleWidth = width(empty_space(rollC))
#     print(possibleWidth[0:4])
#     count += 1

# for i in range(100):
#     position = empty_space(rollC)
#     print(position[0])
#     possibleWidth = width(empty_space(rollC))
#     print(possibleWidth[0])


visualisation(rollC)


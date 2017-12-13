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
    Find the next bottom left corner to place a suborder and find possible width.
    """
    i = 0
    j = 0
    indexes = [[0,0]]
    for i in range(rollC.shape[0]):
        for j in range(rollC.shape[1]):
            if roll[i][j] == 0:
                break
        columnpos = j
        rowpos = i
        indexes.append([rowpos,columnpos])
        if columnpos == 0:
            break

    newindexes = []
    for k in range(len(indexes)-1):
        a = indexes[k][1]
        b = indexes[k+1][1]
        c = indexes[k+1][0]
        if a != b:
            newindexes.append([c,b])

    possiblewidthlist = []
    for l in range(len(newindexes)):
        counter = 0
        rowpos = newindexes[l][0]
        colpos = newindexes[l][1]
        for m in range(newindexes[l][1], rollC.shape[1]):
            if rollC[rowpos][m] == 0:
                counter += 1
        possiblewidthlist.append(counter)

    emptyspaces = []
    for n in range(len(possiblewidthlist)):
        emptyspaces.append([newindexes[n][0],newindexes[n][1],possiblewidthlist[n]])

    if len(emptyspaces) == 0:
        emptyspaces.append([0,0,rollC.shape[1]])

    return emptyspaces

# lengte = 10
# breedte = 10
# for i in range(lengte):
#     for j in range(breedte):
#         rollC[i][j] = 1

print(orderlist)

#
rollC[0:10,0:30] = 1
# print(empty_space(rollC))
#
# rollC[0:10,30:40] = 2
# print(empty_space(rollC))
#
# rollC[10:20,0:20] = 3
# print(empty_space(rollC))
#


remainingOrders = orderlist

print(remainingOrders)
while remainingOrders:

    emptyspaces = empty_space(rollC)
    print(emptyspaces)
    for i in range(len(emptyspaces[0])):

        if emptyspaces[i][2] >= orderlist[0][1]:

            rollC[orderlist[0][0]:emptyspaces[i][0],orderlist[0][1]:emptyspaces[i][1]] = i
            break


    remainingOrders.pop(0)
    print(remainingOrders)

#
# for i in range(len(orderlist)):
#     emptyspaces = empty_space(rollC)
#     print(emptyspaces)
#     # print(len(emptyspaces))
#     for j in range(len(emptyspaces)):
#         print(emptyspaces[j])
#         for k in range(len(emptyspaces[j])):
#             # print(emptyspaces[j][k])
#             if emptyspaces[j][2] >= orderlist[i][1]:
#                 print("---------")
#                 print(emptyspaces[j][0])
#                 print(orderlist[i][0])
#                 print(emptyspaces[j][1])
#                 print(orderlist[i][1])
#                 print("---------")
#                 rollC[emptyspaces[j][0]:orderlist[i][0], emptyspaces[j][1]:orderlist[i][1]] == i
#                 break
            # if emptyspaces[j][2] >= orderlist[i][1]:
            #     rollC[emptyspaces[j][0]:orderlist[i][0],emptyspaces[j][1]:orderlist[i][1]] == i
            #     break
            # else:
            #     continue



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


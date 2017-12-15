from helper import *
from load_orders import *
import numpy as np

# load orderlist
from Code.helper import visualisation

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

    # delete zero positions in the same column
    newindexes = []
    for k in range(len(indexes)-1):
        a = indexes[k][1]
        b = indexes[k+1][1]
        c = indexes[k+1][0]
        d = indexes[k][0]
        if a != b:
            newindexes.append([c,b])

    print(newindexes)

    # check amount of zeroes next to zeroposition
    possiblewidthlist = []
    for l in range(len(newindexes)):
        counter = 0
        rowpos = newindexes[l][0]
        for m in range(newindexes[l][1], rollC.shape[1]):
            if rollC[rowpos][m] == 0:
                counter += 1
            if roll[rowpos][m] != 0:
                break
        possiblewidthlist.append(counter)

    # check amount of zeroes above zeroposition
    possibleheigthlist = []
    for l in range(len(newindexes)):
        counter = 0
        colpos = newindexes[l][1]
        # for m in range(0, 4850)
        for m in range(newindexes[l][0], rollC.shape[0]):
            if rollC[m][colpos] == 0:
                counter += 1
            if roll[m][colpos] != 0:
                break
        possibleheigthlist.append(counter)

    emptyspaces = []
    for n in range(len(possiblewidthlist)):
        emptyspaces.append([newindexes[n][0],newindexes[n][1],possiblewidthlist[n],possibleheigthlist[n]])

    if len(emptyspaces) == 0:
        emptyspaces.append([0,0,rollC.shape[1],rollC.shape[0]])

    return emptyspaces



print(orderlist)
print("------")
remainingOrders = orderlist[0:21]

counter = 1
while remainingOrders:

    print(remainingOrders)

    emptyspaces = empty_space(rollC)
    print(emptyspaces)

    rowpos = 0
    columnpos = 0
    for i in range(len(emptyspaces)):
        if emptyspaces[i][2] >= remainingOrders[0][1] and emptyspaces[i][3] >= remainingOrders[0][0]:
            break
    rowpos = emptyspaces[i][0]
    columnpos = emptyspaces[i][1]
    print("------")
    print(emptyspaces[i])
    print("......")
    print(rowpos), print(remainingOrders[0][0]), print(columnpos), print(remainingOrders[0][1])
    print("######")
    rollC[rowpos:remainingOrders[0][0]+rowpos,columnpos:remainingOrders[0][1]+columnpos] = counter + 1

    counter +=1
    remainingOrders.pop(0)


visualisation(rollC)


from helper import *
from load_orders import *

orderlist = sorted_orders(order1.orderlist)

maxLength = order1.maxLengthRoll
rollC = create_roll(maxLength, ROLL_C)

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
    if emptyspaces[i][4] > 0:
        rowpos = rowpos - emptyspaces[i][4] + 1
    rollC[rowpos:remainingOrders[0][0]+rowpos,columnpos:remainingOrders[0][1]+columnpos] = counter + 1

    print("------")
    print(emptyspaces[i])
    print("......")
    print(rowpos), print(remainingOrders[0][0]), print(columnpos), print(remainingOrders[0][1])
    print("######")

    counter +=1

    remainingOrders.pop(0)


visualisation(rollC)


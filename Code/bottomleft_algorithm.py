from helper import *
from load_orders import *

<<<<<<< HEAD:Code/bottomleft.py
# Exercise A Pack steel roll(rolltype, ordernumber, exercise)
packedRoll1 = pack_bottom_left(ROLL_C,order1,1)
cost = cost(packedRoll1)[1]

# # Exercise B Pack steel roll(rolltype, ordernumber, exercise)
# packedRoll1 = pack_bottom_left(ROLL_C,combinedOrders234,2)
# packedRoll2 = pack_bottom_left(ROLL_B,combinedOrders234,3)
# cost1 = cost(packedRoll1)
# cost2 = cost(packedRoll2)
# cost = cost(packedRoll1)[1] + cost(packedRoll2)[1]

# # Exercise B Pack steel roll(rolltype, ordernumber, exercise)
# packedRoll1 = pack_bottom_left(ROLL_C,order5,4)
# packedRoll2 = pack_bottom_left(ROLL_B,order5,5)
# packedRoll3 = pack_bottom_left(ROLL_A,order5,6)
# cost1 = cost(packedRoll1)
# cost2 = cost(packedRoll2)
# cost3 = cost(packedRoll3)
# cost = cost(packedRoll1)[1] + cost(packedRoll2)[1] + cost(packedRoll3)[1]

# Get score
print("The cost of this order is: € %.2f" % cost)

# Get visualisation
visualisation(packedRoll1)
# visualisation(packedRoll2)
# visualisation(packedRoll3)
=======
# Exercise A
# Initialize orderlist, remainingorders, maxlength and create grid of zeroes
orderlist = sorted_orders(order1.orderlist)
remainingOrders = orderlist
maxLength = order1.maxLengthRoll - 3000
rollC = create_roll(maxLength, ROLL_C)

# Loop through remaining orders and delete suborder if suborder is packed
counter = 1
while remainingOrders:

    # Check zero positions and empty spaces around the zero positions
    emptyspaces = empty_space(rollC)

    # Check if suborder fits in empty space found by emptyspaces function
    rowpos = 0
    columnpos = 0
    for i in range(len(emptyspaces)):
        if emptyspaces[i][2] >= remainingOrders[0][1] and emptyspaces[i][3] >= remainingOrders[0][0]:
            break

    # Save upper left corner from the suborder
    rowpos = emptyspaces[i][0]
    columnpos = emptyspaces[i][1]

    # Save upper right corner from the suborder
    columnpos_r = emptyspaces[i][1] + remainingOrders[0][1] - 1

    # Check empty space above upper right corner
    possiblewasteright = 0
    if emptyspaces[i][4] > 0:
        n = 0
        for m in range(rowpos, 0, -1):
            if rollC[m][columnpos_r] == 0:
                n += 1
            if rollC[m][columnpos_r] != 0:
                break
        possiblewasteright = n

    # Check empty space above upper left corner and upper right corner
    if emptyspaces[i][4] <= possiblewasteright:
        smallest = emptyspaces[i][4] - 1
    else:
        smallest = possiblewasteright - 1

    # Count empty rows above suborder
    freerows = 0
    for q in range(rowpos, rowpos - smallest, -1):
        for r in range(columnpos,columnpos_r):
            if rollC[q][r] != 0:
                break
        freerows += 1
    print("freerows")
    print(freerows)

    # If empty space is bigger than 1 move suborder up by amount of freerows
    if smallest > 1:
        rowpos = rowpos - freerows - 1

    # Pack suborder and delete suborder from the list
    rollC[rowpos:remainingOrders[0][0]+rowpos,columnpos:remainingOrders[0][1]+columnpos] = counter + 1
    remainingOrders.pop(0)

    # Go to next order in the list
    counter +=1

visualisation(rollC)
>>>>>>> origin/master:Code/bottomleft_algorithm.py

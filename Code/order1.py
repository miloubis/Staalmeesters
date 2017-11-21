import numpy as np
from load_orders import *
from helper import *

orders = [[19,27],[9,16],[12,29],[11,22],[16,12],[9,12],[20,10],[11,29], [12,17],[10,32],[9,16],[19,30],[17,25],
          [18,34],[17,18],[9,10],[11,27],[7,22],[4,13],[14,33],[13,11],[4,24]]

# WANNEER IK NEWARRAY GEBRUIK KRIJG IK FOUTMELDING
# orderArray = np.array(order1.orderlist, dtype='i')
# myInt = 10
# newArray = orderArray/myInt

# print grid of zeros and set printoptions
roll = np.zeros((480,55))
np.set_printoptions(threshold=100000, linewidth=350)

# set row and column position at 0
rowPosition = 0
columnPosition = 0

# loop through orderlist and place orders in grid
for i in range(1, len(orders) + 1):
    roll[rowPosition:rowPosition + orders[i - 1][0], columnPosition:orders[i - 1][1]] = i
    rowPosition += orders[i-1][0]

# calculate used meters
usedLengthRoll = ((rowPosition)/10)
cost = usedLengthRoll * CLASS_C

print('The total costs are €%.2f' % (cost))

print(roll)



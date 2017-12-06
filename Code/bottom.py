import numpy as np
from load_orders import *
from helper import *
from classes import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches

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

# fill in sort method
sortedlist = sort_short(dividedOrderlist)

# print grid of zeros and set printoptions
roll = np.zeros((480,55))
np.set_printoptions(threshold=100000, linewidth=350)

# set row and column position at 0
rowpos = 0
columnpos = 0

# create list for indexes visualisation
indexes = []

# loop through orderlist and place orders in grid
for i in range(1, len(sortedlist) + 1):
    roll[rowpos:rowpos + sortedlist[i - 1][0], columnpos:sortedlist[i - 1][1]] = i
    indexes.append([columnpos, rowpos, sortedlist[i - 1][1], sortedlist[i - 1][0]])
    rowpos += sortedlist[i - 1][0]

# set axes
fig = plt.figure()
ax= fig.add_subplot(111, aspect='equal')
ax.set_xlim(0, 55)
ax.set_ylim(0, 500)

# set title
fig.suptitle('Roll of steel', fontsize=14, fontweight='bold')

# set axis labels
ax.set_xlabel('Width (in decimeters)')
ax.set_ylabel('Length (in decimiters)')

for i in indexes:
    xas = i[0]
    yas = i[1]
    width = i[2]
    heigth = i[3]
    ax.add_patch(
        patches.Rectangle(
            (xas,yas),
            width,
            heigth,
            edgecolor="black"
        )
    )

plt.show()


# Practising
# ax.add_patch(
#     patches.Rectangle(
#         (0, 0),
#         27,
#         19,
#         edgecolor="black"
#     )
# )
#
# ax.add_patch(
#     patches.Rectangle(
#         (0, 19),
#         30,
#         19,
#         edgecolor="black"
#     )
# )
#
# ax.add_patch(
#     patches.Rectangle(
#         (0, 37),
#         34,
#         18,
#         edgecolor="black"
#     )
# )




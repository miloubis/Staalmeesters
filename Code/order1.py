import numpy as np
from load_orders import *
from helper import *

# orderlist = [
#   [9,16],
#   [12,29],
#   [11,22],
#   [16,12],
#   [9,12],
#   [20,10],
#   [11,29],
#   [12,17],
#   [10,32],
#   [9,16],
#   [19,30],
#   [17,25],
#   [18,34],
#   [17,18],
#   [9,10],
#   [11,27],
#   [7,22],
#   [4,13],
#   [14,33],
#   [13,11],
#   [4,24]
# ]

np.set_printoptions(threshold=100000, linewidth=300
                    )
roll = np.zeros((480,50))

roll[0:9, 0:16] = 1
roll[9:21, 0:29] = 2
roll[21:32, 0:22] = 3
roll[32:48, 0:12] = 4
roll[48:57, 0:12] = 5

print(roll)


import numpy as np

orders = [[2,3],[2,2],[2,1],[1,3],[1,4]]

roll = np.zeros((48,5))

roll[0:2, 0:3] = 1
roll[2:4, 0:2] = 2
roll[4:6, 0:1] = 3
roll[6:7, 0:3] = 4
roll[7:8, 0:4] = 5

# for x in np.nditer(roll, op_flags=['readwrite']):
#      if x == 0:
#          for i in orderlist:
#             roll[0:orderlist[0][0], 0:orderlist[0][1]] = 1

print(roll)
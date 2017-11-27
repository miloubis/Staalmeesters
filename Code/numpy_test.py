import numpy as np

orders = [[2,3],[2,2],[2,1],[1,3],[1,4]]

roll = np.zeros((48,5))

roll[0:2, 0:3] = 1
roll[2:4, 0:2] = 2
roll[4:6, 0:1] = 3
roll[6:7, 0:3] = 4
roll[7:8, 0:4] = 5

column_pos = 0
row_pos = 0

# roll[row_pos:row_pos + orders[0][0], column_pos:orders[0][1]] = 1
# row_pos += orders[0][0]
# roll[row_pos:row_pos + orders[1][0], column_pos:orders[1][1]] = 2
# row_pos += orders[1][0]
# roll[row_pos:row_pos + orders[2][0], column_pos:orders[2][1]] = 3
# row_pos += orders[2][0]
# roll[row_pos:row_pos + orders[3][0], column_pos:orders[3][1]] = 4
# row_pos += orders[3][0]
# roll[row_pos:row_pos + orders[4][0], column_pos:orders[4][1]] = 5
# row_pos += orders[4][0]

#
# for i in range(1,len(orders)):
#     roll[row_pos:row_pos + orders[i-1][0], column_pos:orders[i][1]] = i
#     print ("--------------------------{}--------------------------".format(column_pos))
#     row_pos += orders[i][0]
#     print ("--------------------------{}--------------------------".format(row_pos))
#     # print(i[0])
#
# for i in range(1,len(orders)+1):
#     roll[row_pos:row_pos + orders[i - 1][0], column_pos:orders[i - 1][1]] = i
#     row_pos += orders[i - 1][0]
# >>>>>>> eef2d4ff235902c25204e7473421c27ad6736710


# for x in np.nditer(roll, op_flags=['readwrite']):
#      if x == 0:
#          x[...] = 100

         # for i in orderlist:
         #    roll[0:orderlist[0][0], 0:orderlist[0][1]] = 1


print(roll)

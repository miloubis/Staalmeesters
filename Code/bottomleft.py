from helper import *
from load_orders import *

# # Exercise A Pack steel roll(rolltype, ordernumber, exercise)
# packedRoll = pack_bottom_left(ROLL_C,order1,1)
# cost = cost(packedRoll)[1]

# Exercise B Pack steel roll(rolltype, ordernumber, exercise)
packedRoll1 = pack_bottom_left(ROLL_C,combinedOrders234,2)
packedRoll2 = pack_bottom_left(ROLL_B,combinedOrders234,3)
cost = cost(packedRoll1)[1] + cost(packedRoll2)[1]

# # Exercise B Pack steel roll(rolltype, ordernumber, exercise)
# packedRoll1 = pack_bottom_left(ROLL_C,order5,4)
# packedRoll2 = pack_bottom_left(ROLL_B,order5,5)
# packedRoll3 = pack_bottom_left(ROLL_B,order5,6)
# cost = cost(packedRoll1)[1] + cost(packedRoll2)[1] + cost(packedRoll3)[1]



# Get score
print("The cost of this order is: € %.2f" % cost)

# Get visualisation
visualisation(packedRoll)





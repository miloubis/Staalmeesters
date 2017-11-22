import nunpy as np 
from helper import *
from load_orders import *

# create an empty array
order1 = order1.orderlist
maxLengthRoll = order1.maxLengthRoll / 10
rollC = np.zeros((maxLengthRoll,55))

# functie die de rij bepaalt waarin de breedte van de "skyline" moet worden gezocht
def determine_row():
	height = 0
	for i in range(1, 1000000):
		if rollC[i,1] != 0:
			height += 1
	row = height + 1
	return row

# functie die de breedte van de "skyline" bepaalt
def search_skyline(roll):
	skyline = 55
	for i in range(1,55):
		if rollC[1,i] != 0:
			skyline -= rollC[1,i]/rollC[1,i]
	return skyline

# functie die het "bestfit" blokje in de numpy array plaatst
def pack(bestFit, rollC):
	skyline_width=rollC.size
	rollC=np.append(rollC(), bestFit, axis=1)


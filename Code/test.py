rollC = [[18, 0, 0, 0, 4, 0, 2, 2, 0, 0, 0, 0, 0],
		 [0, 0, 0, 0, 4, 3, 2, 2, 1, 1, 1, 1, 1],
		 [5, 5, 5, 5, 4, 3, 2, 2, 1, 1, 1, 1, 1]]


def search_skyline(roll):
	counter = 0
	numrows = len(roll)
	numcols = len(roll[0])
	for n in range(numrows, 1):
		for i in range(1,14):
			if roll[n][i] == 0:
				for j in range(i, 14):
					if roll[n][j]!=0:
						counter+=j

	print counter
	print numrows
	print numcols
	print roll[0][0]


search_skyline(rollC)


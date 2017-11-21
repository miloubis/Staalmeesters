rollC = [[0, 0, 1, 1, 2, 2, 2, 3, 3, 3],
		 [4, 4, 4, 5, 5, 5, 6, 6, 6, 7]]


def search_skyline(roll):
	skyline = 10
	for i in range(1,10):
		if roll[1,i] != 0:
			skyline -= roll[1,i]/roll[1,i]
	print skyline


search_skyline(rollC)

#@L14D010[C:Code]|15> python test.py
#Traceback (most recent call last):
#  File "test.py", line 13, in <module>
#    search_skyline(rollC)
#  File "test.py", line 8, in search_skyline
#    if roll[1,i] != 0:
#TypeError: list indices must be integers, not tuple
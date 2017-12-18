"""
Helper.py
Staalmeester case
This file contains all the functions that are used in the three algorithms.
The functions are presented in alphabetical order.
In helper the constants for roll width and roll cost per meter are defined as well.
"""
import numpy as np
from classes import *
import matplotlib.pylab as plt
import random

# Define constants
ROLL_A = 500
ROLL_B = 520
ROLL_C = 550

COST_A = 14.80
COST_B = 14.24
COST_C = 13.92

def bestfit(remainingOrders, roll):
    """
    This function places all the sub orders into a roll of steel. It uses a while loop that loops until there aren't
    any sub orders remaining.
    :param remainingorders: A list of remaining sub orders
    :param roll: A numpy array that represents the steel roll in which the sub orders are placed
    :return: A numpy array in which all the sub orders are placed
    """
    orderNum = 0
    while remainingOrders:
        # Reset j for each iteration
        j = 0

        # Get the skyline
        skylineVars = skyline(roll)
        possibleWidth = skylineVars[2]

        # Search for the best fitting sub order
        bestFit = search(possibleWidth, remainingOrders)

        # Fill the unusable space with a filler
        if not bestFit.size:
            roll = fill(roll, skylineVars)

        # Place the best fitting order in the roll
        elif bestFit.size:
            orderNum += 1
            roll = pack_bestfit(roll, skylineVars, bestFit, orderNum)

            # Remove the just placed order from list of remaining orders.
            for j in range(len(remainingOrders)):
                if remainingOrders[j][0] == bestFit.shape[0] and remainingOrders[j][1] == bestFit.shape[1]:
                    del remainingOrders[j]
                    break
                elif remainingOrders[j][0] == bestFit.shape[1] and remainingOrders[j][1] == bestFit.shape[0]:
                    del remainingOrders[j]
                    break
    return roll

def cost(roll):
    """
    score function. This function calculates how many meters of the roll is used for all the orders that are placed
    within the roll. And how much this x amount of meters roll costs.
    :param roll: A numpy array that represents the steel roll in which the sub orders were placed.
    :return: In meters, the length of roll that is used. And the costs of using this x amount of roll.
    """
    results = []

    # Strip the roll of rows with only zeros
    roll = roll[~np.all(roll == 0, axis=1)]

    # Calculate the length of roll that is used
    meter = roll.shape[0] / 100

    # Calculate the cost of using roll A
    if roll.shape[1] == ROLL_A:
        costs = round( meter * COST_A, 2)
        results.append(meter)
        results.append(costs)
        return results

    # Calculate the cost of using roll B
    if roll.shape[1] == ROLL_B:
        costs = round(meter * COST_B,2)
        results.append(meter)
        results.append(costs)
        return results

    # Calculate the cost of using roll C
    if roll.shape[1] == ROLL_C:
        costs = round(meter * COST_C, 2)
        results.append(meter)
        results.append(costs)
        return results

def create_roll(maxLength, type):
    """
    This function creates a numpy array - representing a roll of steel -
    in which all sub orders from an order must be placed.
    :param maxLength: The maximum length of roll needed to fit all sub orders into the array.
    :param type: Type of steel roll.
    :return: A numpy array which represents the roll of steel in which all sub order must be placed.
    """
    roll = np.zeros((maxLength, type))
    return roll

def empty_space(roll):
    """
    This function searches for the next empty corner (zero). After it found an empty corner it checks how much
    space there is around the empty corner (possible width and possible height).
    :param roll: The roll in which the function has to search for an empty corner
    :return: An array with the index, the possible width, and the possible height of the empty corner.
    """

    # Search for zero positions
    i = 0
    j = 0
    indexes = [[0,0]]
    for i in range(roll.shape[0]):
        for j in range(roll.shape[1]):
            if roll[i][j] == 0:
                break
        columnpos = j
        rowpos = i
        indexes.append([rowpos,columnpos])

    # Check amount of zeroes next to zeroposition
    possiblewidthlist = []
    for l in range(len(indexes)):
        counter = 0
        rowpos = indexes[l][0]
        for m in range(indexes[l][1], roll.shape[1]):
            if roll[rowpos][m] == 0:
                counter += 1
            if roll[rowpos][m] != 0:
                break
        possiblewidthlist.append(counter)

    # Check amount of zeroes above zeroposition
    possibleheigthlist = []
    for l in range(len(indexes)):
        counter = 0
        colpos = indexes[l][1]
        for m in range(indexes[l][0], roll.shape[0]):
            if roll[m][colpos] == 0:
                counter += 1
            if roll[m][colpos] != 0:
                break
        possibleheigthlist.append(counter)

    # Check amount of zeroes under zeroposition
    possiblewastelist = []
    for l in range(len(indexes)):
        counter = 0
        colpos = indexes[l][1]
        for m in range(indexes[l][0], 0, -1):
            if roll[m][colpos] == 0:
                counter += 1
            if roll[m][colpos] != 0:
                break
        possiblewastelist.append(counter)

    emptyspaces = []
    for n in range(len(possiblewidthlist)):
        emptyspaces.append([indexes[n][0],indexes[n][1],possiblewidthlist[n],possibleheigthlist[n],
                            possiblewastelist[n]])

    if len(emptyspaces) == 0:
        emptyspaces.append([0,0,roll.shape[1],roll.shape[0],0])

    return emptyspaces

def fill(roll, skyline):
    """
    This function fills the space in which no sub order fits with a filler of 9999 (arbitrary).
    :param roll: A numpy array in which the orders are placed.
    :param skyline: A list that contains the coordinates at which the skyline starts and the width of the skyline.
    :return: A numpy array with filling in the skyline where no sub order fits.
    """

    row = skyline[0]
    startingCol = skyline[1]
    possibleWidth = skyline[2]
    filler = 9999

    # check whether skyline is between a sub order and the edge of the numpy array
    if startingCol + possibleWidth >= roll.shape[1]:
        for i in range(roll.shape[0]):

            # stop filling the rows when position before the filled space has a zero
            if roll[row + i][startingCol - 1] == 0:
                break

            # fill row with filler for the possible width
            for j in range(possibleWidth):
                roll[row + i][startingCol + j] = filler
        return roll

    # skyline is between sub orders
    else:
        for i in range(roll.shape[0]):

            # stop filling the rows if position right before or after filled space has a zero
            if roll[row + i][startingCol - 1] == 0 or roll[row + i][startingCol + possibleWidth] == 0:
                break

            # fill row with filler for the possible width
            for j in range(possibleWidth):
                roll[row + i][startingCol + j] = filler
        return roll

def pack_bestfit(roll, skyline, bestFit, orderNum):
    """
    This function packs the best fitting sub order into the roll of steel for the bestfit algorithm.
    :param roll: A numpy array - roll of steel - in which the sub order must be placed.
    :param skyline: A list that contains the coordinates at which the skyline starts and the width of the skyline.
    :param bestFit: A numpy array representing the best fitting order.
    :param orderNum: The number of the order being placed
    :return: A numpy array - roll of steel - in which the sub order is placed.
    """

    # Starting coordinates
    row = skyline[0]
    startingCol = skyline[1]

    # Place the sub order within the given skyline
    for i in range(bestFit.shape[0]):
        for j in range(bestFit.shape[1]):
            roll[row + i][startingCol + j] = orderNum
    return roll


def pack_random(remainingOrders, orderNum, rowPos, rowPos2, columnPos, columnPos2, roll):
    """
    This function packs the randomly shuffled sub orders in a numpy array which represents the roll of steel.
    :param remainingOrders: A list of lists of the remaining orders and their specifications.
    :param orderNum: An int to keep track of the sub order that is being placed.
    :param rowPos: An int to keep track of the first row position, to determine the rowSpace.
    :param columnPos: An int to keep track of the first column position, to determine the columnSpace.
    :param rowPos2: An int to keep track of the second row position, to determine the rowSpace.
    :param columnPos2: An int to keep track of the second column position, to determine the columnSpace.
    :param roll: A numpy array in which all the sub orders are placed.
    :return: Roll with every sub order placed.
    """

    # Loop while there are remaining sub orders and place the first sub order is the list
    while remainingOrders:
        subOrder = remainingOrders[0]

        # Reset all positions except rowPos
        columnPos = 0
        columnPos2 = 0
        rowPos2 = 0

        # Check where an empty space in the columns of the roll begins
        for column in range(roll.shape[1]):
            if roll[rowPos][column] == 0:
                columnPos = column
                break

            # If there is no empty space, up rowPos with 10 and call the function recursively
            elif column == roll.shape[1] - 1:
                rowPos += 10
                pack_random(remainingOrders, orderNum, rowPos, rowPos2, columnPos, columnPos2, roll)

        # Check where the empty space in the columns of the roll ends
        for column2 in range(roll.shape[1]):
            if columnPos + column2 == roll.shape[1] - 1 or roll[rowPos][columnPos + column2 + 1] != 0:
                columnPos2 = columnPos + column2
                break

        # Remember how much space is between the column positions
        columnSpace = columnPos2 - columnPos + 1

        # Check if height of the sub order will not overlap with another order above it.
        if roll[rowPos + subOrder[0] - 1][columnPos] == 0 and roll[rowPos + subOrder[0] - 1][columnPos2] == 0:

            # Check if there will not be a sub order overlapping in the middle
            for row in range(subOrder[0]):
                if roll[rowPos + row + 1][columnPos] != 0 or roll[rowPos + row + 1][columnPos2 -1] != 0:
                    rowPos2 = rowPos + row
                    break

                # If no overlap in the middle
                if row == subOrder[0] - 1:
                    rowPos2 = rowPos + subOrder[0] - 1

        # If there is overlap with an order above this sub order's height, up rowPos with 10 and call function again
        else:
            rowPos += 10
            pack_random(remainingOrders, orderNum, rowPos, rowPos2, columnPos, columnPos2, roll)

        # Remember how much space is between the row positions
        rowSpace = rowPos2 - rowPos + 1

        # Place sub order in roll if it fits in the row and column space
        if subOrder[0] <= rowSpace and subOrder[1] <= columnSpace:
            orderNum += 1
            for rows in range(subOrder[0]):
                for columns in range(subOrder[1]):
                    roll[rowPos + rows][columnPos + columns] = orderNum
            remainingOrders.remove(subOrder)

            # Reset rowPos to zero as well
            rowPos = 0

        # If sub order does not fit, up rowPos with 10, reset other positions back to zero and call function recursively
        else:
            rowPos += 10
            pack_random(remainingOrders, orderNum, rowPos, rowPos2, columnPos, columnPos2, roll)

    # Return the roll with all sub orders packed into it
    return roll

def rotation(subOrder):
    """
    This function rotates a sub order with 90 degrees.
    :param subOrder: The sub order that will be rotated.
    :return: The sub order that is now rotated.
    """

    # Rotate order
    rotateOrder = np.transpose(subOrder)
    return rotateOrder

def search(possibleWidth, remainingOrders):
    """
    This function searches for the best fitting sub order that fits into the the width of the lowest skyline.
    :param possibleWidth: The possible width of the lowest skyline; calculated with the skyline function.
    :param remainingOrders: A list of remaining sub orders that need to be placed in the roll of steel.
    :return: A numpy array representing the best fitting sub order.
    """
    # Initiate bestFit array
    bestFit = np.zeros((0, 0))

    # Iterate through the complete list of remaining orders searching for the best fitting sub order.
    for i in range(len(remainingOrders)):

        # Update the sub order that your trying to fit into the skyline
        subOrder = np.ones((remainingOrders[i][0], remainingOrders[i][1]))

        # Update bestFit if sub order fits (better) within the skyline
        if subOrder.shape[1] <= possibleWidth and subOrder.shape[1] > bestFit.shape[1]:
            bestFit = subOrder
            subOrder = rotation(subOrder)

            # Update bestFit if the rotated version of the sub order fits better
            if subOrder.shape[1] <= possibleWidth and subOrder.shape[1] > bestFit.shape[1]:
                bestFit = subOrder

        # If the sub order did not fit or did not fit better; rotate the sub order
        else:
            subOrder = rotation(subOrder)

            # Update bestFit if sub order fits (better) within the skyline
            if subOrder.shape[1] <= possibleWidth and subOrder.shape[1] > bestFit.shape[1]:
                bestFit = subOrder

        # If maximum width of the best fitting sub order is reached break loop and return bestFit
        if bestFit.shape[1] == possibleWidth:
            break
    return bestFit


def simulate(orderList, orderNum, rowPos, rowPos2, columnPos, columnPos2, roll):
    """
    This function carries out the pack_random function for 500 times.
    :return: The outcome with the lowest costs and its costs.
    """
    lowestCosts = 0
    for i in range(500):
        random.shuffle(orderList)
        roll = pack_random(orderList, orderNum, rowPos, rowPos2, columnPos, columnPos2, roll)
        costs = cost(roll)
        if i == 1:
            lowestCosts = costs[1]
            saveRoll = roll
        else: 
            if costs[1] < lowestCosts:
                lowestCosts = costs[1]
                saveRoll = roll
    return saveRoll

def skyline(roll):
    """
    This function searches for the lowest skyline. It remembers the starting coordinates of this skyline - row position
    and column position - and the width of the skyline; how many columns the skyline covers.
    :param roll: A numpy array representing the roll of steel in which the orders are placed.
    :return: The skyline results. A list with starting coordinates and the width of the lowest skyline.
    """

    # Initiate coordinates, possible width counter and the list in which the values must be saved.
    row = 0
    startingCol = 0
    counter = 0
    skylineValues = []

    # Find the lowest skyline in the roll of steel
    for i in range(roll.shape[0]):
        for j in range(roll.shape[1]):

            # Update coordinates only if no skyline has been found yet.
            if counter == 0:
                row = i
                startingCol = j

            # Save in skylineValues[0] the row coordinate, skylineValues[1] the column coordinate
            # and in skylineValues[2] the width of skyline
            if counter != 0 and (row != i or roll[i][j] != 0):
                skylineValues.append(row)
                skylineValues.append(startingCol)
                skylineValues.append(counter)

            # Break column loop if skyline is found
            if skylineValues:
                break

            # Update counter
            if roll[i][j] == 0:
                counter += 1

        # Break row loop if skyline is found
        if skylineValues:
            break

    return skylineValues

def sort_area(orderlist):
    """
    This function sort a list of orders from largest surface area to smallest.
    :param orderlist: The list of sub orders that need to be sorted
    :return: A list of sorted sub orders
    """

    # Initiate list for the areas per sub order and the list in which the orders will be placed; sorted on surface area
    areas = []
    orderedlist = []

    # Copy the order list as to not delete the original order list.
    indexableOrders = copy.copy(orderlist)

    # Calculate surface area for each sub order
    for i in range(len(indexableOrders)):
        areas.append(indexableOrders[i][0]*indexableOrders[i][1])

    # Sort the order list
    for i in range(len(indexableOrders)):

        # Find the index of the sub order in the remaining list of sub orders with the largest surface area
        index = areas.index(max(areas))
        orderedlist.append(indexableOrders[index])

        # Delete this sub order so it will nog be appended to the ordered list twice.
        del areas[index]
        del indexableOrders[index]

    return orderedlist

def sort_long(orderlist):
    """
    This function sorts a list of sub orders from largest long side to smallest.
    But, for example, to make sure [4,3] comes before [4,2] in the sorted list,
    the orderlist is first sorted on surface area.
    :param orderlist: List of (remaining) orders that need to be sorted
    :return: List of sorted orders
    """

    # Sort the list first on area
    orderlist = sort_area(orderlist)

    # Initiate ordered list of sub orders and create a copy the original order list as to not delete the order list
    orderedlist = []
    indexableOrders = copy.copy(orderlist)

    # Switch elements in the lists within the order list if second element has a larger value
    for i in range(len(indexableOrders)):
        if indexableOrders[i][0] < indexableOrders[i][1]:
            indexableOrders[i][0], indexableOrders[i][1] = indexableOrders[i][1], indexableOrders[i][0]

    # Make a list with only the largest element (= first element) of each sub list in indexableOrders
    firstelement = list(map(lambda x: x[0], indexableOrders))

    # Sort orders by finding the index of largest order, append this sub order to orderedList
    for i in range(len(indexableOrders)):
        index = firstelement.index(max(firstelement))
        orderedlist.append(indexableOrders[index])

        # Delete the ordered sub order as to not use it twice.
        del firstelement[index]
        del indexableOrders[index]

    return orderedlist

def sort_short(orderlist):
    """
    This function sorts a list of sub orders from largest short side to smallest.
    But, for example, to make sure [4,6] comes before [4,5] in the sorted list,
    the orderlist is first sorted on surface area.
    :param orderlist: List of (remaining) orders that need to be sorted
    :return: List of sorted orders
    """

    # Sort the list first on area
    orderlist = sort_area(orderlist)

    # Initiate ordered list of sub orders and create a copy the original order list as to not delete the order list
    orderedlist = []
    indexableOrders = copy.copy(orderlist)

    # Switch elements in the lists within the order list if second element has a smaller value
    for i in range(len(indexableOrders)):
        if indexableOrders[i][0] > indexableOrders[i][1]:
            indexableOrders[i][0], indexableOrders[i][1] = indexableOrders[i][1], indexableOrders[i][0]

    # Make a list with only the smallest element (= first element) of each sub list in indexableOrders
    firstelement = list(map(lambda x: x[0], indexableOrders))

    # Sort orders by finding the index of largest short side per sub order, append this sub order to orderedList
    for i in range(len(indexableOrders)):
        index = firstelement.index(max(firstelement))
        orderedlist.append(indexableOrders[index])

        # Delete the ordered sub order as to not use it twice.
        del firstelement[index]
        del indexableOrders[index]
    return orderedlist

def sorted_orders(orderlist):
    """
    This function sorts a list of orders in three ways: long or sort side or area.
    If you'd like to change the manner of sorting you only need to change this function.
    :param orderlist: A List of (remaining) orders that need to be sorted.
    :return: A List of sorted orders
    """
    # use either sort_long, sort_short or sort_area
    sortedOrders = sort_long(orderlist)
    return sortedOrders

def visualisation(roll):
    """
    This function visualizes how the sub orders are placed in the numpy array that represents a roll of steel.
    :param roll: A numpy array in which the all the sub orders are placed.
    """

    # Remove all rows with only zeros from numpy array
    roll = roll[~np.all(roll == 0, axis=1)]

    # Change empty space to NaN so it's visualized as white space
    for i in range(roll.shape[0]):
        for j in range(roll.shape[1]):
            if roll[i][j] == 9999 or roll[i][j] == 0:
                roll[i][j] = "NaN"

    # Create image and show image in computers cmd
    plt.imshow(roll, cmap='gist_ncar')
    plt.show()
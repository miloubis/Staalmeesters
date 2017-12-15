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
    if roll.shape[1] == 500:
        costs = meter * COST_A
        results.append(meter)
        results.append(costs)
        return results

    # Calculate the cost of using roll B
    if roll.shape[1] == 520:
        costs = meter * COST_B
        results.append(meter)
        results.append(costs)
        return results

    # Calculate the cost of using roll C
    if roll.shape[1] == 550:
        costs = meter * COST_C
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

def fill(roll, skyline):
    """
    This function fills the space in which no sub order fits with a filler of 9999 (arbitrary).
    :param roll: A numpy array in which the orders are placed.
    :param skyline: Contains the coordinates at which the skyline starts and the width of the skyline.
    :return: A numpy array with filling in the skyline where no sub order fits.
    """
<<<<<<< HEAD
    # use either sort_long, sort_short or sort_area
    sortedOrders = sort_area(orderlist)
    return sortedOrders
=======
>>>>>>> origin/master

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
    :param roll: numpy array in which is order must be placed
    :param skyline: a list of values indicating the starting row and column at which the order must be placed.
    :param bestFit: numpy array of the best fitting order
    :param orderNum: the number of the order being placed
    :return: roll with added order.
    """
    row = skyline[0]
    startingCol = skyline[1]
    # width = skyline[2]
    # if 0 < roll[row][startingCol - 1] < 9999:
    #     startingCol =
    #     for i in range(bestFit.shape[0]):
    #         for j in range(bestFit.shape[1]):
    #             roll[row + i][startingCol + j] = orderNum
    # else:
    for i in range(bestFit.shape[0]):
        for j in range(bestFit.shape[1]):
            roll[row + i][startingCol + j] = orderNum
    return roll

def rotation(subOrder):
    rotateOrder = np.transpose(subOrder)
    return rotateOrder

def search(possibleWidth, remainingOrders):
    """
    Searches for the best fitting sub order that fits into the the width of the lowest skyline.
    :param possibleWidth: the possible width of the lowest skyline that was calculated with the skyline function
    :param remainingOrders: a list of remaining sub orders that need to be placed.
    :return: numpy array of the best fitting sub order
    """
    # initiate bestFit array
    bestFit = np.zeros((0, 0))

    # Sort method can be changed to sort_long, sort_short or sort_area.
    sortedOrders = remainingOrders

    for i in range(len(sortedOrders)):
        subOrder = np.ones((sortedOrders[i][0], sortedOrders[i][1]))

        if subOrder.shape[1] <= possibleWidth and subOrder.shape[1] > bestFit.shape[1]:
            bestFit = subOrder
            subOrder = rotation(subOrder)
            if subOrder.shape[1] <= possibleWidth and subOrder.shape[1] > bestFit.shape[1]:
                bestFit = subOrder
        else:
            subOrder = rotation(subOrder)
            if subOrder.shape[1] <= possibleWidth and subOrder.shape[1] > bestFit.shape[1]:
                bestFit = subOrder

        # If maximum width of array is reached break loop and return bestFit
        if bestFit.shape[1] == possibleWidth:
            break
    return bestFit

def skyline(roll):
    """
    Find the lowest skyline. The row in which this skyline is located, the column at which the skyline starts
    and how many columns the skyline covers.
    :param roll: numpy array in which the orders are placed
    :return: the skyline. A list with row position and column position where the skyline starts and the width of said
    skyline.
    """
    row = 0
    startingCol = 0
    counter = 0
    skyline = []
    find = False

    for i in range(roll.shape[0]):
        for j in range(roll.shape[1]):
            if counter == 0:
                row = i
                startingCol = j

            # Skyline[0] the row in which the skyline lies, skyline[1] the column and skyline[2] the width of skyline
            if counter != 0 and (row != i or roll[i][j] != 0):
                skyline.append(row)
                skyline.append(startingCol)
                skyline.append(counter)
                find = True
            if find:
                break
            if roll[i][j] == 0:
                counter += 1
        if find:
            break
    return skyline

def sort_area(orderlist):
    """
    Sort a list of orders from largest surface area to smallest.
    :param orderlist: list of (remaining) orders that need to be sorted
    :return: list of sorted orders
    """
    areas = []
    orderedlist = []
    indexableOrders = copy.copy(orderlist)
    for i in range(len(indexableOrders)):
        areas.append(indexableOrders[i][0]*indexableOrders[i][1])
    for i in range(len(indexableOrders)):
        index = areas.index(max(areas))
        orderedlist.append(indexableOrders[index])
        del areas[index]
        del indexableOrders[index]
    return orderedlist

def sort_long(orderlist):
    """
    Sort a list of orders from largest long side to smallest. Example: To make sure [4,3] comes before [4,2] in the
    sorted list, the orderlist is first sorted on surface area.
    :param orderlist: list of (remaining) orders that need to be sorted
    :return: list of sorted orders
    """
    orderlist = sort_area(orderlist)
    orderedlist = []
    indexableOrders = copy.copy(orderlist)
    for i in range(len(indexableOrders)):
        if indexableOrders[i][0] < indexableOrders[i][1]:
            indexableOrders[i][0], indexableOrders[i][1] = indexableOrders[i][1], indexableOrders[i][0]
    firstelement = list(map(lambda x: x[0], indexableOrders))

    for i in range(len(indexableOrders)):
        index = firstelement.index(max(firstelement))
        orderedlist.append(indexableOrders[index])
        del firstelement[index]
        del indexableOrders[index]
    return orderedlist

def sort_short(orderlist):
    """
    Sort a list of orders from largest short side to smallest. Example: To make sure [4,7] comes before [4,6] in the
    sorted list, the orderlist is first sorted on surface area.
    :param orderlist: list of (remaining) orders that need to be sorted
    :return: list of sorted orders
    """
    orderlist = sort_area(orderlist)
    orderedlist = []
    indexableOrders = copy.copy(orderlist)
    for i in range(len(indexableOrders)):
        if indexableOrders[i][0] > indexableOrders[i][1]:
            indexableOrders[i][0], indexableOrders[i][1] = indexableOrders[i][1], indexableOrders[i][0]
    firstelement = list(map(lambda x: x[0], indexableOrders))

    for i in range(len(indexableOrders)):
        index = firstelement.index(max(firstelement))
        orderedlist.append(indexableOrders[index])
        del firstelement[index]
        del indexableOrders[index]
    return orderedlist

def sorted_orders(orderlist):
    """
    Sort a list of orders in three ways: long or sort side or area. If you'd like to change the manner of sorting you
    only need to change this function.
    :param orderlist: list of (remaining) orders that need to be sorted
    :return: list of sorted orders
    """
    # use either sort_long, sort_short or sort_area
    sortedOrders = sort_short(orderlist)
    return sortedOrders

def visualisation(roll):
    """
    Visualize how the sub orders are placed in the roll that is used.
    :param roll: numpy array in which the orders are placed
    """
    roll = roll[~np.all(roll == 0, axis=1)]
    for i in range(roll.shape[0]):
        for j in range(roll.shape[1]):
            if roll[i][j] == 9999 or roll[i][j] == 0:
                roll[i][j] = "NaN"
    plt.imshow(roll, cmap='gist_ncar')
    plt.show()
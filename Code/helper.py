"""
Helper.py
Staalmeester case

This file contains the class 'Order' which holds every useful attribute of an order. It further
includes every function necessary for a certain algorithm.

"""
import numpy as np
from classes import *
import math

# Define constants
ROLL_A = 500
ROLL_B = 520
ROLL_C = 550

COST_A = 14.80
COST_B = 14.24
COST_C = 13.92

def sort_short(orderlist):
    """

    :param orderlist:
    :return:
    """
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


def sort_long(orderlist):
    """

    :param orderlist:
    :return:
    """
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

def sort_area(orderlist):
    """

    :param orderlist:
    :return:
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

def rotation(subOrder):
    rotateOrder = np.transpose(subOrder)
    return rotateOrder

def search(possibleWidth, remainingOrders):
    """

    :param possibleWidth:
    :param remainingOrders:
    :return:
    """
    """ This is the search funtion for the best fitting sub order in an (remaining) order list. It searches in a
    sorted list of lists which is either sorted based on the long side, short side or acreage. It returns a best
    fitting sub order when 1) the order has the maximum possible with. For example possible width is 5 and the
    best fit numpy array has 5 columns. Or 2) when each possibility is tried and the resulting best fitting order
    has an as close as possible width (columns) to the possible width. For example, possible width is 5 and the
    remaining orders have a width of 1, 2 , 3, 4 than 4 is the clostest width to the possible width. """

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

def Skyline(roll):
    """

    :param roll:
    :return:
    """
    """
    Find the lowest skyline. The row in which this skyline is located, the column at which the skyline starts
    and how many columns the skyline covers.
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

def fill(roll, skyline):
    '''
    Where the roll has zero's in which no sub order fits. We will fill that space with 999
    :param roll: the roll in which the orders are placed
    :param skyline: contains the values at which the skyline starts and the width of that skyline where no order fits
    :return: a filled roll
    '''

    row = skyline[0]
    startingCol = skyline[1]
    possibleWidth = skyline[2]
    filler = 9999
    for i in range(roll.shape[0]):
        if roll[row + i][startingCol - 1] == 0:
            break
        for j in range(possibleWidth):
            roll[row + i][startingCol + j] = filler
    return roll

def pack(roll, skyline, bestFit, orderNum):
    """
    Pack the best fitting sub order into the roll
    :param roll: the roll in which is order must be placed
    :param skyline: a list of values indicating the starting row and column at which the order must be placed.
    :param bestFit: an numpy array of the best fitting order
    :param orderNum: the number of the order being placed
    :return:
    """
    row = skyline[0]
    startingCol = skyline[1]
    for i in range(bestFit.shape[0]):
        for j in range(bestFit.shape[1]):
            roll[row + i][startingCol + j] = (orderNum * 100)
    return roll

def cost(roll):
    """
    :param roll: the roll filled with orders
    :return: the length of roll used and the costs of using this roll
    """
    results = []

    # Strip the roll of rows with only zeros
    roll = roll[~np.all(roll == 0, axis=1)]

    # Calculate the length of roll that is used
    meter = roll.shape[0] / 100

    # Calculate the cost of using roll A
    if roll.shape[1] == 500 or roll.shape[1] == 50:
        costs = meter * COST_A
        results.append(meter)
        results.append(costs)
        return results

    # Calculate the cost of using roll B
    if roll.shape[1] == 520 or roll.shape[1] == 52:
        costs = meter * COST_B
        results.append(meter)
        results.append(costs)
        return results

    # Calculate the cost of using roll C
    if roll.shape[1] == 550 or roll.shape[1] == 55:
        costs = meter * COST_C
        results.append(meter)
        results.append(costs)
        return results

# MOGEN WE SORT CODE GEBRUIKEN???
# def mergesort(orderlist):
#     """based on https://github.com/TheAlgorithms/Python/blob/master/sorts/merge_sort.py
#     but tweaked to suit this project"""
#     length = len(orderlist)
#     if length > 1:
#         midpoint = length // 2
#         left_half = mergesort(orderlist[:midpoint])
#         right_half = mergesort(orderlist[midpoint:])
#         i = 0
#         j = 0
#         k = 0
#         left_length = len(left_half)
#         right_length = len(right_half)
#         while i < left_length and j < right_length:
#             if left_half[i] < right_half[j]:
#                 orderlist[k] = left_half[i]
#                 i += 1
#             else:
#                 orderlist[k] = right_half[j]
#                 j += 1
#             k += 1
#
#         while i < left_length:
#             orderlist[k] = left_half[i]
#             i += 1
#             k += 1
#
#         while j < right_length:
#             orderlist[k] = right_half[j]
#             j += 1
#             k += 1
#
#    return orderlist

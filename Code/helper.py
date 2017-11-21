"""
Helper.py
Staalmeester case

This file contains the class 'Order' which holds every useful attribute of an order. It further
includes every function necessary for a certain algorithm.

"""
import numpy as np

class Order:
    """" In this class all useful attributes for an order are saved """

    def __init__(self, orderlist):
        self.orderlist = orderlist
        self.totalArea = area(orderlist)
        self.maxLengthRoll = max_length(orderlist)

def area(orderlist):
    totalArea = 0
    if len(orderlist[0]) == 2 or isinstance(orderlist[0][2], str):
        for i in range(len(orderlist)):
            totalArea += orderlist[i][0] * orderlist[i][1]

    # 0.5 * basis * hoogte --> geen rechthoekige driehoeken wat betekenen de 3 cijfers?
    else:
        for i in range(len(orderlist)):
            totalArea += ((orderlist[i][0] * orderlist[i][1]) / 2)
    return totalArea

def max_length(orderlist):
    maxLength = 0
    for i in range(len(orderlist)):
        maxLength += max(orderlist[i][0], orderlist[i][1])
    return maxLength

def rotation(subOrder):
    rotateOrder = np.transpose(subOrder)
    return rotateOrder

def search(possibleWidth, remainingOrders):
    """ This is the search funtion for the best fitting sub order in an (remaining) order list. It searches in a
    sorted list of lists which is either sorted based on the long side, short side or acreage. It returns a best
    fitting sub order when 1) the order has the maximum possible with. For example possible width is 5 and the
    best fit numpy array has 5 columns. Or 2) when each possibility is tried and the resulting best fitting order
    has an as close as possible width (columns) to the possible width. For example, possible width is 5 and the
    remaining orders have a width of 1, 2 , 3, 4 than 4 is the clostest width to the possible width. """

    # initiate bestFit array
    bestFit = []

    # Sort method can be changed to sortlong, sortshort or sortarea.
    sortedOrders = sortlong(remainingOrders)

    for i in range(len(sortedOrders)):
        subOrder = np.ones((sortedOrders[i][0], sortedOrders[i][1]))
        print subOrder.shape
        if subOrder.shape[1] <= possibleWidth & subOrder.shape[1] > bestFit.shape[1]:
            bestFit = subOrder
            subOrder = rotation(subOrder)
            if subOrder.shape[1] <= possibleWidth & subOrder.shape[1] > bestFit.shape[1]:
                bestFit = subOrder
        else:
            subOrder = rotation(subOrder)
            if subOrder.shape[1] <= possibleWidth & subOrder.shape[1] > bestFit.shape[1]:
                bestFit = subOrder

        # If maximum width of array is reached break loop and return bestFit
        if bestFit.shape[1] == possibleWidth:
            break
            
    return bestFit

def sortshort(orderlist):
    """Sorts an orderlist according to smallest side from larger to smaller"""
    orderedlist = []
    for i in range(len(orderlist)):
        if orderlist[i][0] > orderlist[i][1]:
            orderlist[i][0], orderlist[i][1] = orderlist[i][1], orderlist[i][0]
    firstelement = map(lambda x: x[0], orderlist)
    for i in range(len(orderlist)):
        index = firstelement.index(max(firstelement))
        orderedlist.append(orderlist[index])
        del firstelement[index]
        del orderlist[index]
    return orderedlist

def sortlong(orderlist):
    """ Sorts an orderlistlist according to largest side from larger to smaller"""
    orderedlist = []
    for i in range(len(orderlist)):
        if orderlist[i][0] < orderlist[i][1]:
            orderlist[i][0], orderlist[i][1] = orderlist[i][1], orderlist[i][0]
    firstelement = map(lambda x: x[0], orderlist)
    for i in range(len(orderlist)):
        index = firstelement.index(max(firstelement))
        orderedlist.append(orderlist[index])
        del firstelement[index]
        del orderlist[index]
    return orderedlist

def sortarea(orderlist):
    """Sorts an orderlist according to area from larger to smaller"""
    areas = []
    orderedlist = []
    for i in range(len(orderlist)):
        areas.append(orderlist[i][0]*orderlist[i][1])
    for i in range(len(orderlist)):
        index = areas.index(max(areas))
        orderedlist.append(orderlist[index])
        del areas[index]
        del orderlist[index]
    return orderedlist

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

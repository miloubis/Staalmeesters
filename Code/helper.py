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
    widthArray = np.zeros(100, possibleWidth)
    bestFit = np.zeros((0, 0))
    sortedOrders = sortlong(remainingOrders)
    for i in range(len(sortedOrders)):
        subOrder = np.ones((sortedOrders[i][0], sortedOrders[i][1]))
        if subOrder.size(axis=1) <= widthArray.size(axis=1) & subOrder.size(axis=1) > bestFit.size(axis=1):
            bestFit = subOrder
            rotation(subOrder)
            if subOrder.size(axis=1) <= widthArray.size(axis=1) & subOrder.size(axis=1) > bestFit.size(axis=1):
                bestFit = subOrder
        else:
            rotation(subOrder)
            if subOrder.size(axis=1) <= widthArray.size(axis=1) & subOrder.size(axis=1) > bestFit.size(axis=1):
                bestFit = subOrder
    return bestFit

def sortshort(orderlist):
    """Sorts an orderlist according to smallest side from larger to smaller"""
    orderedlist = []
    for i in range(len(orderlist)):
        if orderlist[i][0] > orderlist[i][1]:
            orderlist[i][0], orderlist[i][1] = orderlist[i][1], orderlist[i][0]
    firstelement = map(lambda x: x[0], orderlist)
    print firstelement
    for i in range(len(orderlist)):
        index = firstelement.index(max(firstelement))
        print index
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
    print firstelement
    for i in range(len(orderlist)):
        index = firstelement.index(max(firstelement))
        print index
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

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
    for i in range(len(remainingOrders)):
        subOrder = np.ones((remainingOrders[i][0], remainingOrders[i][1]))
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
    for i in range(len(orderlist)):
        if orderlist[i][0] > orderlist[i][1]:
            orderlist[i][0], orderlist[i][1] = orderlist[i][1], orderlist[i][0]
    return orderlist

def sortlong(orderlist):
    for i in range(len(orderlist)):
        if orderlist[i][0] < orderlist[i][1]:
            orderlist[i][0], orderlist[i][1] = orderlist[i][1], orderlist[i][0]
    return orderlist

def sortarea(orderlist):
    areas = []
    orderedlist = []
    for i in range(len(orderlist)):
        areas = areas.extent(orderlist[i][0]*orderlist[i][1])
    for i in range(len(orderlist)):
        index = areas.index(max(areas))
        orderedlist = orderedlist.append(orderlist[index])
        del areas[index]
    return orderedlist
















"""
Helper.py
Staalmeester case

This file contains the class 'Order' which holds every useful attribute of an order. It further
includes every function necessary for a certain algorithm.

"""

class Order:
    """" In this class all useful attributes for an order are saved """

    def __init__(self, orderlist):
        self.orderlist = orderlist
        self.totalArea = Area(orderlist)
        self.maxLengthRoll = MaxLength(orderlist)

def Area(orderlist):
    area = 0
    for i in range(len(orderlist)):
        area += orderlist[i][0] * orderlist[i][1]
    return area

def MaxLength(orderlist):
    maxLength = 0
    for i in range(len(orderlist)):
        maxLength += max(orderlist[i][0], orderlist[i][1])
    return maxLength



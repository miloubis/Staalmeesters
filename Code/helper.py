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



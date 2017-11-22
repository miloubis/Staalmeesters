# Create order class with useful attributes
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
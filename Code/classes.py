import copy
# Create order class with useful attributes
class Order:
    """" In this class all useful attributes for an order are saved """

    def __init__(self, orderlist):
        self.orderlist = orderlist
        self.totalArea = self.area(orderlist)
        self.maxLengthRoll = self.max_length(orderlist)
        #self.area = area(orderlist)

    def area(self, orderlist):
        totalArea = 0
        if len(orderlist[0]) == 2 or isinstance(orderlist[0][2], str):
            for i in range(len(orderlist)):
                totalArea += orderlist[i][0] * orderlist[i][1]

        # 0.5 * basis * hoogte --> geen rechthoekige driehoeken wat betekenen de 3 cijfers?
        else:
            for i in range(len(orderlist)):
                totalArea += ((orderlist[i][0] * orderlist[i][1]) / 2)
        return totalArea

    def max_length(self, orderlist):
        maxLength = 0
        for i in range(len(orderlist)):
            maxLength += max(orderlist[i][0], orderlist[i][1])
        return maxLength

def sort_short(orderlist):
    """
    Sorts an order list according to smallest side from larger to smaller
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
    Sorts an orderlistlist according to largest side from larger to smaller
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
    Sorts an orderlist according to area from larger to smaller
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
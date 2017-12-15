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
        return totalArea

    def max_length(self, orderlist):
        maxLength = 0
        for i in range(len(orderlist)):
            maxLength += max(orderlist[i][0], orderlist[i][1])
        return maxLength

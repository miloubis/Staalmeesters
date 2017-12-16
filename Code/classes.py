import copy
# Create order class with useful attributes
class Order:
    """"
    In this class all useful attributes for an order are saved .
    """

    def __init__(self, orderlist):
        """
        This funtion initializes the order attributes.
        :param orderlist: List of sub orders.
        """
        self.orderlist = orderlist
        self.totalArea = self.area(orderlist)
        self.maxLengthRoll = self.max_length(orderlist)

    def area(self, orderlist):
        """
        This function calculates the total surface area of all sub orders in an order.
        :param orderlist: List of sub orders.
        :return: The total area of all sub orders combined.
        """
        totalArea = 0
        if len(orderlist[0]) == 2 or isinstance(orderlist[0][2], str):
            for i in range(len(orderlist)):
                totalArea += orderlist[i][0] * orderlist[i][1]
        return totalArea

    def max_length(self, orderlist):
        """
        This function calculates the maximum length of steel roll needed.
        This maximum length is based on placing all suborders on top of each other with longest side as rows.
        :param orderlist: List of sub orders.
        :return: The maximum length of steel roll need for an order.
        """
        maxLength = 0
        for i in range(len(orderlist)):
            maxLength += min(orderlist[i][0], orderlist[i][1])
        return maxLength

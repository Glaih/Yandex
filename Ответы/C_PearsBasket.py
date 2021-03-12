class PearsBasket:
    def __init__(self, quantity):
        self.quantity = quantity

    def __floordiv__(self, num):
        basket_list = []
        for i in range(num):
            basket_list.append(__class__(self.quantity // num))
        basket_list.append(__class__(self.quantity % num))
        return basket_list

    def __mod__(self, num):
        return self.quantity % num

    def __add__(self, other):
        return __class__(self.quantity + other.quantity)

    def __sub__(self, num):
        self.quantity -= num
        return self.quantity

    def __str__(self):
        return f"{self.quantity}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.quantity})"

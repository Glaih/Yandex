class AbstractCat:
    def __init__(self):
        self.weight = 0
        self.leftovers = 0

    def eat(self, food_given):
        food = food_given + self.leftovers
        self.leftovers = food % 10
        self.weight = self.weight + food // 10 if (self.weight + food // 10) <= 100 else 100

    def __str__(self):
        return f"{self.__class__.__name__} ({self.weight})"


class Kitten(AbstractCat):
    def __init__(self, weight):
        super(Kitten, self).__init__()
        self.weight = weight

    @staticmethod
    def meow():
        return "meow..."

    def sleep(self):
        return 'Snore' * (self.weight // 5)


class Cat(Kitten):
    def __init__(self, weight, name):
        super(Kitten, self).__init__()
        self.weight = weight
        self.name = name

    @staticmethod
    def meow():
        return "MEOW..."

    def get_name(self):
        return self.name

    @staticmethod
    def catch_mice():
        return 'Got it!'

class Upgrade:
    def __init__(self, name, cost, target_attr, value):
        self.__name = name
        self.__cost = cost
        self.__target_attr = target_attr
        self.__value = value

    @property
    def name(self):
        return self.__name

    @property
    def cost(self):
        return self.__cost

    @property
    def target_attr(self):
        return self.__target_attr

    @property
    def value(self):
        return self.__value

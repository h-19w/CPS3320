class cp:
    def __init__(self, manufact, model, price):
        self.manufact = manufact
        self.model = model
        self.price = price

    def get_model(self):
        return self.__model
    def set_model(self, model):
        self.__model = model
    def get_price(self):
        return self.__price
    def set_price(self, price):
        self.__price = price
    def get_manufact(self):
        return self.__manufact
    def set_manufact(self, manufact):
        self.__manufact = manufact

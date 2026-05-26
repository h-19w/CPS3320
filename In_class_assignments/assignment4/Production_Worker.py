# problem 1
class Employee:
    def __init__(self, name, id_number):
        self.__name = name
        self.__id_number = id_number

    def set_name(self, name):
        self.__name = name

    def set_id_number(self, id_number):
        self.__id_number = id_number

    def get_name(self):
        return self.__name
        
    def get_id_number(self):
        return self.__id_number
    
class Production_Worker(Employee):
    def __init__(self, name, number, shift, pay_rate):
        Employee.__init__(self, name, number) # Call the parent class constructor
        self.shift = shift
        self.pay_rate = pay_rate

    def get_shift(self):
        return self.shift

    def get_pay_rate(self):
        return self.pay_rate #hourly pay rate

    def set_shift(self, shift):
        self.shift = shift

    def set_pay_rate(self, pay_rate):
        self.pay_rate = pay_rate


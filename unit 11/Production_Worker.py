from Employee import Employee

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


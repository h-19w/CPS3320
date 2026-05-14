from Employee import Employee

class ShiftSupervisor(Employee):
    def __init__(self, name, number, annual_salary, annual_production_bonus):
        super().__init__(name, number)
        self.__annual_salary = annual_salary
        self.__annual_production_bonus = annual_production_bonus

    def get_annual_salary(self):
        return self.__annual_salary

    def get_annual_production_bonus(self):
        return self.__annual_production_bonus

    def set_annual_salary(self, salary):
        self.__annual_salary = salary

    def set_annual_production_bonus(self, bonus):
        self.__annual_production_bonus = bonus
class PersonalInfo:
    def __init__(self, name, address, age, phonenum):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phonenum = phonenum

    def set_name(self, name):
        self.__name = name
    def get_name(self):
        print('Name: ', self.__name)
        return self.__name
    def set_address(self, address):
        self.__address = address
    def get_address(self):
        print('Address: ', self.__address)
        return self.__address
    def set_age(self, age):
        self.__age = age
    def get_age(self):
        print('Age: ', self.__age)
        return self.__age
    def set_phonenum(self, phonenum):
        self.__phonenum = phonenum
    def get_phonenum(self):
        print('Phone Number: ', self.__phonenum)
        return self.__phonenum
    
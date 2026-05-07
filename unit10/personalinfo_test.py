import personal_info

def main():
    # name, address, age, phonenum
    # 3 people
    for i in range(3):
        name = input('Enter your name: ')
        address = input('Enter your address: ')
        age = input('Enter your age: ')
        phonenum = input('Enter your phone number: ')

        person = personal_info.PersonalInfo(name, address, age, phonenum)
        print("-----------------------------")
        print(f"Personal Information ({i+1}):")
        person.get_name()
        person.get_address()   
        person.get_age()
        person.get_phonenum()
        print("-----------------------------")
    

if __name__ == '__main__':
    main()
import Pet

def main():
    # pet data.
    name = input('Enter the name of your pet: ')
    animal_type = input('Enter the type of animal: ')
    age = int(input('Enter the age of your pet: '))

    pet = Pet.Pet(name, animal_type, age)

    print('Here is the data that you entered:')
    print(f'Name: {pet.get_name()}')
    print(f'Type: {pet.get_type()}')
    print(f'Age: {pet.get_age()}')

if __name__ == '__main__':
    main()
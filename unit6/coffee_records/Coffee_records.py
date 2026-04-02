


import search_coffee_records
import show_coffee_records
import add_coffee_records
import modifying_coffee_records
import delete_coffee_records


def menu():
    print('\n Welcome to Coffee Records\n')
    print('1. Search for a coffee record')
    print('2. Show all coffee records')
    print('3. Add a coffee record')
    print('4. Update a coffee record')
    print('5. Delete a coffee record')
    print('6. Exit \n')

def main():
    another = 'y'
    while another == 'y' or another == 'Y':
        menu()
        choice = input('Enter your choice: ')
        if choice == '1':
            search_coffee_records.main()
        elif choice == '2':
            show_coffee_records.main()
        elif choice == '3':
            add_coffee_records.main()
        elif choice == '4':
            modifying_coffee_records.main()
        elif choice == '5':
            delete_coffee_records.main()
        elif choice == '6':
            print('Goodbye!')
        else:
            print('Invalid choice. Please try again.')

        print('Do you want to perform another operation? (y/n): ')
        another = input('Y = yes, anything else = no: ')



if __name__ == '__main__':
    main()
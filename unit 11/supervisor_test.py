from ShiftSupervisor import ShiftSupervisor

def main():
    name= ''
    id = ''
    salary = 0
    bonus = 0.0
    
    # Get data attributes
    name = input('Enter the name: ')
    id = input('Enter the ID number: ')
    salary = float(input('Enter the annual salary: '))
    bonus = float(input('Enter the annual production bonus: '))


    supervisor = ShiftSupervisor(name, id, salary, bonus)

    print ('\nShift Supervisor information:')
    print (f'Name: {supervisor.get_name()}')
    print (f'ID number: {supervisor.get_id_number()}')
    print (f'Annual Salary: ${supervisor.get_annual_salary():,.2f}')
    print (f'Annual Production Bonus: ${supervisor.get_annual_production_bonus():,.2f}')


if __name__ == '__main__':
    main()
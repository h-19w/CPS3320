# Programming Exercise 11-1

import emp

def main():
    # Local variables
    worker_name= ''
    worker_id = ''
    worker_shift = 0
    worker_pay = 0.0
    
    # Get data attributes
    worker_name = input('Enter the name: ')
    worker_id = input('Enter the ID number: ')
    worker_shift = int(input('Enter the shift number: '))
    worker_pay = float(input('Enter the hourly pay rate: '))

    # Create an instance of ProductionWorker
    worker = emp.ProductionWorker(worker_name, worker_id,
                                  worker_shift, worker_pay)

    # Display information
    print ('Production worker information:')
    print (f'Name: {worker.get_name()}')
    print (f'ID number: {worker.get_id_number()}')
    print (f'Shift: {worker.get_shift_number()}')
    print (f'Hourly Pay Rate: ${worker.get_pay_rate():,.2f}')

# Call the main function.
if __name__ == '__main__':
    main()
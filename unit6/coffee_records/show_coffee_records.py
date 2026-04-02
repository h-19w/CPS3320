# This program reads coffee inventory records from
# coffee.txt and displays them.

def main():
    # Open the coffee.txt file.
    with open('coffee.txt', 'r') as coffee_file:
        # Read the first record's description field.
        descr = coffee_file.readline()

        # Read the rest of the file.
        while descr != '':
            # Read the quantity field.
            qty_line = coffee_file.readline()
            qty = float(qty_line.strip()) if qty_line else 0.0

            # Strip the '\n' from the description.
            descr = descr.rstrip('\n')

            # Display the record.
            print(f'Description: {descr}')
            print(f'Quantity: {qty}')

            # Read the next description.
            descr = coffee_file.readline()

# Call the main function.
if __name__ == '__main__':
    main()
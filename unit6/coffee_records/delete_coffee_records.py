import os # Needed for the remove and rename functions

def main():
    # Create a bool variable to use as a flag.
    found = False

    # Get the search value and the new quantity.
    search = input('Enter the description to delete: ')

    # Open the original coffee.txt file and a temporary file.
    with open('coffee.txt', 'r') as coffee_file, open('temp.txt', 'w') as temp_file:
        # Read the first record's description field.
        descr = coffee_file.readline()
        # Read the rest of the file.
        while descr != '':
            # Read the quantity field.
            qty = float(coffee_file.readline())
            # Strip the \n from the description.
            descr = descr.rstrip('\n')
            # Write either this record to the temporary file,
            # or the new record if this is the one that is
            # to be deleted.
            if descr == search:
                # Set the found flag to True.
                found = True
            else:
                # Write the original record to the temp file.
                temp_file.write(f'{descr}\n')
                temp_file.write(f'{qty}\n')
            # Read the next description.
            descr = coffee_file.readline()
    
    # Delete the original coffee.txt file.
    os.remove('coffee.txt')
    # Rename the temporary file.
    os.rename('temp.txt', 'coffee.txt')
    # If the search value was not found in the file
    # display a message.
    if found:
        print('The file has been updated.')
    else:
        print('That item was not found in the file.')

# Call the main function.
if __name__ == '__main__':
    main()
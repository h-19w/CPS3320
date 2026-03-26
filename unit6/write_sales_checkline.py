# This program reads all of the values in
# the sales.txt file.

def main():
    # Open the sales.txt file for reading.
    sales_file = open('sales.txt', 'r')

    # Read the first line from the file, but
    # don't convert to a number yet. We still
    # need to test for an empty string.
    line = sales_file.readline()
    sales_total = 0.0
    # As long as an empty string is not returned
    # from readline, continue processing.
    while line != '':
        # Convert line to a float.
        amount = float(line)
        sales_total += amount

        # Format and display the amount.
        print(f'{amount:.2f}')
        # prints the total after each line.
        # print ("total sales: ${:.2f}".format(sales_total))

        # Read the next line.
        line = sales_file.readline()
    print ("total sales: ${:.2f}".format(sales_total))
 
        
    # Close the file.
    sales_file.close()

# Call the main function.
if __name__ == '__main__':
    main()
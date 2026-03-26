# This program reads three lines of data
# to a file.
def main():
    # Open a file named philosophers.txt.
    infile = open('philosophers.txt', 'r')

    # Read the names of three philosophers
    # from the file.
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()


# the strip() method is used to remove the newline character from the end of the string that was read from the file. [next line is directly below this one]
    line1 = line1.strip() 
    line2 = line2.strip()
    line3 = line3.strip()


    # Close the file.
    infile.close()

    # Print the data that was read into
    # memory.
    print(line1)
    print(line2)
    print(line3)

# Call the main function.
if __name__ == '__main__':
    main()
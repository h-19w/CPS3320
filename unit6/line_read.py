# This program reads the contents of the
# philosophers.txt file one line at a time.
def main():
    # Open a file named philosophers.txt.
    infile = open('philosophers.txt', 'r')

    # Read three lines from the file
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    line4 = infile.readline()


    # Close the file.
    infile.close()

    # Print the data that was read into
    # memory.
    print(line1)
    print(line2, '\n') 
    # the newline character is included in the string that was read from the file, so an extra newline is added when it is printed. 
    print(line3)
    print(line4) 
    # an empty string is returned when the end of the file is reached

# Call the main function.
if __name__ == '__main__':
    main()
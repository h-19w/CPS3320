import random

def write():
    with open("random_num.txt", "w") as infile:
        total_numbers = int(input("how many random numbers do you want to write?: "))
        for i in range(total_numbers):
            num = random.randint(1, 500)
            infile.write(str(num) + "\n")
        print (f"{total_numbers} random numbers written to file.")

def read(): ## check file
    with open("random_num.txt", "r") as infile:
        numbers = infile.readlines()
        total_numbers = len(numbers)
        print(f"Total numbers in file: {total_numbers}")
        for num in numbers:
            print(num.strip())

def main():
    write()
    read()
# Call the main function.
if __name__ == '__main__':
    main()
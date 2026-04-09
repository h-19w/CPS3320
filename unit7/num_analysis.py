#lowest number in the list
# highest number in the list
# total of numbers in the list
# average of numbers in the list

def main():
    print("Enter 20 numbers:")
    numbers = [] #list
    for i in range(20):
        num = float(input(f"Number {i + 1}: "))
        numbers.append(num)
    lowest = min(numbers)
    highest = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)

    print(f"Lowest number: {lowest}")
    print(f"Highest number: {highest}")
    print(f"Total: {total}")
    print(f"Average: {average}")


if __name__ == '__main__':   
    main()
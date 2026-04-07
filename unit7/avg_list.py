def main():

    numbers = [5, 10, 20, 30]
    total = sum(numbers)
    average = total / len(numbers)
    print(f"The average is {average}.") 
    numbers.remove(min(numbers))
    total = sum(numbers)
    average = total / len(numbers)
    print(f'Average with lowest score dropped: {average}')

if __name__ == '__main__':
    main()
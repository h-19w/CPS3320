def calculate_average():
    total = 0
    count = 0
    with open('numbers.txt', 'r') as file:
        for line in file:
            number = int(line.strip())
            total += number
            count += 1
    return total / count

avg = calculate_average()
print(f"the average is: {avg}")
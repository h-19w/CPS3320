def create_file():
    with open('numbers.txt', 'w') as infile:
        infile.write("10\n")
        infile.write("20\n")
        infile.write("30\n")
    print('data written to numbers.txt.')

def calculate_average():
    total = 0
    count = 0
    with open('numbers.txt', 'r') as infile:
        for line in infile:
            number = int(line.strip())
            total += number
            count += 1
    return total / count

create_file()
avg = calculate_average()
print(f"the average is: {avg}")
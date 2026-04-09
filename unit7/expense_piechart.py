import matplotlib.pyplot as plt

def write_file():
    with open('expenses.txt', 'w') as outfile:
        outfile.write('Rent: 500\n')
        outfile.write('Gas: 300\n')
        outfile.write('Food: 1000\n')
        outfile.write('Clothing: 2000\n')
        outfile.write('Car Payment: 0\n')
        outfile.write('Miscellaneous: 100\n')
    print('data written to expenses.txt.')

def main():
    write_file()
    with open('expenses.txt', 'r') as infile:   
        categories = []
        amounts = []
        for line in infile:
            category, amount = line.split(':')
            categories.append(category.strip())
            amounts.append(float(amount.strip()))
    plt.pie(amounts, labels= categories)
    plt.title("Monthly Expenses")
    plt.show()

if __name__ == '__main__':
    main()
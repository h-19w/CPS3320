def num_file():
    with open('AvgNum.txt', 'w') as outfile:
        outfile.write("22\n")
        outfile.write("14\n")
        outfile.write("-99\n")
    print('data written to AvgNum.txt.')


def get_avg():
    total = 0
    count = 0
    try: 
        with open('AvgNum.txt', 'r') as infile: # 
            for line in infile:
                number = int(line)
                print(f"Read {number} from the file.")
                total += number
                count += 1
        average = total / count
        print(f"The average is {average}.")

    except FileNotFoundError:
        print("The file AvgNum.txt was not found.")
    except ValueError:
        print("The file contains non-numeric data.")

def main():
    num_file()
    get_avg()

# Call the main function.
if __name__ == '__main__':
    main()
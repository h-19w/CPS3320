def main():
    dict()

def dict():
    with open ("shorttext.txt", "r") as f:
        dictionary = {}
        for line in f:
            line = line.strip() 
            for symbol in ',.?!;:':
                line = line.replace(symbol, '')
            for word in line.split():
                if word in dictionary:
                    dictionary[word] += 1
                else:
                    dictionary[word] = 1
    print(dictionary)





if __name__ == "__main__":
    main()
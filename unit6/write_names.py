def main():
    print("enter the names of three friends. ")
    name1 = input("friend 1: ")
    name2 = input("friend 2: ") 
    name3 = input("friend 3: ")

    myfile = open("friends.txt", "w")

    myfile.write(name1 + "\n") 
    myfile.write(name2 + "\n")
    myfile.write(name3 + "\n")

    myfile.close()
    print("the names have been written to the file -> friends.txt")

if __name__ == "__main__":
    main()
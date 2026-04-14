def main():
    full_name = str(input("Enter a full name: "))
    name = full_name.split()
    initials = [i[0].upper() + "." for i in name]
    print("The initials are: ", end="")
    print(*initials, sep= "")


if __name__ == "__main__":
    main()
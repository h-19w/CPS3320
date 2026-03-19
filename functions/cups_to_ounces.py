def main():
    intro()
    cups_needed = int (input("enter the number of cups: "))
    cups_to_ounces(cups_needed)


def intro():
    print("welcome to the cups to ounces converter!")
    print("this program will convert cups into fluid ounces.")
    print("1 cup =  8 fluid ounces \n")
    
def cups_to_ounces(cups):
    ounces = cups * 8
    print(f"that is equal to {ounces} fluid ounces.")    

main()
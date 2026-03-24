def area(width, height):
    return width * height

def perimeter(width, height):
    return 2 * (width + height)

def main():
    print("welcome to the rectangle calculator!!")
    width = float(input("please enter the width of the rectangle: "))
    height = float(input("please enter the height of the rectangle: "))
    print(f"the area of the rectangle is: {area(width, height)}")
    print(f"the perimeter of the rectangle is: {perimeter(width, height)}")


if __name__ == "__main__":
    main()
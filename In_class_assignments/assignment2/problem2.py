matrixline1 = [int(x) for x in input("Enter three integers of the first line of the square(add spaces between them): ").split()]
matrixline2 = [int(x) for x in input("Enter three integers of the second line of the square(add spaces between them): ").split()]
matrixline3 = [int(x) for x in input("Enter three integers of the third line of the square(add spaces between them): ").split()]

magic = [matrixline1, matrixline2, matrixline3]

def matric_check():
    flat = matrixline1 + matrixline2 + matrixline3 
    if sorted(flat) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print("The numbers must be from 1 to 9 without repetition.")
        return False
    return True

def magic_check():
    magic = [matrixline1, matrixline2, matrixline3]
    if sum(matrixline1) != 15 or sum(matrixline2) != 15 or sum(matrixline3) != 15:
        return False
    if sum(magic[i][0] for i in range(3)) != 15:
        return False
    if sum(magic[i][1] for i in range(3)) != 15:
        return False
    if sum(magic[i][2] for i in range(3)) != 15:
        return False
    if sum(magic[i][i] for i in range(3)) != 15:
        return False
    if sum(magic[i][2 - i] for i in range(3)) != 15:
        return False
    return True
if matric_check() and magic_check():
    print("It is a magic square!")
else:
    print("Not a magic square.")

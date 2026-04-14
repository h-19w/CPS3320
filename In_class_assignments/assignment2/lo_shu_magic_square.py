def checker(magic_square):
    # Check if the sum of each row, column, and diagonal is 15
    for i in range(3): 
        if sum(magic_square[i]) != 15: # checks rows
            return False
        if sum(magic_square[j][i] for j in range(3)) != 15: # checks columns
            return False
    if sum(magic_square[i][i] for i in range(3)) != 15: # checks main diagonal
        return False
    if sum(magic_square[i][2 - i] for i in range(3)) != 15:
        return False
    return True

def main():
    ls_msquare = [
        [2, 7, 6],
        [9, 5, 1],
        [4, 3, 8]
    ]
    
    if checker(ls_msquare):
        print("The square is a Lo Shu Magic Square.")
    else:
        print("The square is not a Lo Shu Magic Square.")

if __name__ == "__main__":
    main()
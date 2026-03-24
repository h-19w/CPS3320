import random
random.seed(42)# allows each generation of the same sequenec of random numbers 
def main():
    print("welcome to the number guessing game!!")
    guessing_game()

def guessing_game():
    num = random.randint(1, 100)
    print("I have generated a random number between 1 and 100. \n take a guess what the number is: ")
    while True:
        guess = int(input("take a guess: "))
        if guess < num:
            print("too low, try again")
        elif guess > num:
            print("too high, try again")
        else:
            print("congratulations! you guessed the number correctly!!")
            print("generating new number...")

main()
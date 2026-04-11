import random 
## asks user for start no and end no 
# generates a random int in the range [including range numbers]
def generate_random_integer(start, end):
    return random.randint(start, end)

def main():
    try:
        start = int(input("Enter the start number: "))
        end = int(input("Enter the end number: "))
        
        if start > end:
            print("Start number should be less than or equal to end number.")
            return
        
        random_integer = generate_random_integer(start, end)
        print(f"Generated random integer between {start} and {end}: {random_integer}")
    except ValueError:
        print("Please enter valid integers.")
# Example usage:
if __name__ == "__main__":  
    main()
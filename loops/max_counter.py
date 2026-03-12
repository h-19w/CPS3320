# MAX = 5
# total = 0.0

# print ("this code calculates the sum of", end = " ")
# print(f'{MAX} numbers you will now enter: ')

# number = int(input("Enter a number: "))

# for counter in range(MAX):
#     number = int(input("Enter a number: "))
#     total = total + number 
   
# print(f'The sum of the numbers is: {total}')

###############
total = 0.0

print ("this code calculates the sum of numbers you will now enter: ")

number = int(input("\nEnter a number: "))

while (number != 0): 
    total = total + number 
    number = int(input("Enter a number: "))
   
print(f'The sum of the numbers is: {total}')
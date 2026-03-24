# generates 100 random numbers between 1 and 100, inclusive, using a fixed seed for reproducibility. 
#checks how many odd and even numbers are generated and prints the count at the end.

import random
random.seed(42)# allows each generation of the same sequenec of random numbers 
odd_count = 0
even_count = 0
for x in range(100):
    num = random.randint(1, 100)
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1  
    print(num)

print(f"Odd numbers: {odd_count}")
print(f"Even numbers: {even_count}")  



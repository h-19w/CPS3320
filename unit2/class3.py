
# CLASS 3 
print ("one", "two", "three") 
      # prints the three strings with a space in between by default
print ("one"+"two"+"three")
      # concatenates the three strings without any spaces in between
print ("one", "two", "three", sep="***") 
      # prints the three strings with '***' in between instead of a space
print ("one", "two", "three", end="!!!")
      # prints the three strings with a space in between and ends the line with '!!!'
   
name = "python"
print (f'{name} is a programming language')
        # uses an f-string to insert the value of the variable 'name' into the string
num = 12345.6789
print (f'{num:.2f}') # float with 2 decimal places
        # uses an f-string to insert the value of the variable 'num' into the string
print (f'{num:.2e}') # scientific notation with 2 decimal places
        # uses an f-string to format the variable 'num' in scientific notation with 2 decimal places
print (f'{int(num):d}') # integer
        # uses an f-string to format the variable 'num' as an integer with 2

discount = 0.25
print (f'{discount:.0%}')
        # output: 25%
        # uses an f-string to format the variable 'discount' as a percentage with no decimal places


num1 = 12341.23
num2 = 12345.6789
num3 = 123456789.123456789
num4 = 1789.123456789

print(f"num1: {num1:15.5f} $") # float with 2 decimal places
print(f"num2: {num2:^15.5f} $") # centered in a field of width 15
print(f"num3: {num3:>15.5f} $" ) # right-aligned in a field of width 15
print(f"num4: {num4:<15.5f} $") # left-aligned in a field of width 15



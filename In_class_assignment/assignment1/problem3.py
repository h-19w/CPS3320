total = 0
print("Enter a positive number \n(or a negative number to end):")
while True:
    num = int(input())
    if num < 0:
        break
    total += num
print("The sum of the positive numbers is:", total)
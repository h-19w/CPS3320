
input = int(input("please choose a number from 1-7: [exit = 0]\n"))
if input == 1:
    print("Monday")
elif input == 2:
    print("Tuesday")
elif input == 3:
    print("Wednesday")
elif input == 4:
    print("Thursday")
elif input == 5:
    print("Friday")
elif input == 6:
    print("Saturday")
elif input == 7:
    print("Sunday")
elif input == 0:
    print("exiting..")
    exit()
else:
    print("Invalid input, please choose a number from 1-7: ")

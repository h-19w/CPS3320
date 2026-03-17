#uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30 minutes.

x = 10 
while x<=30:
    calories_burned = x * 4.2
    print ("After " + str(x) + " minutes, you have burned " + str(calories_burned) + " calories.")
    if x == 30:
        break
    x = x+5
#distance x speed x time 
#distance traveled 

speed_input = int(input ("what is the speed of the vehicle in MPH? "))
hour_input = int(input ("how many hours has it traveled? "))
print("Hour\tDistance Traveled")
print("-----------------------------")

hour = 1

while (hour <= hour_input):
    distance_traveled = speed_input * hour 
    print(hour,"\t", distance_traveled)
    hour = hour+1


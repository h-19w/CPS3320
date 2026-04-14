common = []
powerball = []
with open("pbnumbers.txt", "r") as f:

    for line in f:
        numbers = line.strip().split()
        common.extend(int(x) for x in numbers[:5])   
        powerball.append(int(numbers[5]))  

count = {}
for num in common:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

pb_count = {}
for num in powerball:
    if num in pb_count:
        pb_count[num] += 1
    else:
        pb_count[num] = 1

pairs = []
for i in range(1, 70):
    freq = common.count(i)
    pairs.append([freq, i])


pairs.sort(reverse=True)
print("The 10 most common numbers, ordered by frequency:")
for i in range(10):
    print(f"{pairs[i][1]}: {pairs[i][0]} times")

pairs.sort() 
print("The 10 least common numbers, ordered by frequency:")
for i in range(10):
    print(f"{pairs[i][1]}: {pairs[i][0]} times")

last_seen = {}
lines = []
with open("pbnumbers.txt", "r") as f:
    for line in f:
        numbers = line.strip().split()
        lines.append(numbers)

for i, numbers in enumerate(lines):
        for num in numbers[:5]:
            last_seen[int(num)] = i  

overdue = []
for i in range(1, 70):
    if i in last_seen:
        overdue.append([last_seen[i], i])
    else:
        overdue.append([-1, i])  

overdue.sort() 
print("10 most overdue numbers:")  
for i in range(10):
    print(overdue[i][1])

print("Frequency of each number 1-69:")
for i in range(1, 70):
    freq = common.count(i)
    print(i, ":", freq)

print("Frequency of each Powerball number 1-26:")
for i in range(1, 27):
    freq = powerball.count(i)
    print(i, ":", freq)
    
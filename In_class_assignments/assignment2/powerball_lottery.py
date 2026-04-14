
def powerball_frequency():
    regular_counts = {}
    pb_counts = {}
    
    with open("pbnumbers.txt") as file:
        for line in file:
            tokens = line.split()
            if len(tokens) < 6:
                continue  # skip malformed lines
            
            # first 5 are regular numbers, last is PowerBall
            regular_nums = tokens[:5]
            pb_num = tokens[5] 
            
            for token in regular_nums:
                num = int(token)
                regular_counts[num] = regular_counts.get(num, 0) + 1
            
            pb = int(pb_num)
            pb_counts[pb] = pb_counts.get(pb, 0) + 1
    
    print(" Regular Number Frequencies (1–69)")
    for num in range(1, 70):
        count = regular_counts.get(num, 0)
        print(f"{num:>2}: {count}")
    
    print("\n PowerBall Frequencies (1–26)")
    for num in range(1, 27):
        count = pb_counts.get(num, 0)
        print(f"{num:>2}: {count}")


    # first 10 most frequent regular numbers
    sorted_regular = sorted(regular_counts.items(), key=lambda x: x[1], reverse=True)
    print("\n 10 Most Frequent Regular Numbers:")
    for num, count in sorted_regular[:10]:
        print(f"{num}: {count} times")

    # last 10 least frequent numbers
    sorted_regular_least = sorted(regular_counts.items(), key=lambda x: x[1])
    print("\n 10 Least Frequent Regular Numbers:")
    for num, count in sorted_regular_least[:10]:
        print(f"{num}: {count} times")    
    
    # overdue numbers 
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
    print("\n 10 Most Overdue Regular Numbers:")
    for i in range(10):
        print(overdue[i][1])

powerball_frequency()

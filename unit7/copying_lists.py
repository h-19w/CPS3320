list1 = [1, 2, 3, 4]

list2 = [item for item in list1]
## copies the exact items in list1 -> list2 = [1, 2, 3, 4]

list3 = [item**2 for item in list1]
## copies 2 of each item in list 1 

print(list1)
print(list2)
print(list3)
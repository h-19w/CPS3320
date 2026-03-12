BASE_SIZE = 5

for r in range(BASE_SIZE):
    for c in range(r + 1):
        print('*', end='')
    print()

for r in range(BASE_SIZE):
    for c in range(r, BASE_SIZE):
        print(' ', end='')
    print('*')

for i in range(5):
     if (i!=0):
        for j in range(4-i):
            print(' ', end='')
     for k in range(i):
        print('*', end='')
     print()

for i in range(5):
    for k in range(i):
        print(' ', end='')
    print('*')
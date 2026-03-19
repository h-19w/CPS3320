def main():
    value = 99
    print(f'the value is {value}')
    change_me(value)
    print(f'back in main the value is {value}.')

def change_me(arg):
    print('i am changing the value')
    arg = 0
    print(f'now the value is {arg}')

def change_me(value):
    print('i am changing the value')
    value = 0
    print(f'now the value is {value}')
    # even if the var name is the same as the one in main, the var is a different var so the output is the same as the one w different var name, the value in main is not changed because the value in change_me is a local variable that only exists in the change_me function, it does not affect the value in main. var name. 
    # same var name, but different var, the value in main is not changed because the value in change_me is a local variable that only exists in the change_me function, it does not affect the value in main. var name.

main()
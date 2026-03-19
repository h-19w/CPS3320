def main ():
    # get_name_dw()
    # print(f"hello {name}") # this will not work because name is not defined in the main function, it is only defined in the get_name function.
    get_name()
    print(f"hello {Rname}") # this will work because name is now defined as a global variable in the get_name function.


# def get_name_dw():
#     name = input ("enter your name: ")

def get_name():
    global Rname # this will make the name variable global, so it can be accessed in the main function.
    Rname = input ("enter your name: ")

main()
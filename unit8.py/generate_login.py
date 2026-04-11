import login

def main ():
    first = input('Enter your first name: ')
    last = input('Enter your last name: ')
    idnumber = input('Enter your student ID number: ')
    password = input('Enter a password: ')  
    login_name = login.get_login_name(first, last, idnumber)
    print('Your login name is:', login_name)
    
    if login.valid_password(password):
        print('Your password is valid.')
    else:
        print('Your password is invalid.')

if __name__ == '__main__':
    main()
import login 
def main ():
    password = input('Enter your password: ')
    if login.valid_password(password):
        print('Your password is valid.')
    else:
        print('Your password is invalid.')

if __name__ == '__main__':
    main()
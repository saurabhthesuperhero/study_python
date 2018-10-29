def validate(password=''):
    if( len(password) < 8 ) :
        return False
    elif password.isalpha() :
        return False
    elif password.isnumeric() :
        return False
    else :
        return True


def main():
    password = input('input password : ')
    if (validate(password)):
        print('valid')
    else :
        print('not valid')


main()
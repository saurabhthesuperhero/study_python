try:
    f = open('abc.txt', 'r')
    print(f.read())
except FileExistsError:
    print('file exists error')
except FileNotFoundError:
    print('file not found')
except:
    print('ERROR')

price = input('price : ')
try:
    price = float(price)
    print('price -> ', price)
except ValueError as err:
    print('NaN', err)


class MyException(Exception):
    pass

try:
    raise MyException('error is occured')
except MyException as e:
    print('my exception : ', e)
# comment
```python
# comment

Multiline comment
""" """
```

# list
```python
arr = []

# add
arr.insert(0, 123)
arr.append(321)

# remove
arr.remove(123)

del(arr[0])
# del arr[0]

arr.pop()


# etc
list('abc')           
# ['a', 'b', 'c']

'a/b//cd'.split('/')         
# ['a', 'b', '', 'cd']

arr.index('1')        
# return index

1 in arr              
# true / false

arr.count(1)          
# return count
```


# tuples
    : list와 달리 readonly list
    : 속도

```python
tup = (1, 2, 3, 4)
# 튜플 정의할 때는 주로 () 안 붙임
tup = 1, 2, 3, 4

# tuple unpacking
# str, list, tuple 모두 unpacking 가능
a, b, c, d = tup
list = [1, 2, 3, 4]
a, b, c, d = list
str = '1234'
a, b, c, d = str

# 튜플은 더 적은 공간 사용
# 실수로 튜플 항목이 손상될 염려가 없다
# 함수의 파라매터는 튜플로 전달된다

tuple(list)
```

# dictionary
    = map

```python
dict = {}
dict['a'] = 'apple'
dict['b'] = 'banana'
del dict['a']

# 전체 삭제
dict.clear()

print( dict.get('c') )       
# None or value


#dict()
lol = [['a', 'b'], ['c', 'd'], ['e', 'f']]
dict(lol)     
# {'a': 'b', 'c': 'd', 'e': 'f'}

tos = {'ab', 'bc', 'cd'}
dict(tos)       
# {'c': 'd', 'b': 'c', 'a': 'b'}

# in : key 가 있는지 확인
'a' in dict

# keys()
# values()
# items() : full scan, = for
# 위 세개는 return iterator 객체로 올려줌.

for a, b in dict.items():
    print('%s in %s' % (a, b)))
```

# other
```python
# zip()
days = ['mon', 'tue', 'wed']
fruits = ['banana', 'apple']
sports = ['soccer', 'baseball', 'basketball', 'tennis']
for d, f, s in zip(days, fruits, sports):
    print(d, f, s)

# tuple -> dict
eng = 'mon', 'tue', 'wed'
kor = '월', '화', '수'
list(zip(eng, kor))
dict(zip(eng, kor))


# range
for i range(0, 3)
# 0, 1, 2
list[range(0, 3)]
range(0, 10, 2)

# setdefault()
# dict에 값을 추가하려고 할 때, 
# 키가 있으면 x, 기존 값 return
# 키가 없으면 추가

```


# function
    위치 parameter / 키워드 parameter
```python
def method(p1, p2):
    return 'p1 : ' + str(p1) + ' / p2 : ' + str(p2)

method(100, 200)
method(p2=200, p1=100)
# 'p1 : 100 / p2 : 200'
```
    default parameter
    parameter의 타입도 말해줌
```python
def times(a = 10, b = 20):
    return a * b

times()
# 200
times(5)
# 100
times(b=5)
# 50
```

    가변 parameter
```python
def var_param_test(*p):
    return p

# key, value pair 로 받음 dict
def var_param_test(**p):
    for x, v in p.items():
        print(x, v)
var_param_test(x=1, b=2, c=3)
```

    return
    return문 생략되면 None return
```python
def swap(a,b):
    return b, a
# 다중 return이지만
# 튜플 표현식
# -> 실제로는 튜플로 넘어감
```

# module
    
    import os
    from os import listdir
    import os as winos

```
pip install requests
```

# package
    __init__.py 파일이 디렉토리에 위치하면 파이썬이 패키지로 인식
    내용은 없고, 파일만 존재함.

    from package_name import module_name
    import package_name.module_name

```python
from services import avg
import services.avg
```

# string function
```python

# join
>>> str = 'hello world'
>>> arr = str.split(' ')
>>> joinArr = ', '.join(arr)
>>> joinArr
'hello, world'

# in, not in
>>> 'hello' in 'hello world'
True
>>> 'hello' in 'Hello world'
False
>>> 'hello' not in 'Hello world'
True

# etc
upper()
lower()
isupper()
islower()
isalpha()
isalnum()   # 문자와 숫자로만 구성
isdecimal()
isspace()
istitle()   # 단어가 대문자로 시작
startswith()
endswith()

# formatting
# interpolate

# python2 
'hello world %s' % ('hello')
# %s string
# %d decimal
# %f float

# python3
'{} {}'.format(a, b)
'{2} {0} {1}'.format(a, b, c)
# c a b
d = {'a': 'apple', 'b': 'banana'}
'{0[b]} {0[a]}'.format(d)


# pyperclip
>>> import pyperclip
>>> pyperclip.copy('hello world')
>>> pyperclip.paste()
'hello world'
```


# regular expression | regex
regex101.com

```regex
\b(https?:\/\/)?([\w.]+){1,2}(\.[\w]{2,4}){1,2}\b

\b \b
^ $
```
```python
import re
result = re.match('pattern', 'source string')

phonenum_regex = re.compile(r '\d{3}-\d{4}')

search()
findall()
split()
sub()

>>> import re
>>> reg = re.compile(r'\d{3}-\d{4}-\d{4}')
>>> mo = reg.search('My number is 123-1234-1234')
>>> mo
<re.Match object; span=(13, 26), match='123-1234-1234'>
>>> print(mo.group())
123-1234-1234

# grouping
>>> reg = re.compile(r'(\d{3})-(\d{4}-\d{4})')
>>> mo = reg.search('My number is 123-1234-1234')
>>> mo.group(1)
'123'
>>> mo.group(2)
'1234-1234'
>>> mo.groups()
('123', '1234-1234')

# findall
>>> mo = reg.findall('My number is 123-1234-1234 work 234-2344-2345')
>>> mo
[('123', '1234-1234'), ('234', '2344-2345')]

# flag
# 대소문자 무시
reg = re.compile(r'robocop', re.I')


```


# file read/write

```python

# 파일 경로 리눅스 맥은 /, 윈도우는 \
>>> import os
>>> os.path.join('usr', 'bin', 'spam')
'usr/bin/spam'

>>> os.getcwd()
'/Users/wookee/wookee/python'
>>> os.chdir('..')
>>> os.getcwd()
'/Users/wookee/wookee'

# 현재 디렉토리의 모든 리스트
>>> import glob
>>> glob.glob('*')

# basename dirname
>>> path = os.getcwd()+'/a.txt'
>>> path
'/Users/wookee/wookee/a.txt'
>>> os.path.basename(path)
'a.txt'
>>> os.path.dirname(path)
'/Users/wookee/wookee'


# open()
# write
log = open('test.txt', 'w')
# append
log = open('test.txt', 'a')

log.write('hello world\n')
log.write('hello world2\n')
log.write('hello world3\n')
log.write('hello world4\n')
log.write('hello world5\n')
log.close()

# read
f = open('test.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)

lines = f.readlines()
for line in lines:
    print(line)

f.close()

# 자동으로 close 해줌
with open('test.txt', 'w') as f:
    f.write('hello world')
```

# pickle
    data를 binary로 저장
    binary serialize
```python
>>> import pickle
>>> colors = ['red', 'green', 'black']
>>> f = open('colors.pickle', 'wb')
>>> pickle.dump(colors, f)
>>> f.close()

>>> import pickle
>>> colors
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'colors' is not defined
>>> f = open('colors.pickle', 'rb')
>>> colors = pickle.load(f)
>>> colors
['red', 'green', 'black']
>>> f.close()
```

# shell util = shutil
    파일 및 디렉터리 관리
```python
import shutil
shutil.copy(, )
shutil.move(, )

# 파일 삭제
os.unlink(path)
os.remove(path)

# directory 삭제 = 복원 불가
# 해당 경로가 비어있어야 함
os.rmdir(path)
# 해당 경로가 비어있지 않아도 모든 파일 삭제
shutil.rmtree(path)

# 완전 삭제 대신 휴지통으로 보내기
pip3 install send2trash

import send2trash
send2trash.send2trash(path)

# directory 순회
os.walk(path)
>>> import os
>>> for folder, subfolder, file in os.walk('./'):
...     print( folder, '->', subfolder, file)
...

```

# zip 파일 읽기
```python
import zipfile, os

testzip = zipfile.ZipFile(zipfile_path)
testzip.namelist()
# 압축 파일 내부의 파일 정보
fileinfo = testzip.getinfo(filename_in_zipfile)
fileinfo.file_size
fileinfo.compress_size

# 압축 해제
testzip.extractall()
testzip.close()

# 압축하기
newzip = zipfile.ZipFile('new.zip', 'w')
newzip.write(file_name, compress_type=zipfile.ZIP_DEFLATED)
newzip.close()

```

# exception
```python

try:
    file = open('sales.txt', 'r')
    print(file.read())
except:
    print('file does not exist')

price = input('price : ')
try:
    price = float(price)
    print('price -> ', price)
except ValueError as err:
    print('NaN', err)

# 사용자 정의 예외
class MyException(Exception):
    pass

try:
    raise MyException('error is occured')
except MyException as e:
    print('my exception : ', e)

my exception :  error is occured
```

# loggin
```python
import logging

logging.basicConfig(filename='log.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('start log')

def factorial(n):
    logging.debug('start factorial(%s)' % (n) )
    total = 1
    for i in range(n + 1):
        if not i:
            continue
        total *= i
        logging.debug('i is %s, total is %s' % (i, total) )
    logging.debug('end factorial')
    return total

print(factorial(5))
logging.debug('end log')

# TimedRotatingFileHandler
import logging
from logging import handlers

# formatter setting
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# timedRotatingFileHandler setting
logHandler = handlers.TimedRotatingFileHandler(filename='rotatinglog.log', when='S', interval=5, encoding='utf-8')
logHandler.setFormatter(formatter)
logHandler.prefix = '%Y%m%d'

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(logHandler)

logger.debug('start log')
```

# class
    class 이름은 대문자로 시작, 단어 시작도 대문자
    첫글자가 대문자면 모두 class
```python
class Animal:
    is_alive = True
    age = 1

    def __init__(self, name):
        self.name = name
        print('constructor invoked')

    def descript(self):
        print('name : {0}\nage : {1}\nalive : {2}'.format(self.name, self.age, self.is_alive))


def main():
    cat = Animal('iamcat')
    # print('name : ', cat.name)
    cat.descript()
    print(type(cat))


if __name__ == '__main__':
    main()
```

# inheritance 상속
    상속 이외에 composition(포함)도 있음
    생성자는 상속 받지 않음
```python
class Dog(Animal):
    # 생성자는 상속 받지 않음
    def __init__(self, name, speed):
        Animal.age = 2;
        Animal.__init__(self, name)
        self.speed = speed

    # override
    def descript(self):
        Animal.descript(self)
        print('--override--\nspeed : {0}'.format(self.speed))


def main():
    d = Dog('hello', 100)
    d.descript()
    print(type(d))

if __name__ == '__main__':
    main()
```

# excel
    workbook : file
    worksheet : sheet
    cell : cell
```python
>>> import openpyxl

# workbook 접근
>>> wb = openpyxl.load_workbook('sample.xlsx')
>>> type(wb)
<class 'openpyxl.workbook.workbook.Workbook'>
>>> wb.sheetnames
['Sheet1']

# sheet 접근
>>> sheet = wb['Sheet1']
>>> sheet
<Worksheet "Sheet1">
>>> type(sheet)
<class 'openpyxl.worksheet.worksheet.Worksheet'>
>>> sheet = wb.active

# cell 접근
>>> sheet['B1'].value
'카드명'
>>> sheet.cell(1, 2).value
'카드명'
>>> sheet.cell(column=2, row=1).value
'카드명'

sheet.max_row
sheet.max_column

# 저장
>>> from openpyxl import Workbook
>>> wb = Workbook()
>>> wb.sheetnames
['Sheet']
>>> sheet = wb.active
>>> sheet.title
'Sheet'
>>> sheet.title = '파이썬 공부'
>>> sheet.title
'파이썬 공부'
>>> wb.create_sheet('Sheet2')
<Worksheet "Sheet2">
>>> wb.create_sheet('Sheet3', 1)
<Worksheet "Sheet3">
>>> wb.sheetnames
['파이썬 공부', 'Sheet3', 'Sheet2']

>>> sheet['A1'] = 'hello'
>>> sheet.cell(2, 1, 'world')

>>> for row in row_range:
...     for cell in row:
...             print(cell.value)
...
hello
world
None

>>> wb.save('pytest.xlsx')

# 수식, 병합 등등
sheet['A1'] = '=SUM(A1:A2)'
sheet.merge_cells('C5:D5')

```

# CSV
    탭, 콤마, 수직바 등을 구분자로 사용
    separate, delimeter : ,
    줄바꿈 리눅스/맥 : \n
          윈도우 : \r\n

    엑셀과 CSV 차이
        - 데이터 타입은 문자열
        - 워크시트 없음
        - 이미지 차트 없음

    파이썬에서 CSV 핸들링
        - 리스트나 딕셔너리
        - 리스트 <-> CSV
        - 딕셔너리 <-> CSV
```python
import csv
import pprint


# csv -> list
import csv
import pprint

a_list = []
f = open('filename.csv', 'r')
reader = csv.reader(f)
for row in reader:
    a_list.append(row)
f.close()

with open('filename.csv', 'r') as f:
    reader = csv.reader(f)
    a_list = list(reader)

# list -> csv
# newline=''
# window에서만 넣어주면 됨.
# 안써주면 2칸씩 띄워짐
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['spam', 'eggs', 'bacon', 'ham'])
    writer.writerow(['hello, world', 'eggs', 'bacon', 'ham'])
    writer.writerow([1, 2, 3, 4])


# csv -> dict
with open('filename.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

# OrderedDict 형태 return

```

# api
```python

```

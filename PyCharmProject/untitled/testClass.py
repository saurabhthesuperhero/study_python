class Animal:
    is_alive = True
    age = 1

    def __init__(self, name):
        self.name = name
        print('=====================\nconstructor invoked')

    def descript(self):
        print('name : {0}\nage : {1}\nalive : {2}'.format(self.name, self.age, self.is_alive))


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
    cat = Animal('iamcat')
    # print('name : ', cat.name)
    cat.descript()
    print(type(cat))


    d = Dog('hello', 100)
    d.descript()
    print(type(d))

if __name__ == '__main__':
    main()

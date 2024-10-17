"==============================Функции====================================="
# Функция - это именованный блок кода, который может принимать аргументы и вовзращать результат


def my_sum(a, b):
    return a+b

res = my_sum(5, 5)
print(res)

def my_len(obj):
    count = 0
    for i in obj:
        count += 1 # инкремент
    return count

print(my_len((1,2,3,4,5,6,7,8,9,10))) # 10

# print(my_len(), 'hello', )

list1 = [1,2,3,4,5]
count = 0
for i in list1:
    count += 1
print(count)

"""
ФУНКЦИИ СОБЛЮДАЮТ ПРИНЦИП DRY (don't repeat yourself) - НЕ ПОВТОРЯЙСЯ
"""

"===============================Аргументы и параметры==========================="
"""
параметры - переменные внутри функции, значения которым мы задаем при вызове функции (т.е. те переменные, которые мы пишем в круглых скобках, когда пишем def)

аргументы - значения, которые мы передаем при вызове функции
"""

"========================Виды параметров==================================="
# 1. обязательные
# 2. не обязательные
# 2.1 с дефолтным значением (со значением по умолчанию)
# 2.2 args (все позиционные аргументы, которые не попали в обязательные, и с дефолтом)
# 2.3 kwargs (все лишние именованные аргументы)

"===================================Виды аргументов=============================="
# 1. позиционные (по позиции)
# 2. именованные (по названию (параметр=значение))


def add_or_add_10(num1, num2=10):
    """
    Складывает 2 числа

    Если второе число не передать, сложит первое с 10
    """
    return num1 + num2

num = 100
print(add_or_add_10(num))

"--------------------------*----------------------------"
list1 = list(range(1, 11))
print(list1) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [*range(1, 11)]
print(list2) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


dict1 = {'a': 1, 'b': 2, 'c': 3}
list3 = [*dict1]
dict2 = {**dict1} # {'a': 1, 'b': 2, 'c': 3}
print(dict2)
print(list3)


def func(a, b=10, *args, **kwargs):
    print('a - ', a)
    print('b - ', b)
    print('args - ', args)
    print('kwargs - ', kwargs)


# func() # TypeError: func() missing 1 required positional argument: 'a'
func(b=100, a=12)

# a -  100
# b -  12
# args -  (1, 2, 3, 4, 5, 6, 7, 8, 9)
# kwargs -  {'hello': 'world', 'name': 'Nikita', 'city': 'Bishkek'}

"==============================Lambda==============================="
# lambda - анонимная функция, которая записывается в одну строку
lambda_func = lambda x: x ** 10
print(lambda_func(10)) # 10000000000

"==========================Калькулятор==============================="

calc = {
    '+': lambda n1,n2: n1 + n2,
    '-': lambda n1,n2: n1 - n2,
    '*': lambda n1, n2: n1 * n2,
    '**': lambda n1, n2: n1 ** n2,
    '/': lambda n1, n2: n1 / n2,
    '//': lambda n1, n2: n1 // n2,
    '%': lambda n1, n2: n1 % n2
}


def main():
    try:
        num1 = int(input('Введите первое число: '))
        num2 = int(input('Введите второе число: '))
        operation = input('Введите операцию: ')
        func = calc[operation]
        result = func(num1, num2)
        print(num1, operation, num2, '=', result)

    except ValueError:
        print('Введите число!')
    except KeyError:
        print('Операция не верная!')
    except ZeroDivisionError:
        print('На ноль делить нельзя')


# while True:
#     main()
#     if input('Завершить (yes/no)?').lower() == 'yes':
#         break

db = [
    {'name': 'Nikita', 'password': hash('12345678')},
    {'name': 'hello', 'password': hash('hello world')},
]


def in_database(name):
    for user in db:
        if user['name'] == name:
            return True
    return False

def register(name, password1, password2):
    if in_database(name):
        raise Exception('Пользователь с таким именем уже существует!')
    if password1 != password2:
        raise Exception('Пароли не совпали!')
    user = {'name': name, 'password':hash(password1)}
    db.append(user)
    print(db)
    return 'Вы успешно зарегестрировались!'

def login(name, password):
    if not in_database(name=name):
        raise Exception('Пользователь не найден!')
    for user in db:
        if user['name'] == name:
            if user['password'] != hash(password):
                raise Exception('Пароль не верный!')
    return 'Вы успешно вошли в систему'

from decorators import time_decorator

@time_decorator
def main():
    print('Добро пожаловать!')
    while True:
        try:
            action = input('Register:1, Login:2, Quit:3\n')

            if action == '3':
                break
            elif action == '1':
                name = input('Введите ваше имя: ')
                p1 = input('Введите пароль: ')
                p2 = input('Повторите пароль: ')
                print(register(name=name, password1=p1, password2=p2))
            elif action == '2':
                name = input('Введите ваше имя: ')
                password = input('Введите ваш пароль: ')
                print(login(name=name, password=password))
            else:
                print('Не корректный выбор!')
        except Exception as error:
            print(error)

main()
# print(db)

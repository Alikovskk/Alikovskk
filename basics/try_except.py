"===================================Exceptions============================="
# Исключения (ошибки) - объекты, которые прерывают работу кода, если не были обработаны

SyntaxError
# исключение, которое выходит в случае, когда в коде допущена синтаксическая ошибка

# print(
"""
File "/mnt/c/Users/User/Desktop/ADA_lections/basics/try_except.py", line 7
print(
       ^
SyntaxError: '(' was never closed
"""

# a =

"""
File "/mnt/c/Users/User/Desktop/ADA_lections/basics/try_except.py", line 15
a =
    ^
SyntaxError: invalid syntax
"""

NameError
# исключение, которые выходит, когда мы обращаемся к несществуюшей переменной

# print(a)

"""
File "/mnt/c/Users/User/Desktop/ADA_lections/basics/try_except.py", line 27, in <module>
print(a)
        ^
NameError: name 'a' is not defined
"""

IndexError
# исключение, которое выходит, когда мы обращаемся по несуществующему индексу

# list_ = [1,2,3,4,5]
# print(list_[1000])
"""
File "/mnt/c/Users/User/Desktop/ADA_lections/basics/try_except.py", line 40, in <module>
print(list_[1000])
        ~~~~~^^^^^^
IndexError: list index out of range
"""

KeyError
# исключение, которое выходит, когда обращаемся по несуществующему ключу
dict_ = {'a': 1}
# print(dict_['b'])
"""
File "/mnt/c/Users/User/Desktop/ADA_lections/basics/try_except.py", line 51, in <module>
print(dict_['b'])
        ~~~~~^^^^^
KeyError: 'b'
"""

ValueError
# когда мы передаем в функцию не коректный для нее тип данных
# когда мы распаковываем итерируемый объект на несколько переменных, и количество переменных не совпадает с количеством элементов в итерируемом объекте
# int('10d')
"""
Traceback (most recent call last):
  File "/mnt/c/Users/User/Desktop/ADA_lections/basics/try_except.py", line 62, in <module>
    int('10d')
ValueError: invalid literal for int() with base 10: '10d'
"""
# a,b,c = [1,2]
"""
Traceback (most recent call last):
  File "/mnt/c/Users/User/Desktop/ADA_lections/basics/try_except.py", line 69, in <module>
    a,b,c = [1,2]
    ^^^^^
ValueError: not enough values to unpack (expected 3, got 2)
"""

TypeError
# когда мы пытаемся использовать методы, не свойственные какому то типу данных
# или когда мы пытаемся передать функции больше или меньше аргументов, чем принимает функция

# for i in 123:
#     ...
"""
Traceback (most recent call last):
  File "/mnt/c/Users/User/Desktop/ADA_lections/basics/try_except.py", line 82, in <module>
    for i in 123:
TypeError: 'int' object is not iterable
"""

# 5 + 'str'
"""
Traceback (most recent call last):
  File "/mnt/c/Users/User/Desktop/ADA_lections/basics/try_except.py", line 91, in <module>
    5 + 'str'
    ~~^~~~~~~
TypeError: unsupported operand type(s) for +: 'int' and 'str'
"""
# {[123]: "hello"}
"""
Traceback (most recent call last):
  File "/mnt/c/Users/User/Desktop/ADA_lections/basics/try_except.py", line 99, in <module>
    {[123]: "hello"}
TypeError: unhashable type: 'list'
"""

ZeroDivisionError
# выходит при делении на ноль
# 45 / 0
"""
Traceback (most recent call last):
  File "/mnt/c/Users/User/Desktop/ADA_lections/basics/try_except.py", line 109, in <module>
    45 / 0
    ~~~^~~
ZeroDivisionError: division by zero
"""
# 45 % 0
"""
Traceback (most recent call last):
  File "/mnt/c/Users/User/Desktop/ADA_lections/basics/try_except.py", line 117, in <module>
    45 % 0
    ~~~^~~
ZeroDivisionError: integer modulo by zero
"""

# 45 // 0
"""
Traceback (most recent call last):
  File "/mnt/c/Users/User/Desktop/ADA_lections/basics/try_except.py", line 126, in <module>
    45 // 0
    ~~~^^~~
ZeroDivisionError: integer division or modulo by zero
"""

IndentationError
# выходит, когда мы неправильно используем отступы

    # a = 5

"""
nt/c/Users/User/Desktop/ADA_lections/basics/try_except.py
  File "/mnt/c/Users/User/Desktop/ADA_lections/basics/try_except.py", line 138
    a = 5
IndentationError: unexpected indent
"""
# for i in range(10):
# print(i)

"""
nt/c/Users/User/Desktop/ADA_lections/basics/try_except.py
  File "/mnt/c/Users/User/Desktop/ADA_lections/basics/try_except.py", line 147
    print(i)
    ^
IndentationError: expected an indented block after 'for' statement on line 146
"""

Exception
# исключение, которое создали, чтобы его вызывать

"===============================Вызов исключений============================="
# raise NameError
# raise позволяет вручную вызвать исключение

# raise NameError('Неправильное имя пользователя')
# NameError: Неправильное имя пользователя

"=================================Обработка исключений==========================="
# чтобы код не прекращал работу когда возникает исключение, мы можем использовать конструкцию try-except, и обрабатывать вызванное исключение

# try:
#     # код, который возможно вызовет ошибку
#     num = int(input('Введите число: '))
# except ValueError: # ошибка, которая может возникнуть
#     # код, который отрабатывает только если ошибка вызвалась
#     print('Введи число!')
# else:
#     # код который отработает только если никакая ошибка не вышла
#     print('Введенное число', num)
# finally:
#     # код, который отработает вообще в любом случае
#     print('До свидания')


# try:
#     raise ValueError
# except (SyntaxError, NameError): # except не сработает, потому что не передали ValueError в скобки
#     print('Вышла одна из этих ошибок: (SyntaxError, NameError)')

# try:
#     raise TypeError
# except Exception as error:
#     print('Ошибка', type(error).__name__)


"==================================Декораторы====================================="
# функция высшего порядка - функция, которая принимает в аргументы функцию, создает внутри себя функцию, вызывает функцию, и возвращает функцию

# декоратор - функция высшего порядка, которая нужна чтобы расширять функционал функции не изменяя ее (функция обертка)

def time_decorator(func):
    def wrapper(*args, **kwargs):
        from datetime import datetime
        start = datetime.now()
        func(*args, **kwargs)
        finish = datetime.now()
        print(f'Total time: {finish - start}')
    return wrapper

@time_decorator
def hello():
    print('hello world')

# hello()
# decorator = time_decorator(hello)
# decorator()

@time_decorator
def my_sqrt(x):
    print(x ** 0.5)

# my_sqrt(25)

def func_start_time(func):
    def wrapper(*args, **kwargs):
        from datetime import datetime
        now = datetime.now()
        correct_format = now.strftime('%d.%m.%Y %H:%M')
        print('Функция запущена', correct_format)
        func(*args, **kwargs)
    return wrapper

@func_start_time
def func():
    print('hello world')

# func()

def decorator(num):
    def inner_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num):
                func(*args, **kwargs)
        return wrapper
    return inner_decorator

@decorator(4)
def hello():
    print('hello world')

hello()

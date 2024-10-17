"=================================Comprehensions================================"
# генератор, с помозью которого мы можем создавать последовательности используя цикл for в одну строку

"""
Синтаксис:

результат for элемент in последовательность
результат for элемент in последовательность if фильтр -- ФИЛЬТРАЦИЯ
результат if условие else результат2 for элемент in последовательность -- УСЛОВИЕ
"""

comprehension = (i for i in range(1, 6))
print(comprehension) # <generator object <genexpr> at 0x7f6b717a0ac0>
# генератор - итерируемый объект, который не хранит в себе полностью всю последовательность данных, а создает их когда требуется

print(next(comprehension))
print(next(comprehension))
print(next(comprehension))
print(next(comprehension))
print(next(comprehension))

# next - функция, которая запрашивает у генератора текущий элемент и генератор создает следующий элемент


"===============================List Comprehension=========================="
# 1 способ
list_comprehension = list((i ** 2 for i in range(1, 6)))
print(list_comprehension) # [1, 4, 9, 16, 25]

# 2 способ
list_comprehension1 = [i**2 for i in range(1, 6)]
print(list_comprehension1) # [1, 4, 9, 16, 25]

"Создайте список состоящий из четных чисел от 1 до 10 используя comprehension"
list_comprehension2 = [i for i in range(1, 11) if i % 2 == 0]
print(list_comprehension2) # [2, 4, 6, 8, 10]

list_comprehension3 =  [i for i in range(2, 11, 2)]
print(list_comprehension3)

list_ = []
for i in range(1, 11):
    if i % 2 == 0:
        list_.append(i)
print(list_)

a = 5
"Создайте список состоящий из 5 строк 'hello' используя comprehension"
# ['hello', 'hello', 'hello', 'hello', 'hello']
list2 = ['hello' for i in range(5)]
print(list2) # ['hello', 'hello', 'hello', 'hello', 'hello']

list3 = ['hello'] * 5
print(list3)

hello_list = []
for _ in range(5):
    hello_list.append('hello')

print(hello_list)

"Создайте список состязий из чисел от 1 до 10, но вместо чисел написать 'четное' или 'нечетное'"
# ['нечетное', 'четное', 'нечетное'...]

list4 = ['четное' if i % 2 == 0 else 'нечетное' for i in range(1, 11)]
print(list4)

list1 = []
for i in range(1, 11):
    list1.append('четное'if i % 2 == 0 else 'нечетное')
print(list1)

list1 = []
for i in range(1, 11):
    if i % 2 == 0:
        list1.append('четное')
    else:
        list1.append('нечетное')


"создать список из существующего списка, оставив только строки"
list1 = ['hello', 'python', 1, 2, {1: 'a'}, [1, 2, 3], 'world']

new_list = []
for i in list1:
    if type(i) == str:
        new_list.append(i)
print(new_list)

list_comprehension = [i for i in list1 if type(i) == str]
print(list_comprehension)

"=================================Dict Comprehension========================"
dict1 = {i: i**2 for i in range(1, 11)}
print(dict1)

# Дан словарь, создайте его копию с помощью comrehension
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {key: value for key, value in dict1.items()}
print(dict2)

"Дан словарь, поменяйте ключи со значениями с помощью comprehension"
dict3 = {value: key for key, value in dict1.items()}
print(dict3)

"Дан словарь, где значения - списки с числами, создайте словарь, где значениями будут суммы этих списков"

dict1 = {
    "a": [1,2,3,4],
    "b": [10,111,222,333],
    "c": [1, 2, 543]
}

dict2 = {key: sum(value) for key, value in dict1.items()}
print(dict2)

# Создайте словарь с ключами - числа от 1 до 10, а значениями числа в виде строк
# {1: '1', 2: '2', 3: '3'...}
dict1 = {i: str(i) for i in range(1, 10)}
print(dict1)

"Даны 2 списка, создайте словарь, ключами будут элементы из первого списка, а значениями - элементы второго списка"
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']

# dict1 = {}
# for index in range(len(list1)):
#     key = list1[index]
#     value = list2[index]
#     dict1[key] = value

# print(dict1)


dict1 = {list1[index]: list2[index] for index in range(len(list1))}
print(dict1)

dict3 = dict(zip(list1, list2))
print(dict3)

"==================================Вложенные comprehension======================="
# создайте словарь, где ключами будут числа от 1 до 5, а значениями - списки с числами от 1 до этого числа
# {1: [1], 2: [1, 2], 3: [1, 2, 3], 4: [1, 2, 3, 4], 5: [1, 2, 3, 4, 5]}

# dict1 = {}
# for i in range(1, 6):
#     key = i
#     value = [j for j in range(1, i + 1)]
#     dict1[key] = value

# print(dict1)

# dict1 = {i: [j for j in range(1, i + 1)] for i in range(1, 6)}
# print(dict1)


"Создать список, состоящий из 10 списков, в которых строка hello world повторяется по 5 раз"
# [['hello world', 'hello world', 'hello world', 'hello world', 'hello world'],
# ['hello world', 'hello world', 'hello world', 'hello world', 'hello world']]
# 1) способ

list1 = []
for i in range(1, 11):
    inner_list = []
    for j in range(5):
        inner_list.append('hello world')
    list1.append(inner_list)

# print(list1)

list1 = [['hello world']* 5 for i in range(10)]
# print(list1)

list1 = [['hello world' for j in range(5)] for i in range(10)]
# print(list1)

list1 = [['hello world']*5] *10
print(list1)

"создать список, состоящий из 10 списков, в которых будут числа от 1 до 5"
# [[1,2,3,4,5],
#  [1,2,3,4,5],
#  [1,2,3,4,5],
#  [1,2,3,4,5],
#  [1,2,3,4,5],
#  [1,2,3,4,5],
#  [1,2,3,4,5],
#  [1,2,3,4,5],
#  [1,2,3,4,5],
#  [1,2,3,4,5]]

list1 = [[j for j in range(1, 6)] for i in range(10)]
list2 = [list(range(1,6)) for i in range(10)]
list3 = [list(range(1,6))]*10
# print(list3)

"создать словарь, где ключами будут числа от 1 до 5, а значениями словари, в которых ключи будут от 1 до этого числа, а значениями будут списки от 1 до этого числа"

{
    1:{
        1:[1]
    },
    2:{
        1: [1],
        2: [1, 2]
    },
    3: {
        1: [1],
        2: [1, 2],
        3: [1,2,3]
    }
}

dict1 = {}
for i in range(1, 6):
    inner_dict = {}
    for j in range(1, i+1):
        list_ = []
        for k in range(1, j+1):
            list_.append(k)
        inner_dict[j] = list_
    dict1[i] = inner_dict

# print(dict1)

dict2 = {
    i:{
        j:[k for k in range(1, j+1)] for j in range(1, i+1)
    }
    for i in range(1, 6)
}

# print(dict2)

dict3 = {i: {j: list(range(1, j+1)) for j in range(1, i+1)} for i in range(1, 6)}

"Дан словаь:"
dict1 = {"sedan": 1500, 'SUV':2000, 'pickup': 2500, 'minivan':1600, 'vann': 2400, 'semi': 13600, 'bicycle': 7, 'motorcycle': 110}
"""
Создайте словарь dict2:
- Ключи должны быть те же, что и в первом словаре, но каждый символ замените на ''
- Значением должно быть количество повторений символа 'i' в этом ключе
"""

dict2 = {k.replace('i', ''):k.count('i') for k in dict1}
print(dict2)
dict_ = {
    'Dasha': {
        'likes': 15,
        'comments': [
            {'id': 1, 'text': 'some text'},
            {'id': 2, 'text': 'some text'},
        ],
        'rating': 2
    },
    'Luna': {
        'likes': 12,
        'comments': [
            {'id': 1, 'text': 'some text'},
            {'id': 2, 'text': 'some text'},
            {'id': 3, 'text': 'some text'},
        ],
        'rating': 1
    },
    'Rena': {
        'likes': 26,
        'comments': [
            {'id': 1, 'text': 'some text'},
            {'id': 2, 'text': 'some text'},
            {'id': 3, 'text': 'some text'},
            {'id': 4, 'text': 'some text'},
            {'id': 5, 'text': 'some text'},
            {'id': 6, 'text': 'some text'},
        ],
        'rating': 2
    }
}
"""
Используя приведенный словарь dict_, создайте список из id,
которые хранятся под ключом comments. Берите только те комментарии,
количество которых больше 3
"""
ids = []

# for inner_dict in dict_.values():
#     comments = inner_dict['comments']
#     if len(comments) > 3:
#         for comment in comments:
#             ids.append(comment['id'])

# print(ids)

ids = [comment['id'] for inner_dict in dict_.values() if len(inner_dict['comments']) > 3 for comment in inner_dict['comments']]
print(ids)

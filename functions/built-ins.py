'============================Встроенные функции=============================='
# map, zip, filter, reduce, enumerate

"""
zip - функция, которая соединяет несколько последовательностей (получаем генератор, в котором элементы - tuple)
"""

# list1 = [1, 2, 3, 4, 5]
# list2 = ['a', 'b', 'c']
# list3 = [10.5, 20.6, 30.8, 23.12]

# zipped = zip(list1, list2, list3)
# print(zipped) # <zip object at 0x7f337013b0c0>, возвращается ссылка на ячейку в памяти

# for element in zipped:
#     print(element)

# (1, 'a', 10.5)
# (2, 'b', 20.6)
# (3, 'c', 30.8)

# list1 = [1, 2, 3, 4, 5]
# list2 = ['a', 'b', 'c', 'd', 'e']
# dict_ = list(zip(list1, list2))
# print(dict_) # {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}


"""
enumerate - нумерует последовательность (по дефолту с 0) (так-же получаем генератор)
"""
enumerated = enumerate('hello') # <enumerate object at 0x7f93c780bbf0>
print(enumerated)
for i in enumerated:
    print(i)
# (0, 'h')
# (1, 'e')
# (2, 'l')
# (3, 'l')
# (4, 'o')

string = 'hello world'
print(list(enumerate(string[5:]))) # [(0, ' '), (1, 'w'), (2, 'o'), (3, 'r'), (4, 'l'), (5, 'd')]

"""
map - принимает функцию и последовательность (записывает в новую последовательность результат функции, в которую передаются элементы последовательности)
"""

list1 = ['1', '2', '3', '4', '5']
mapped = list(map(int, list1))
print(mapped) # [1, 2, 3, 4, 5]


string = 'hello world'
res = ''.join(map(lambda x: x.upper(), string))
print(res) # HELLO WORLD

list1 = [1, 2, 3, 4, 5]
res = list(map(lambda x: x ** 2, list1))
print(res) # [1, 4, 9, 16, 25]

def to_2_degree(x):
    return x ** 2

print(list(map(to_2_degree, list1))) # [1, 4, 9, 16, 25]


"""
filter - возвращает генератор, с элементами, прошедшими фильтр (какое-то условие), принимает функцию, и последовательность
"""

list1 = [3, -5, -10, 0, 1, 2, 3, 4, 5, -100]
filtered_list = list(filter(lambda x: x > 0, list1))
print(filtered_list) # [3, 1, 2, 3, 4, 5]

users = [
    {'name': 'Nastya', 'age': 22},
    {'name': 'Nikita', 'age': 14},
    {'name': 'Marat', 'age': 17}
]
result = list(filter(lambda x: x['age']>15, users))
print(result) # [{'name': 'Nastya', 'age': 22}, {'name': 'Marat', 'age': 17}]


"""
reduce - принимает функцию и последовательность, возвращает 1 результат (передаваемая функция должна принимать 2 аргумента), оборачивать в list/dict не нужно и нельзя
"""

from functools import reduce

list1 = [1,2,3,4,5, 200]
res = reduce(lambda x, y: x + y, list1)
print(res) #15
res = reduce(lambda x, y: x*y, list1)
print(res) # 24000

def multiply(x, y):
    return x * y
res = reduce(multiply, list1) # 24000
print(res)

string = 'hello'
res = reduce(lambda x, y: x+'%'+y, string)
print(res) # h%e%l%l%o

# total_sum = 0ц
# for i in list1:
#     total_sum += i

# print(total_sum)

list_ = [1, 2, 3, 21, 23, 54, -123, 542, 214,42,23,4]
# выведите самое маленькое число, с помощью reduce

result = reduce(lambda x, y: x if x<y else y, list_)
print(result)

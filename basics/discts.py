"================================Словари===================================="
# dict - это изменяемый, итерируемый, неупорядоченный, неиндексируемый тип данных, для хранения данных в парах (ключ: значение)

user = {
    "name": "Nikita",
    "city": "bishkek",
    "last_name": 'Grebnev'
}

print(user)
print(user["name"])

# ключами могут быть только неизменяемые типы данных
# dict_ = {
#     [1, 2, 3]: 'nikita',
#     {'a': 1}: 'bishkek',
#     {1, 2, 3}: '20'
# }
# print(dict_)

# dict2 = {
#     'name': [1, 2, 3],
#     "age": {1, 2, 3}
# }
# print(dict2)

"===================================Создание========================"
# 1 способ
dict_ = {'name': 'nikita', 'city': 'Bishkek'}
print(dict_)

# 2 способ
dict1 = dict(["ab", "cd", "ef"])
print(dict1)

# 3 способ
dict3 = {}
dict3['name'] = 'Nikita'
dict3['age'] = 20
dict3['city'] = 'Bishkek'
print(dict3)
dict3["name"] = 'Almaz'
print(dict3)
"===============================Методы словарей=================================="
# get() - метод, который возвращает значение по ключу, если такого ключа нет, то возвращает None или дефолтное значение

user = {
    "name": "Nikita",
    "city": "bishkek",
    "last_name": 'Grebnev'
}

print(user["city"])
print(user.get('city'))
# print(user['id']) # KeyError: 'id'
print(user.get('id')) # None
print(user.get('name'))


# pop() - удаляет пару по ключу, и возвращает значение
# dict1 = {'a': 1, 'b': 2, 'c': 3} # {'b': 2, 'c': 3}
# popped = dict1.pop('a')
# print(dict1)
# print(popped) # 1


# popitem() - удаляет последнюю пару и возвращает ее
dict1 = {'a': 1, 'b': 2, 'c': 3}
popped = dict1.popitem()
print(dict1) # {'a': 1, 'b': 2}
print(popped) # ('c', 3) - вернул пару ключ значение в типе данных tuple

# update() - расширяет словарь парами из второго словаря
dict1 = {'a': 1, 'b': 2}
dict2 = {"c": 3, 'd': 4}
dict1.update(dict2) 
print(dict1) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(dict2) # {'c': 3, 'd': 4}

# clear() - очищает словарь полностью
dict1.clear()
print(dict1)


"""
keys(), values(), items()
keys() - метод, котоырй возвращает ключи
values() - метод, который возвращает значения
items() - метод, который возвращает пары ключ - значение, в типе данных tuple
"""

user = {
    "name": "Nikita",
    "city": "bishkek",
    "last_name": 'Grebnev'
}

print(user.keys()) # dict_keys(['name', 'city', 'last_name'])
print(user.values()) # dict_values(['Nikita', 'bishkek', 'Grebnev'])
print(user.items()) # dict_items([('name', 'Nikita'), ('city', 'bishkek'), ('last_name', 'Grebnev')])

"==========================Итерирование словарей================================"
user = {
    "name": "Nikita",
    "city": "bishkek",
    "last_name": 'Grebnev'
}

for key in user:
    print(key)
    # при итерации словаря будут приходить ключи


for key in user.keys():
    print(key)
    # при итерации dict_keys тоже приходят ключи

for value in user.values():
    print(value)
    # при итерации dict_values приходят значния

for key, value in user.items():
    print(f'ключ: {key}, значние: {value}')
    # ('name', 'Nikita')


# Вам дан словарь
dictionary = {'a': 1, 'b': 2, 'c': 3}
# создать новый словарь, поменяв местами ключи со значниями 
# {1: 'a', 2: 'b', 3: 'c'}

dict_ = {}
for key, value in dictionary.items():
    dict_[value] = key
print(dict_) # {1: 'a', 2: 'b', 3: 'c'}

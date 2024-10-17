"===================================Set======================================"
# множество - изменяемый, неупорядоченный, итерируемый, неиндексируемый тип данных, прелназначенный для хранения уникальных значений. Множества могут хранить в себе ТОЛЬКО неизменяемые типы данных. 


# set1 = {1, 2, 3, 4}
# set2 = {True, False, 1, 1, 1, 1, 1, 1, 1, 1, 1}
# print(set2) # {False, True}
# set4 = {1, 2, 3, 4, 4, 4, 4, 2, 2, 2, 5, 5, 5}
# print(set4)

# set3 = {(1, 2, 3), 1, 2, 3}
# print(set3) # {1, 2, 3, (1, 2, 3)}


"==========================Методы Set========================================"
# add() - добавляет элементы в set

# set1 = {1, 2, 3}
# set1.add(3)
# print(set1) # {1, 2, 3} - не добавил тройку, потому что она уже там есть
# set1.add(4)
# print(set1) # {1, 2, 3, 4} - добавил, потому что 4 нет в множестве, и это значение уникально


# pop() - удаляет случайный элемент из set

# set1 = {1, 2, 3, 4, 5, 6}
# popped = set1.pop()
# print(set1) # {2, 3, 4, 5, 6}
# print(popped) # 1


# # remove() - удаляет элемент из set по значению
# set2 = {1, 2, 3, 4, 5, 6}
# set2.remove(6)
# set2.remove(4)
# print(set2) # {1, 2, 3, 5}


# difference() (-) - находит отличие между двумя set

# set1 = {1, 2, 3}
# set2 = {3, 5, 6}

# print(set1.difference(set2)) # {1, 2}
# print(set2.difference(set1)) # {5, 6}
# print(set1 - set2) # {1, 2}
# print(set2 - set1) # {5, 6}


# symmetric_diffence() - сравнивает 2 set и возвращает set который состоит из уникальных значений двух set'ов

# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# print(set1.symmetric_difference(set2)) # {1, 2, 4, 5}
# print(set2.symmetric_difference(set1)) # {1, 2, 4, 5}


# intersection() (&) - находит пересечения в двух set, то есть, сравнивает их, и возвращает только те значения, которые есть и в set1 и в set2

# set1 = {1, 2, 3, 4, 5, 6}
# set2 = {3, 4, 5, 6, 7, 8}
# print(set1.intersection(set2)) # {3, 4, 5, 6}
# print(set2.intersection(set1)) # {3, 4, 5, 6}
# print(set1 & set2) # {3, 4, 5, 6}


# for i in set1:
#     print(i)

# set3 = {1, 4, 2, 3, 6, 7, 8, 10}
# set3.remove(7)
# print(set3)

# Создайте SET который хранит в себе все методы для работы с SET. Создайте второй SET который хранит в себе методы для работы с Dictionary которые вы  узнали. Проверьте какие методы похожи у этих типов данных.

# dir() - возвращает все методы которые есть у типа данных, который передали

# print(dir({1: 'a'}))


set_sets = {'__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 
'symmetric_difference', 'symmetric_difference_update', 'union', 'update'}

set_dict = {'__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'}

print(set_sets & set_dict)
# {'copy', '__doc__', '__gt__', '__format__', '__ge__', '__ior__', '__subclasshook__', '__iter__', '__delattr__', 'update', '__init_subclass__', '__reduce_ex__', '__sizeof__', '__hash__', 'pop', '__new__', '__contains__', '__setattr__', '__ror__', '__ne__', '__len__', '__reduce__', '__str__', '__dir__', '__repr__', '__getattribute__', '__init__', 'clear', '__le__', '__lt__', '__class__', '__class_getitem__', '__eq__', '__getstate__', '__or__'}

# найти объекты, которые есть и в set2 и в set3

set2 = {'Python', 'it', 'c++', 'Java', 'programming'}
set3 = {'html', 'css', 'c++', 'Java', 'dart'}

print(set2.intersection(set3)) # {'c++', 'Java'}

# В set3 найти объекты которых нет в set2

print(set3.difference(set2)) # {'html', 'css', 'dart'}
print(set3 - set2) # {'html', 'css', 'dart'}


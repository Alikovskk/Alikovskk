# "===================================List===================================="
# # списки - это изменяемый, индексируемый, упорядоченный, итерируемый тип данных, который предназначен для хранения любых данных в определенном порядке


# list1 = [1, 2, 3, 4, 5, True, False, [1,2,3], {'a': 1}, [[[(1,2,3)]]]]
# print(list1[-1]) # (1, 2, 3)
# print(list1[-1][-1][-1][-1][-1]) # 3

# list2 = list('hello') # ['h', 'e', 'l', 'l', 'o']
# print(list2)

# list3 = list(range(11))
# print(list3)

# list4 = [1] * 5
# print(list4)

# "====================================методы списков==========================="
# # append() - добавляет элемент в конец списка
# list2 = [1, 2, 3]
# list2.append(1)
# list2.append(454)
# list2.append(True)
# list2.append([1, 'hello'])
# print(list2)


# # pop() - удаляет элемент из списка по индексу и результатом метода будет удаленный элемент (метод возвращает удаленный элемент), если не передать индекс - автоматически удалит элемент с конца

# deleted_element = list2.pop(0)
# print(list2, deleted_element)
# element = list2.pop()
# print(element)
# print(list2)


# # remove() - удаляет элемент по значению
# list_ = [True, False, 1, 2, 3]
# list_.remove(True)
# print(list_)
# list_.remove(3)
# print(list_)

# # count() - считает количнство принятого элемента в списке
# list_ = ['hello', 'hello', 'hello']
# print(list_.count('hello'))
# print(list_.count('h'))

# # index() - возвращает индекс первого вхождения принятого элемента
# list_ = ['hello', 'hello', 'hello', 1, 2, 3, [1, 2, 3, True], (True, False, 23)]
# print(list_.index('hello')) # 0
# print(list_.index(1)) # 3

# # extend() - добавляет элементы принятого списка в первый список, изменяя его
# list5 = [1, 2, 3]
# list6 = [4, 5, 6]
# list5.extend(list6)
# print(list5) # [1, 2, 3, 4, 5, 6]

# # sort() - сортирует список, состоящий из элементов одного типа данных
# list3 = .[23, 123, 243541, 23,1, 3533, 54, 2, 3, 4, 5]
# # list3.sort()
# # print(list3) # [1, 2, 3, 4, 5, 23, 23, 54, 123, 3533, 243541]


# # clear() - очищает список
# # list3.clear()
# # print(list3)
# # []

# # list1 = [1, 2, 3, [31,132, 4,132,3,4,534,21,32,34,1434,3,23,42,34,1324,31]] # 4
# # print(len(list1))

# # a, b, c = 1, 2, 3
# # print(a) # 1
# # print(b) # 2
# # print(c) # 3

# # a, b, c = ['Nikita', 'bishkek', 'kyrgyzstan']
# # print(a)
# # print(b)
# # print(c)


# Дан список из целых чисел, нужно найти сумму первого и последнего элемента списка, записать результат в переменную result

# list_ = [100, 200, 232, 329, 1000]
# result = list_[0] + list_[-1]
# print(result)


# Дан список чисел, и число которое нужно принять в переменную x от пользователя, определите присутствует ли число x в спискe, если да то создайте переменную found и присвойте ей значение True, так-же выведите индекс этого число

# list1 = [1, 2, 3, 4, 5]
# x = int(input('Введите число'))
# found = False

# if list_[0] == x:
#     found = True
#     print(f'переменная Found = {found}, Индекс искомого элемента = {list_.index(list_[0])}')

# elif list_[1] == x:
#     found = True
#     print(f'переменная Found = {found}, Индекс искомого элемента = {list_.index(list_[1])}')

# elif list_[2] == x:
#     found = True
#     print(f'переменная Found = {found}, Индекс искомого элемента = {list_.index(list_[2])}')

# elif list_[3] == x:
#     found = True
#     print(f'переменная Found = {found}, Индекс искомого элемента = {list_.index(list_[3])}')

# elif list_[4] == x:
#     found = True
#     print(f'переменная Found = {found}, Индекс искомого элемента = {list_.index(list_[4])}')


# list_ = [f'искомое число = {num}' for num in list1 if num == x]
# print(list_)


# Дан список чисел, удалите все числа, значение которых равно 0, распечатайте итоговый список без 0
list_ = [0, 10, 0, 25, 0]

if list_[0] == 0:
    list_.pop(0)
# [10, 0, 25, 0]
if list_[0] == 0:
    list_.pop(0)
# [10, 0, 25, 0]
if list_[1] == 0:
    list_.pop(1)
# [10, 25, 0]
if list_[2] == 0:
    list_.pop(2)
# [10, 25]
print(list_)

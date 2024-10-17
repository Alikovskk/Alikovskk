"========================Циклы============================="
# Цикл - это блок кода, который отрабатывает несколько раз
# for - цикл, который работает с итерируемыми объектами, цикл заканчивает свою работу, когда он доходит до последнего элемента итерируемого объекта
# while - это цикл, который работает до тех пор, пока условие верное (возвращает True)


# list1 = ['hello world', 1, 2, 3, True, None, [1, 2, 3]]

# for element in list1:
#     print(element)

# for letter in 'hello world':
#     print(letter)

# fkdjvlsd mk
n = 1
# while n <= 10:
#     print(n)
#     # n = n + 1 - инкремент
#     n += 1
# 1 2 3 4 5 6 7 8 9 10

#lkm
# n = 0
# while n:
#     print('hello')
    # не отработает потому что 0 - False

"==============================Ключевые слова в циклах============================"
# break - полностью останавливает цикл
# continue - пропускает одну итерацию, и переходит сразу к следующей

# for i in range(10):
#     if i == 3:
#         continue
#     print(i)
# 0 1 2 4 5 6 7 8 9

# for i in range(10):
#     print(i)
#     if i == 3:
#         continue
# 0 1 2 3 4 5 6 7 8 9


# for i in range(10):
#     print(i)
    # break
# 0

# for i in range(10):
#     print(i)
#     if i == 5:
#         break
# 0 1 2 3 4 5


list1 = [1, 2, 3, 1, 1, 3, 5, 1, 3]
# new_list = []

# for num in list1:
#     if num == 1:
#         continue
#     new_list.append(num)

# print(new_list)


# while 1 in list1:
#     list1.remove(1)
# print(list1)


#for i in range(10):
#    print(i, 'i')
#    for j in range(10):
#        print(j, 'j')

# Вывести числа от 1 до 10.(решить с помощью while и for) 
# for i in range(1, 11):
#     print(i)

# n = 1
# while n <= 10:
#     print(n)
#     n += 1

#  Вывести все четные числа от 1 до 20. (решить с помощью while и for) 
# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i)

# n = 1
# while n <= 20:
#     if n % 2 == 0:
#         print(n)
#     n += 1

# Найти числа кратные 3 и 5 в диапазоне (1, 100).(решить с помощью while и for)

# n = 1
# while n <= 100:
#     if n % 3 == 0 and n % 5 == 0:
#         print(n)
#     n += 1
# print(5 % 3)


# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i)


#  Напишите программу, которая выводит чётные числа из диапазона (1, 300) и останавливается, если встречает число 237.


# n = 1
# while n <= 237:
#     if n % 2 == 0:
#         print(n)
#     n += 1


for i in range(1, 301):
    if i % 2 == 0:
        print(i)
    if i == 237:
        break
    
print('hello world')

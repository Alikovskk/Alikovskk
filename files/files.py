'===================================Модули и пакеты========================='
# любой файл с расширением .py - модуль
# пакет - набор модулей (обязательно должен быть файл __init__.py)

"==========================Работа с файлами================================"
# open - функция, которая открывает файл в определенном режиме
"""
РЕЖИМЫ:

r - read (означает, что файл только для чтения)

w - write (только для записи, каждый раз файл очищается)

a - append (только для дозаписи, данные добавляются в конец)

x - создает файл, но если он существует то выйдет ошибка

b - binary (в бинарном виде)
"""

"==================================Read=================================="

file = open('test.txt', 'r')
# print(dir(file))
print(file.writable()) # False
print(file.readable()) # True
print(file.read())
print(file.read()) # ''  (потому что каретка находится)
file.seek(0) # перенос каретки в самое начало файла
print(file.read(5))

file.seek(0)
print(file.readline()) # hello world (метод считывает только 1 строку)
print(file.readline()) # ADA (считывает вторую строчку, потому что каретка смещена)

file.seek(0)
print(file.readlines()) # ['hello world\n', 'ADA\n', 'My name is Nikita\n'] (считывает все строки, и возвращает список из этих строк, добавляя в конец строки '\n' - перенос на новую строку)

file.close()
'======================================Write==================================='
file2 = open('new_file.txt', 'w')
# если файла нет - то создаст его автоматически

# file2.write('Hello world\n')
# file2.write('my name is nikita')
# если были данные, то они удаляются и записываются новые

file2.writelines(['hello\n', 'world\n']) 
# метод writelines принимает список из строк, указывайте \n если нужно перенести на новую строку

file2.close()
'==============================Append======================'
file3 = open('new_file.txt', 'a')
file3.write('New Line')
file3.seek(0)
file3.write('Bishkek') # все равно запишет в конец, даже если переместили каретку

file3.close()

'==============================Контекстный менеджер============================='

with open('new_file.txt', 'r') as file4:
    print(file4.write())
    file4.seek(0)


print(file4.closed) # True - файл закрыт
# closed - проверяет закрыт ли файл, и возвращает либо True, либо False

# конструкция with

# try:
#     file = open('new_file.txt', 'r')
#     file.write()
# finally:
#     file.close()
    
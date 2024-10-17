# "==============================Строки=================================="
# # строки - неизменяемый тип данных, который предназначен для хранения текста (любой последовательности символов), заключенного в одинарные или двойные кавычки


# string1 = 'hello'
# string2 = "world"
# # error_str = 'hello world" # таким образом создавать строки нельзя
# str3 = "don't"
# # print(str3)
# str4 = 'don\'t'
# # print(str4)
# str5 = " 'ada courses'" # внутри двойных кавычек все одинарные кавычки - это просто символы

# # print(str5) # 'ada courses'
# str6 = '"hello"'
# # print(str6) "hello"

# str_ = """
# многострочный текст в тройных кавычках, тут можно ставить "любые" 'кавычки'
# """

# str_ = '''
# многострочный текст в тройных кавычках, тут можно ставить "любые" 'кавычки'
# '''

# # Конкатенация - склеивание строк
# string = 'hello'
# string2 = 'world'
# print(string + ' ' + string2) # hello world
# string3 = 'hello' + ' ' + 'world'
# print(string3) # hello world

# string4 = 'ADA'
# string = 100
# print(string4 * 2)

# "===============================Экранизация строк========================"
# # '\n' - Перенос на новую строку
# print('hello\nworldljnlljhlln')
# # hello
# # worldljnlljhlln


# # '\t' - добавляет 4 пробела (1 таб)
# print('hello\tworldljnlljhlln') # hello   worldljnlljhlln

# # 'don't'
# '\''
# print('hello\'worldljnlljhlln')

# "=====================Форматирование строк=============================="
# # name_of_model = input('Введите название модели: ')
# price_iphone14 = 1000
# price_iphone15 = 1100
# price_iphone15_pro = 1250

# #1 способ - f-строки
# # string = f'Название модели: {name_of_model}\nЦена товара: {price_iphone15}'
# # print(string)
# # Название модели: iphone 15 pro
# # Цена товара: 1100

# # 2 способ
# format1 = 'название модели: {}\nЦена товара: {}'
# # print(format1.format(name_of_model, price_iphone14))
# # название модели: iphone 14
# # Цена товара: 1000

# format3 = 'название модели: %s\nЦена товара: %s'
# # print(format3 % (name_of_model, price_iphone14))

# '================================Методы строк================================='
# # методы - функции, которые относятся к определенному типу данных, к ним мы обращаемся через точку

# # dir() - функция которая выводит все методы, которые относятся к определенному типу данных
# # print(dir('hello'))

# # .lower() - метод которые переводит всю строку в нижний регистр

# string1 = 'HELLO WORLD'
# print(string1)
# print(string1.lower()) # hello world
# print('HEllO'.lower()) # hello

# # .upper() - метод которые переводит всю строку в верхний регистр
# string1 = 'hello'
# print(string1.upper()) # HELLO
# print('hello'.upper()) # HELLO

# # .swapcase() - метод которые переводит все символы в противоположный регистр
# string3 = 'HElLO' # HeLlOwOrLd21
# print(string3.swapcase()) # hello WORLD

# # .title() - метод который меняет первую букву строки на верхний регистр (делает ее заглавной)
# string1 = 'hello world my name is nikita'
# print(string1.title()) # Hello World My Name Is Nikita

# # .capitalize() - метод который делает первую букву, первого слова в строке заглавной
# string1 = 'hello world my name is nikita'
# print(string1.capitalize()) # Hello world my name is nikita

# # .count() - метод который считает количество опеределенных символов в строке
# string1 = 'hello world my name is nikita!'
# print(string1.count('!'))

# # .startswith() - проверяет, начинается ли исходная строка с введенной подстроки возвращает булевое значение (True/False)
# string_ = 'hello world my name is nikita!'
# print(string_.startswith('H')) #True

# .endswith() - проверяет, заканчивается ли исходная строка с введенной подстроки возвращает булевое значение (True/False)
# print(string_.endswith('nikita!'))

# .islower() - проверяет, является строка полностью в нижнем регистреБ возвращает булевое значение
# string_ = 'hello5'
# print(string_.islower()) # True

# .isupper() - проверяет, является строка полностью в верхнем регистре возвращает булевое значение
string_ = 'HELLO'
# print(string_.isupper())

# .isdigit() - проверяет состоит ли строка полностью из символов
str_ = 'hello'
# print(str_.isdigit())

# .isalpha() - проверяет состоит ли строка полностью из букв
# print(str_.isalpha()) # True

# .isalnum() - Проверяет состоит ли строка из символов и букв
# string = 'ljkm;'
# print(string.isalnum())

# .split() - разделяет строку по указанному разделителю, если его не указать, то разделит по пробелу, возвращает список
string = 'hello world this is ada courses'
# print(string.split('i'))

#.join() - принимает список из строк, и соединяет их в одну по указаному символу
# list_str = string.split()
# print(list_str)
# print('+'.join(list_str))

# .strip() - убирает пробелы справа и слева строки
str_ = '                kdjfmsl;sfkj                   9 '
# print(str_.strip())

#.lstrip() - убирает пробелы слева
# print(str_.lstrip())

# print(str_.rstrip())

# "==========================Индексы====================================="
# # индекс - порядковый номер элемента в последовательности (символа в строке) (индексация начинается с нуля)

# 'h e l l o   w o r l d'
# #0 1 2 3 4 5 6 7 8 9 10
# #              .. -2  -1
# string1 = 'ada courses kjsflkmdvjlvn sfbkjn sfb fldjnb slkjdb kjsdnfb kljsdfb s;kbf s;jf skjl fbdsbkjsf kjsbf skj b'
# print(len(string1))
# # фукнция len() нужна для того чтобы посчитать количество всех символов в строке

# print(string1[4])
# list_ = ['ada', 'courses', 'bishkek', '21.08']
# print(list_[0])

"================================Cрезы========================================"
# срез - подстрока строки

string = 'hello world this is ada courses'
print(string[0:11]) # hello world
print(string[12:]) # this is ada courses
print(string[:11]) # hello world
print(string[::-1]) # hlowrdti saacuss
# sesruoc ada si siht dlrow olleh


string2 = string.upper()
print(string)
print(string2)
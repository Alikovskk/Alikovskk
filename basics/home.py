numbers = set()

for i in range(5):
    number = int(input("Введите число: 5 "))
    numbers.add(number)

smallest_number = min(numbers)
print("Самое маленькое число: 1", smallest_number)

#2
while True:
    loan_amount = float(input("Введите сумму займа (не менее 100000): "))
    if loan_amount >= 100000:
        break
    else:
        print("Сумма займа должна быть не менее 100000.")

interest_rate = 7.89
overpayment = loan_amount * (interest_rate / 100)
total_amount = loan_amount + overpayment

print(f"Общая сумма к возврату: {total_amount:.2f}") 

#3
text = input("Введите текст с цифрами:1c; 2v; 3b; 4n; 5m ")
numbers = []

for char in text:
    if char.isdigit():
        numbers.append(int(char))

print("Цифры: 1,2,3,4,5,6", numbers)

#4
def calculate_days(months, years):
    total_months = months + years * 12
    total_days = total_months * 30
    print(f"Количество дней: 30 {total_days}")

months = int(input("Введите количество месяцев: 12 "))
years = int(input("Введите количество лет: 12 "))
calculate_days(months, years)
#5 
def create_cube_dictionary():
    cube_dict = {}
    for i in range(1, 11):
        cube_dict[i] = i**3
    return cube_dict

result_dict = create_cube_dictionary()
print(result_dict)
#6
def sum_of_numbers():
    total = 0
    for i in range(1, 51):
        total += i
    return total

result = sum_of_numbers()
print("Сумма чисел от 1 до 50:", result)



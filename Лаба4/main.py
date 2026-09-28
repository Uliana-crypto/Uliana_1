n = int(input("Введите число "))

original = n
different = True

temp1 = original
while temp1 > 0:
    digit1 = temp1 % 10
    temp1 = temp1 // 10

    temp2 = temp1
    while temp2 > 0:
        digit2 = temp2 % 10
        if digit1 == digit2:
            different = False
            break
        temp2 = temp2 // 10
    if not different:
        break
if different:
    print("Все цифры различны")
else:
    print("Есть повторяющиеся цифры")

def is_armstrong_number(num):
    digits = str(num)
    num_digits = len(digits)

    armstrong_sum = sum(int(digit) ** num_digits for digit in digits)

    return armstrong_sum == num

def find_armstrong_numbers(n):
    armstrong_number = []
    for num in range(1, n + 1):
        if is_armstrong_number(num):
            armstrong_number.append(num)
    return armstrong_number

n = int(input("Введите натуральное число N: "))
armstrong_numbers = find_armstrong_numbers(n)
print(f"Числа Армстронга, не превышающие {n}:")
print(armstrong_numbers)
print(f"Найдено чисел: {len(armstrong_numbers)}")

def can_obtain(a, b):
    str_a = str(a)
    str_b = str(b)

    i=0
    j=0
    while i < len(str_a) and j < len(str_b):
        if str_a[i] == str_b[j]:
            i += 1
        j += 1
    return i == len(str_a)
a = int(input("Введите натуральное число A: "))
b = int(input("Введите натуральное число B: "))
if can_obtain(a, b):
    print(f"Число {a} можно получить вычеркиванием цифр из числа {b}.")
else:
    print(f"Число {a} нельзя получить вычеркиванием цифр из числа {b}.")
import math

x = float(input("Введите х: "))
k = int(input("Введите натуральное k > 1" ))
eps = 10 ** (-k)

n = 1
term = x
result = 1.0

while abs(term) >= eps:
    result += term
    n += 1
    term *= x / n

print(f"Приближённое значение {result}")
print(f"Точное значение {math.exp(x)}")
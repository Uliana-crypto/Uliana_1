import random

def fill_keyboard(n: int) -> list:
    print("Введите  элементы массива: ")
    arr = []
    for _ in range(n):
        try:
            arr.append(int(input()))
        except ValueError:
            raise ValueError("Нужно ввести целое число")
    return arr

def fill_random(n: int) -> list:
    l = int(input("Введите нижнюю границу"))
    h = int(input("Введите верхнюю границу"))
    if h < l:
        raise ValueError("верхняя граница меньше нижней")
    arr = []
    for _ in range(n):
        arr.append(random.randint(l, h))
    return arr

def product_even(arr: list) -> int:
    p = 1
    for i in range(0, len(arr), 2):
        p *= arr[i]
    return p

def sum_between_zeros(arr: list) -> int:
    first = None
    last = None
    for i, x in enumerate(arr):
        if x == 0:
            if first is None:
                first = i
            last = i
    if first is None or first == last:
        return 0
    return sum(arr[first+1:last])

def transform1(arr: list) -> list:
    return sorted(arr, key=lambda x: x >= 0)

def product_before_min_abs(arr: list) -> int:
    min = 0
    for i in range(1, len(arr)):
        if(abs(arr[i]) < abs(arr[min])):
            min = i
    product = 1
    for i in range(min):
        product *= arr[i]
    return product

def count_various(arr: list) -> int:
    c = set()
    for i in range(len(arr)):
        c.add(arr[i])
    return len(c)

def transform2(arr: list) -> int:
    negatives = [arr[i] for i in range(len(arr)) if arr[i] < 0 ]
    zeros = [arr[i] for i in range(len(arr)) if arr[i] == 0 ]
    positives = [arr[i] for i in range(len(arr)) if arr[i] > 0 ]
    return negatives + zeros + positives


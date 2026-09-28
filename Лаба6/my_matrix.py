import random

def fill_keyboard(n: int) -> list:
    print(f"Введите элементы матрицы {n}x{n}: ")
    matrix = []
    while len(matrix) < n:
        try:
            row = list(map(int, input().split()))
            if len(row) == n:
                matrix.append(row)
            else:
                print(f"  Нужно ровно {n} чисел")
        except ValueError:
            raise ValueError("Элементы должны быть целыми")
    return matrix

def fill_random(n: int) -> list:
        l = int(input("Введите нижнюю границу "))
        h = int(input("Введите верхнюю границу "))
        if h < l:
            raise ValueError("верхняя граница меньше нижней")
        matrix = []
        for _ in range(n):
            row = []
            for _ in range(n):
                row.append(random.randint(l, h))
            matrix.append(row)
        return matrix

def max_in_columns_without_positives(matrix: list):
    n = len(matrix)
    result = None
    columns = []
    for j in range(n):
        has_pos = False
        for i in range(n):
            if matrix[i][j] > 0:
                has_pos = True
                break
        if not has_pos:
            columns.append(j)
            for i in range(n):
                if result is None or result < matrix[i][j]:
                    result = matrix[i][j]
    if not columns:
        print("Нет столбцов, не содержащих положительных элементов")
        return None

    print(f"Подходящие столбцы: {columns + 1}")
    return result

def count_negatives_lower_right_triangle(matrix: list) -> int:
    n = len(matrix)
    count = 0
    for i in range(n):
        for j in range(i, n):
            if matrix[i][j] < 0:
                count += 1
    return count

def first_row_without_negatives(matrix: list) -> int:
    n = len(matrix)
    for i in range(n):
        has_neg = False
        for j in range(n):
            if matrix[i][j] < 0:
                has_neg = True
                break
        if not has_neg:
            return i + 1
    return -1

def diagonal_sums(matrix: list) -> list:
    n = len(matrix)
    sums = []
    for d in range(1, n):
        s = 0
        for i in range(n - d):
            s += matrix[i][i+d]
        sums.append(s)
    for d in range(1, n):
        s = 0
        for i in range(n - d):
            s += matrix[i+d][i]
        sums.append(s)
    return sums
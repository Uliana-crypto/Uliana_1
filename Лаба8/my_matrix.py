import random

def fill_keyboard(n: int) -> list:
    print("Введите элементы матрицы {n}*{n}: ")
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
    try:
        l = int(input("Введите нижнюю границу "))
        h = int(input("Введите верхнюю границу "))
    except ValueError:
        raise ValueError("Границы должны быть целыми числами")
    if h < l:
        raise ValueError("верхняя граница меньше нижней")
    matrix = []
    for _ in range(n):
        row = []
        for _ in range(n):
            row.append(random.randint(l, h))
        matrix.append(row)
    return matrix

def sum_elem_col__least_one_zero(matrix: list) -> int:
    if not matrix:
        raise ValueError("Матрица пуста")
    rows = len(matrix)
    cols = len(matrix[0])
    col_sums = []
    for j in range(cols):
        has_zero = False
        total = 0
        for i in range(rows):
            if matrix[i][j] == 0:
                has_zero = True
            total += matrix[i][j]
        if has_zero:
            col_sums.append(total)
        else:
            col_sums.append(None)
    return col_sums

def sort_rows_by_parity_inplace(matrix: list) -> None:
    for idx, row in enumerate(matrix):
        if (idx + 1) % 2 == 0:
            row.sort()
        else:
            row.sort(reverse=True)

def fill_symmetric_keyboard(n: int) -> tuple:    
    count = n * (n + 1) // 2
    print(f"Введите {count} чисел (верхний треугольник, включая диагональ):")

    nums = []
    while len(nums) < count:
        for x in input().split():
            nums.append(int(x))

    matrix = []
    for _ in range(n):
        row = []
        for _ in range(n):
            row.append(0)
        matrix.append(row)

    k = 0
    for i in range(n):
        for j in range(i, n):
            matrix[i][j] = matrix[j][i] = nums[k]
            k += 1

    return matrix, nums

def find_max_symmetric(n: int, tri: list) -> tuple:
    expected = n * (n + 1) // 2
    if len(tri) != expected:
        raise ValueError(
            f"Ожидалось {expected} элементов, получено {len(tri)}"
    )
    max_val = None
    max_i = max_j = 0
    pos = 0
    for i in range(n):
        for j in range(i, n):
            val = tri[pos]
            if max_val is None or val > max_val:
                max_val = val
                max_i, max_j = i, j
            pos += 1
    return max_val, max_i, max_j
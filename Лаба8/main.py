import my_matrix

try:
    print("Введите размер матрицы ")
    n = int(input())

    if n < 1:
        raise ValueError("Число должно быть больше 1")

    print("Выберите способ заполнения:")
    print("1 - с клавиатуры")
    print("2 - случайными числами")

    choice = int(input())
    if choice == 1:
        matrix = my_matrix.fill_keyboard(n)
    elif choice == 2:
        matrix = my_matrix.fill_random(n)
    else:
        raise ValueError("Неверный выбор")

    print("Исходная матрица:")
    for row in matrix:
        print(row)

    result = my_matrix.sum_elem_col__least_one_zero(matrix)
    if all(x is None for x in result):
        print("Нет столбцов, содержащих ноль")
    else:
        print("Суммы столбцов с хотя бы одним нулём: ", result)

    my_matrix.sort_rows_by_parity_inplace(matrix)
    print("Матрица после сортировки строк по чётности:")
    for row in matrix:
        print(row)

    matrix, tri = my_matrix.fill_symmetric_keyboard(5)
    max_val, max_i, max_j = my_matrix.find_max_symmetric(5, tri)
    print(f"Максимум в верхнем треугольнике: {max_val} "
            f"(строка {max_i + 1}, столбец {max_j + 1})")
    for row in matrix:
        for x in row:
            print(x, end=" ")
        print()
        
except ValueError as e:
    print(f"{e}")
except Exception as e:
    print(f"{e}")
import my_matrix

try:
    print("Введите размер матрицы ")
    n = int(input())
    if n < 1:
        raise ValueError("число должно быть больше 1")

    print("Выберите способ заполнения:")
    print("1 - с клавиатуры")
    print("2 - случайными числами")

    choice = int(input())
    if choice == 1:
        matrix = my_matrix.fill_keyboard(n)
    elif choice == 2:
        matrix = my_matrix.fill_random(n)
    else:
        raise ValueError("Неверный выбор ")

    print("Исходная матрица:")
    for row in matrix:
        print(row)

    print("Суммы диагоналей, параллельных главной: ",
           my_matrix.diagonal_sums(matrix))

    row_num = my_matrix.first_row_without_negatives(matrix)
    if row_num == -1:
        print("Нет строк без отрицательных элементов")
    else:
        print("Номер первой строки без отрицательных элементов: ", row_num)

    print("Максимум в столбцах без положительных элементов: ",
          my_matrix.max_in_columns_without_positives(matrix))

    print("Количество отрицательных элементов в нижнем правом треугольнике: ",
          my_matrix.count_negatives_lower_right_triangle(matrix))

except ValueError as e:
    print(e)
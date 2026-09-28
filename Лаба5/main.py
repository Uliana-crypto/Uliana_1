import my_array

try:
    print("Введите размер массива ")

    n = int(input())
    if n < 1:
        raise ValueError("число должно быть больше 1")

    print("Выберите способ заполнения:")
    print("1 - с клавиатуры")
    print("2 - случайными числами")

    choice = int(input())
    if choice == 1:
            arr = my_array.fill_keyboard(n)
    elif choice == 2:
        arr = my_array.fill_random(n)
    else:
        raise ValueError("Неверный выбор ")

    print("Исходный массив: ", arr)
    print("Произведение элементов с четными индексами: ", my_array.product_even(arr))
    print("Сумма элементов между первым и последним нулем: ", my_array.sum_between_zeros(arr))
    print("Преобразованный массив: ", my_array.transform1(arr.copy()))

    print("Количество различных элементов ", my_array.count_various(arr))
    print("Произведение элементов до минимального по модулю ", my_array.product_before_min_abs(arr))
    print("Все отрицательные элементы, потом все нули и все положительные элементы ", my_array.transform2(arr))

except ValueError as e:
     print(e)
     
     
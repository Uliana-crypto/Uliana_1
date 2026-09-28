import my_string

try: 
    print("Введите строку:") 
    s = input()

    print("Результат(поменять местами самое длинное и самое короткое слово):")
    print(my_string.swap_words(s))

    print()

    print("Введите первую строку:") 
    s1 = input()
    print("Введите вторую строку:")
    s2 = input()
    print("Результат(объединить две строки):")
    print(*my_string.interleave_strings(s1, s2))

    print()

    print("Результат(Среди слов, состоящих только из цифр," \
    " найти слово, содержащее максимальное число нулей. " \
    "Если таких слов больше одного, найти предпоследнее из них):") 
    my_string.find_word_great_zeros(s)

    print() 

    print("Результат(на нечетном месте должно стоять слово только из цифр," \
    " а на четном – другое слово):")
    print(my_string.words_odd_even_positions(s))

except ValueError as e:
    print(e)
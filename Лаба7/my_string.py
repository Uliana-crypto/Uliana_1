import re

def swap_words(text: str)->str:
    tokens = re.findall(r'\S+|\s+', text)
    words = [(i, token) for i, token in enumerate(tokens) if not token.isspace()]
    if len(words) < 2:
        raise ValueError("Предложение должно состоять не менее чем два слова")
    max_words = max(len(w) for _, w in words)
    min_words = min(len(w) for _, w in words)

    first_max_idx = next(i for i, w in words if len(w) == max_words)
    last_min_idx = None
    for i, w in words:
        if len(w) == min_words:
            last_min_idx = i
    longest_word = tokens[first_max_idx]
    shortest_word = tokens[last_min_idx]

    tokens[first_max_idx] = shortest_word
    tokens[last_min_idx] = longest_word

    return ''.join(tokens)

def interleave_strings(s1: str, s2: str) -> str:
    word1 = s1.split()
    word2 = s2.split()

    result = []
    n = max(len(word1), len(word2))
    for i in range(n):
        if i < len(word1):
            result.append(word1[i])
        if i < len(word2):
            result.append(word2[i])

    return result

def find_word_great_zeros(s: str):
    words = s.split()
    max_zeros = 0
    result = None

    for word in words:
        if word.isdigit():
            zeros = word.count('0')
            if zeros > max_zeros:
                max_zeros = zeros
                result = [word]
            elif zeros == max_zeros:
                result.append(word)

    if result:
        if len(result) >= 2:
            print("Предпоследнее", result[-2])
        else:
            print("Первое", result[0])
    else:
        print("Слов из цифр нет")

def words_odd_even_positions(s: str)->str:
    words = re.findall(r'\w+', s)
    digits = []
    other = []
    for word in words:
        if word.isdigit():
            digits.append(word)
        else:
            other.append(word)

    result = []
    while digits and other:
        result.append(digits.pop(0))
        result.append(other.pop(0))

    while digits:
        result.append(digits.pop(0))

    while other:
        result.append(other.pop(0))

    return ' '.join(result)
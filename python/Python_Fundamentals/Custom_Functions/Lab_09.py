
def detect_vowels(sentence: str) -> list:
    from string import punctuation

    vowels = ['a', 'e', 'ı', 'i', 'o', 'ö', 'u', 'ü']
    caught_vowels = []

    for i in sentence:
        if i in vowels:
            if i not in caught_vowels:
                caught_vowels.append(i)
        elif i.isdigit() or i in punctuation:
            pass
    return caught_vowels


def detect_consonants(sentence: str) -> list:
    from string import punctuation
    vowels = ['a', 'e', 'ı', 'i', 'o', 'ö', 'u', 'ü']
    caught_consonants = []

    for i in sentence:
        if i not in vowels:
            if i not in caught_consonants:
                caught_consonants.append(i)
        elif i.isdigit() or i in punctuation:
            pass
    return caught_consonants


word = input('Please type any sentence: ')
result_1 = detect_consonants(word)
result_2 = detect_vowels(word)

print(f'Caught consonants: {result_1}')
print(f'Caught vowels: {result_2}')



digits = [9, 9, 9, 2, 4, 4, 4, 7, 5, 7, 1, 2, 3, 4, 3, 9, 5, 1, 1, 8, 4, 4, 2, 4, 3, 5, 6]


def counting_digit_frequency(lst: list) -> None:
    frequency_dct = {}

    for i in lst:
        if i in frequency_dct:
            frequency_dct[i] += 1
        else:
            frequency_dct[i] = 1

    for key, value in frequency_dct.items():
        print(f'{key}: {value}')


counting_digit_frequency(digits)


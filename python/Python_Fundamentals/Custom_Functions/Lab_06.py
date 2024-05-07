#

lst_1 = [9, 28, 23, 10, 11, 48, 99, 101, 102, 103]
lst_2 = []
lst_3 = []

def odd_or_even(a: int) -> str:
    if a % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

def appending_list(result: str, counter: int)-> None:
    if result == 'Even':
        lst_2.append(counter)
    else:
        lst_3.append(counter)

    print(f'Even numbers: {lst_2}')
    print(f'Odd numbers: {lst_3}')

for i in lst_1:
    result = odd_or_even(i)
    appending_list(result, i)






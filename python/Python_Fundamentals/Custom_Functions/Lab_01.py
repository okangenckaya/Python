
# How to detect whether number is even or odd ?

def even_or_odd(a: int):
    if a % 2 == 0:
        print(f'{a} is an even number. ')
    else:
        print(f'{a} is an odd number. ')

number = int(input('Please type a number: '))

even_or_odd(number)


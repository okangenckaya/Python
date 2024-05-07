
def find_biggest_number(a: float, b: float, c: float):
    if a > b and a > c:
        print(f'The biggest number is {a}')
    elif b > a and b > c:
        print(f'The biggest number is {b}')
    elif c > a and c > b:
        print(f'The biggest number is {c}')
    else:
        print('The numbers you have typed is equal...! ')

x = float(input('Please type the first number: '))
y = float(input('Please type the second number: '))
z = float(input('Please type the third number: '))

find_biggest_number(x, y, z)



from math import sqrt

def calculating_linear_root(a: int, b:int, c:int):
    delta = b ** 2 - 4 * a * c

    if delta > 0:
        x_1 = -b - sqrt(delta) / 2 * a
        x_2 = -b + sqrt(delta) / 2 * a
        print(f'There are 2 roots\nFirst root: {x_1}\nSecond root: {x_2}. ')
    elif delta == 0:
        x_1 = -b - sqrt(delta) / 2 * a
        print(f'There is only one root: Calculated value is {x_1}')
    else:
        print('There is no real root. ')

k = int(input('Please enter an integer: ' ))
l = int(input('Please enter an integer: ' ))
m = int(input('Please enter an integer: ' ))

calculating_linear_root(k, l , m)


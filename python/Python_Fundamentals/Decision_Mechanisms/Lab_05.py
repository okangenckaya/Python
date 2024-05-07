# How to find the smallest number in 3 numbers typed by user ?

x = float(input('Please type first number. '))
y = float(input('Please type second number. '))
z = float(input('Please type third number. '))

if x < y and x < z:
    print(f'the smallest number {x}')
elif y < x and y < z:
    print(f'the smallest number {y}')
elif z < x and z < y:
    print(f'the smallest number {z}')
else:
    print('all numbers are equal. ')





# how to find middle number between 3 numbers typed by user ?

x = float(input('Please type first number. '))
y = float(input('Please type second number. '))
z = float(input('Please type third number. '))

if x < y < z or z < y < x:
    print(f'ortanca sayı {y}')
elif y < x < z or z < x < y:
    print(f'ortanca sayı {x}')
elif x < z < y or y < z < x:
    print(f'ortanca sayı {z}')
else:
    print('sayılar eşit.')


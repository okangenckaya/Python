# How to find the biggest number in 3 numbers taken by user ?

x = float(input('Please type first number. '))
y = float(input('Please type second number. '))
z = float(input('Please type third number. '))

if x > y and x > z:
    print(f'The biggest number you typed is {x}. ')
elif y > z and y > x:
    print(f'The biggest number you typed is {y}. ')
elif z > x and z > y:
    print(f'The biggest number you typed is {z}. ')
else:
    print('Numbers you have typed could be equal. ')



# how to detect if the number is negative, positive, or neutral ?

number = float(input('Please enter a number. '))

if number > 0:
    print(f'{number} is a positive number. ')
elif number == 0:
    print(f'0 is a neutral number. ')
else:
    print(f'{number} is a negative number. ')


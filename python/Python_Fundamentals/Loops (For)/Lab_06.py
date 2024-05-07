
# How to determine a number is prime number or not (second way)?

number = int(input('Please enter an integer. '))

if number > 1:
    for i in range(2, int(number/2)+1):
        if number % i == 0:
            print(f'{number} is not a prime number.')
            break
    else:
        print(f'{number} is a prime number.')
else:
    print(f'{number} is not a prime number.')



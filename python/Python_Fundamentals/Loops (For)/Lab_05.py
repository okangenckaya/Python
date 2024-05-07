
# How to determine a number is prime number or not ?

number = int(input('Please enter an integer. '))

if number <= 0:
    print('Zero or negative numbers cannot be a prime number. Please enter a positive number. ')

else:
    is_prime = True

    if number == 1:
        is_prime = False

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print(f'{number} is prime. ')
else:
    print(f'{number} is not prime. ')


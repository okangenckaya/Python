
# Factorial Calculation:

def factorial_calculation(a: int):
    if a < 0:
        print('Factorial of numbers below zero cannot be calculated..! ')
    else:
        result = 1
        if a == 0 or a == 1:
            print(f'{a}! : {result}')
        else:
            for i in range(1, a + 1):
                result *= a
                a -= 1
            print(f'{number}! : {result}')

number  = int(input('Please enter a number: '))

factorial_calculation(number)




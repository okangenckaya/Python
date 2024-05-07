
while True:

    reminder_1 = 'A reminder: In order to manage the operation you wish, please type these symbols:'
    print(reminder_1)
    reminder_2 = 'For sum : +'
    print(reminder_2)
    reminder_3 = 'For subtraction : - '
    print(reminder_3)
    reminder_4 = 'For multiplying : * '
    print(reminder_4)
    reminder_5 = 'For dividing : / '
    print(reminder_5)

    operation = input('Please enter an operation you manage to: ')

    if operation == 'e':
        print('The application is closing..! ')
        break

    else:

        if operation == '+':
            a = float(input('Please enter the first number. '))
            b = float(input('Please enter the first number. '))

            total = a + b
            print(f'Result: {total}')

        elif operation == '-':
            a = float(input('Please enter the first number. '))
            b = float(input('Please enter the first number. '))

            difference = a - b
            print(f'Result: {difference}')

        elif operation == '*':
            a = float(input('Please enter the first number. '))
            b = float(input('Please enter the first number. '))

            multiplying = a - b
            print(f'Result: {multiplying}')

        elif operation == '/':
            try:
                dividend = float(input('Enter an integer. '))
                divider = float(input('Enter an integer. '))
                dividing = dividend / divider
                print(f'Result: {dividing}')

            except ZeroDivisionError as err:
                print('Zero cannot divide any number. ')

            finally:
                print('This application will work all the time despite the errors. ')
        else:
            print('Please enter a valid operation symbol. ')





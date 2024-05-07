
#How to print calculation based on operation ?
#How to stop the process when press 'e' key?

reminder = 'Please type these symbols to calculate : + , - , * , / '
warning =  "In order to stop process, please type 'e'."

print(reminder)
print(warning)

while True:
    operation = input('Please enter the type of operation you manage. ')
    if operation == 'e':
            print('Aplication is shutting down.')
            break
    else:
        number_1 = float(input('Please enter first number. '))
        number_2 = float(input('Please enter second number. '))

        if operation == '+':
            print(f'Result: {number_1 + number_2}')
        elif operation == '-':
            print(f'Result: {number_1 - number_2}')
        elif operation == '*':
            print(f'Result: {number_1 * number_2}')
        elif operation == '/':
            print(f'Result: {number_1 / number_2}')
        else:
            print('Girmiş olduğunuz işlem türü bulunmamaktadır.')







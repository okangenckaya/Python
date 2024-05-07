
# How to print how many odd or even numbers between 0 and 300?

x = 0
odd_numbers = 0
even_numbers = 0

while x <= 300:
    if x % 2 == 0:
        even_numbers += 1
    else:
        odd_numbers += 1
    x += 1

print(f'Even numbers: {even_numbers}\nOdd numbers: {odd_numbers}')


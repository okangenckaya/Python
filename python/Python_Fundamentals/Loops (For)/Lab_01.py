
# How to find even and odd numbers between 0 and 500 ?

even_numbers = 0
odd_numbers = 0

for i in range(1,500+1,1):
    if i % 2  == 0:
        even_numbers += 1
    else:
        odd_numbers += 1

print(f'Even numbers {even_numbers}\nOdd numbers {odd_numbers}')





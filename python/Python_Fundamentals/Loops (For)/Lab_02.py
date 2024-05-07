
# How to summ even and odd numbers between 0 and 1000?

sum_even_numbers = 0
sum_odd_numbers = 0

for i in range (0, 1000+1, 1):
    if i % 2 == 0:
        sum_even_numbers += i
    else:
        sum_odd_numbers += i

print(f'Sum Even numbers {sum_even_numbers}\nSumm Odd Numbers {sum_odd_numbers}')





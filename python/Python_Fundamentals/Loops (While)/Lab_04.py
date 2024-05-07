
#How to print summ odd and even numbers between 0 and 700?

x = 0
sum_even_numbers = 0
sum_odd_numbers = 0

while x <= 700:
    if x % 2 == 0:
        sum_even_numbers += x
    else:
        sum_odd_numbers += x
    x += 1
print(f'Sum even numbers {sum_even_numbers}\nsum odd numbers {sum_odd_numbers}')




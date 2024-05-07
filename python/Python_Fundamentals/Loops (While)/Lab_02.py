# How to print even numbers between 0 and 200?

x = 0
while x <= 200:
    if x % 2 == 0:
        print(x, end=',')
    x += 1


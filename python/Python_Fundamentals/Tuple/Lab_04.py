# Square of digits

numbers = []

#First way:

for i in range(10):
    numbers.append(i**2)
print(numbers)

#Second way:

print([i ** 2 for i in range(10)])


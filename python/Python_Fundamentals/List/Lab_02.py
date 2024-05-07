
# How to sum two lists with numbers created randomly (numbers between 0 and 100) ?
# How to print this sum to third list ?

from random import randint

list_1 = []
list_2 = []
list_3 = []

for i in range(10):
    list_1.insert(i, randint(0, 101))
    list_2.insert(i, randint(0, 101))
    list_3.insert(i, list_1[i] + list_2 [i])

print(list_1)
print(list_2)
print(list_3)


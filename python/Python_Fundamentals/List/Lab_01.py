
# Some built-in functions that enables to design list:

favorite_fruits = ['apple', 'orange', 'cherry', 'grapes', 'pineapple']

# how to add 'mango' to this list ?

favorite_fruits.append('mango')
print(favorite_fruits)

# How to insert 'peach' 3rd place to the list?

favorite_fruits.insert(2, 'peach')
print(favorite_fruits)

# How to collect 2 list ?

second_fruits = ['pear', 'blackberries', 'strawberries','watermelon']

favorite_fruits.extend(second_fruits)
print(favorite_fruits)

# How to remove 'apple' in this list ?

favorite_fruits.remove('apple')
print(favorite_fruits)

# How to remove the last unit of the list ?

favorite_fruits.pop()
print(favorite_fruits)


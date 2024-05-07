import pandas as pd
import numpy as np

numbers = [20, 30, 40, 50]
letters = ['a', 'b', 'c', 'd']
scaler = 5
dictionary = {
    'a': 10,
    'b': 20,
    'c': 30
}

#array enables us to sort any sequence regularly.
np_array = np.array(dictionary)
print(np_array)


#Data type that is used mostly is Series and DataFrame.

#How to turn into Series ?
print(pd.Series(numbers))
print(pd.Series(letters))

#While dictionary's keys converted into index, its value turned into column.
print(pd.Series(dictionary))


#Slicing for pandas sequence
print(pd.Series(dictionary)[:1])


#how to get index values?
print(pd.Series(dictionary).shape)

#Sequence's data type
print(pd.Series(dictionary).dtype)

#How many layers does sequence have?
print(pd.Series(dictionary).ndim)

#How to check sequence's count,mean so on?

print(pd.Series(dictionary).describe())

#Head returns us the first n rows. If there is no value, it returns 5 rows.
print(pd.Series(dictionary).head(1))

#Tail returns us the last n rows of a sequence.
print(pd.Series(dictionary).tail(1))

#True false boolen for pandas
print(pd.Series(dictionary) > 20)
print(pd.Series(dictionary) % 2 == 0)

#How to sum all sequence?
print(pd.Series(dictionary).sum())
print(type(pd.Series(dictionary).sum()))



first_index = pd.Series([90, 100, 85], ['midterm', 'final', 'homework'])
second_index = pd.Series([60, 90, 70], ['midterm', 'final', 'homework'])

print(first_index + second_index)




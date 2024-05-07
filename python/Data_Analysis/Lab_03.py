import pandas as pd
import numpy as np
from os import path

#how to find document path ?

print(path.abspath('imdb.csv'))

# how to read cvs format data?

df = pd.read_csv('data/imdb.csv', encoding='UTF-8')
print(df)

# how to read first 20 column of 'Movie_Title' in imdb.csv document?

# first way
print(df['Movie_Title'].head(20))

# second way
print(df[['Movie_Title']][0:20])

# third way
print(df.loc[:20, ['Movie_Title']])

# how to read index value between 20 and 50. columns of 'Movie_Title' and 'Rating' in imdb.csv  document?

print(df[['Movie_Title', 'Rating']][20:50])


# How to read Movie_Title and Rating information of the movies' rating column greater than equal to 7.0?
print(df[df['Rating'] >= 7.0][['Movie_Title', 'Rating']])

# How to read Movie_Title, Rating, and YR_Released of the movies' YR_Release information between 2014 and 2018 ?
print(df[(df['YR_Released'] >= 2014) & (df['YR_Released'] <= 2018)][['Movie_Title', 'Rating', 'YR_Released']])

#  How to read Movie_Title, Rating, and YR_Released of the movies' Num_Revies greater than 10000 or rating between 8 and 9?
print(df[(df['Num_Reviews'] >= 10000) | ((df['Rating'] >= 8) & (df['Rating'] <= 9))][['Movie_Title', 'Rating', 'YR_Released']])




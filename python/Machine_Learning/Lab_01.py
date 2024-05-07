import pandas as pd
import numpy as np
from math import sqrt

movies_df = pd.read_csv('data/movies.csv')
# print(movies_df.head())

rating_df = pd.read_csv('data/ratings.csv')
# print(rating_df.head())

# In case more than one data are in a row, we can seperate from each other. Here, we tried to seperate movie name and year data from each other by regex (regular expression).

movies_df['year'] = movies_df.title.str.extract(pat='(\W{2}\d{4}\W{1})', expand=False)

# expand function enables us to seperate datas from each other. When we give expand False, it returns series. Otherwise, it returns dataframe.
# while we are using extract, before extract function, we need to add column name and after column name, we need to 'str' expression.
# This expression is necessary and without it, the function can't work.
# pat: pattern

# how to get only digits?
movies_df['year'] = movies_df.year.str.extract(pat='(\d{4})', expand=False)


# How to add space inside title column for each string? (Pandas replace function)
movies_df['title'] = movies_df.title.replace(to_replace='(\W{2}\d{4}\W{1})', value=' ', regex=True)

# How to remove blanks from title datas?
movies_df['title'] = movies_df.title.apply(lambda x: x.strip())

# In order to use function inside dataframe, we have used apply function here.
# Apply always gets lambda parameter, which is anonymous function. Basically, we could use strip function through lambda here.
# Strip enables us to remove blanks inside datas in title column.


# Which film does have what type of genre?

movies_with_genre_df = movies_df.copy()

for index, column in movies_df.iterrows():
    for genre in column['genres']:
        movies_with_genre_df.at[index, genre] = 1
        # at in pandas is used to access a single value in Dataframe or Series if needed.
        # When 'at' matches for each index and genre, it returns 1. Otherwise, it returns none.

movies_with_genre_df = movies_with_genre_df.fillna(0)
print(movies_with_genre_df)

# Because we would like to manage arithmetical operation, we used fillna() function to replace nan with 0.
# We created this for loop in order to assign number for every letter according to genres.
# For instance, on the first row, Toy Story movie has Adventure genre and its all letters will get 1 value.

# To understand it better, there is print example here:
# print(movies_with_genre_df['A', 'd', 'v'])


# Imagine one new user signed up our system:

user_input = [
    {'title': 'Toy Story', 'rating': 4},
    {'title': 'Jumanji', 'rating': 5},
    {'title': 'Heat', 'rating': 5},
    {'title': 'Space Jam', 'rating': 4},
    {'title': 'Father of the Bride Part II', 'rating': 4},
]
input_movies_df = pd.DataFrame(user_input)

# We have new user data set as dataframe here. Which movies in our movie data set are corresponded to movies taken by new user's list ?

merged_input = movies_df.merge(input_movies_df, how='inner', on='title')

# Because data contains Heat film more than one, How to delete other Heat movies?
merged_input.drop(index=[4, 5], axis=0, inplace=True)

# How to delete genres and year columns?
merged_input.drop(labels=['genres', 'year'], axis=1, inplace=True)

# How to reset existed index in data set ?
input_movies = merged_input.reset_index(drop=True)
print(input_movies)

# How to detect movies' type through their rating ?
user_movies = movies_with_genre_df.merge(input_movies, how='inner', on='movieId')
print(user_movies)

# We need to delete some columns:
user_genre_df = user_movies.drop(labels=['movieId', 'title_x', 'title_y', 'rating', 'genres', 'year'], axis=1)


# Thus far, we attempted to determine the movies' type that new user evaluated.
# Therefore,in this step, we will receive 'user profile' we will multiply both new user's rating and movie types.

user_profile = user_genre_df.transpose().dot(input_movies_df['rating'])
print(user_profile)


# So as to implement Content Base system, we will create another matrix needed.
# We have created a data set with movie type and named as movies_with_genre_df above.
# We will transfer this data set into a new data set we need by manipulating.


# Step 1: We will set movieId column to relevant data set as index.
movie_matrix = movies_with_genre_df.set_index(movies_with_genre_df['movieId'])

# Step 2: We will remove the columns we don't need for now.
movie_matrix.drop(labels=['movieId', 'genres', 'year', 'title'], axis=1, inplace=True)
print(movie_matrix)

# We have just prepared movie_matrix and user profile. We can calculate weighted matrix now.
weighted_movie_matrix = (user_profile * movie_matrix).sum(axis=1)

recommendation_movie_matrix = weighted_movie_matrix / user_profile.sum()
recommendation_movie_matrix.sort_values(ascending=False, inplace=True)

# We have recommendation_movie_matrix now. Let's turn it into dataframe:

recommendation_df = pd.DataFrame(recommendation_movie_matrix)
print(recommendation_df)

#Let's manipulate dataframe:

recommendation_df.columns = ['Weight of Recommendation']
print(recommendation_df)

result = movies_df.merge(recommendation_df,
                         how='right',
                         left_on='movieId',
                         right_on='movieId')
print(result.head(10))


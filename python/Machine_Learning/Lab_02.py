import pandas as pd
import numpy as np
from math import sqrt

movies_df = pd.read_csv('data/movies.csv')
# print(movies_df.head())

rating_df = pd.read_csv('data/ratings.csv')
# print(rating_df.head())


movies_df['year'] = movies_df.title.str.extract(pat='(\W{2}\d{4}\W{1})', expand=False)

movies_df['year'] = movies_df.year.str.extract(pat='(\d{4})', expand=False)

movies_df['title'] = movies_df.title.replace(to_replace='(\W{2}\d{4}\W{1})', value=' ', regex=True)

movies_df['title'] = movies_df.title.apply(lambda x: x.strip())


# Which film does have what type of genre?

def pipe_separator(dataset) -> str:
    split_dataset = dataset.split('|')
    return ', '.join(split_dataset)


movies_df['GenresWithoutPipe'] = movies_df['genres'].apply(pipe_separator)

movies_with_genre_df = movies_df.copy()

for index, column in movies_df.iterrows():
    for genre in column['GenresWithoutPipe']:
        movies_with_genre_df.at[index, genre] = 1

movies_with_genre_df = movies_with_genre_df.fillna(0)
print(movies_with_genre_df)

# Movies watched by a new user:

user_input = [
    {'title': 'Toy Story', 'rating': 4},
    {'title': 'Jumanji', 'rating': 5},
    {'title': 'Heat', 'rating': 5},
    {'title': 'Space Jam', 'rating': 4},
    {'title': 'Father of the Bride Part II', 'rating': 4},
]
input_movies_df = pd.DataFrame(user_input)

merged_input = movies_df.merge(input_movies_df, how='inner', on='title')
merged_input.drop(index=[4, 5], axis=0, inplace=True)
merged_input.drop(labels=['genres', 'year'], axis=1, inplace=True)

input_movies = merged_input.reset_index(drop=True)
print(input_movies)

user_movies = movies_with_genre_df.merge(input_movies, how='inner', on='movieId')
print(user_movies)

user_genre_df = user_movies.drop(labels=['movieId', 'title_x', 'title_y', 'rating', 'genres', 'year', 'GenresWithoutPipe_x', 'GenresWithoutPipe_y'], axis=1)
print(user_genre_df)

user_profile = user_genre_df.transpose().dot(input_movies_df['rating'])
print(user_profile)


movie_matrix = movies_with_genre_df.set_index(movies_with_genre_df['movieId'])
print(movie_matrix)

weighted_movie_matrix = (user_profile * movie_matrix).sum(axis=1)
print(weighted_movie_matrix)


recommendation_movie_matrix = weighted_movie_matrix / user_profile.sum()
recommendation_movie_matrix.sort_values(ascending=False, inplace=True)

recommendation_df = pd.DataFrame(recommendation_movie_matrix)
print(recommendation_df)

result = movies_df.merge(recommendation_df,
                         how='right',
                         left_on='movieId',
                         right_on='movieId')
print(result.head(10))


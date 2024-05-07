
import pandas as pd

df = pd.read_csv('data/youtube-ing.csv')
print(df.head())

# How to print the most-viewed video?

print(df[df['views'] == df['views'].max()][['title']])

# How to print the top 10 most-viewed videos largest to smaller?

print(df.groupby('title').sum().sort_values(by='views', ascending=False).head(10)[['views']])

# How to find likes' mean according to category_id ?

print(df.groupby('category_id').mean(numeric_only=True).sort_values(by='likes', ascending=False)[['likes']].head(10))
# Because likes column includes some strange values, we only take numeric values' mean.


# Which channel does have how many comments ?

print(df.groupby('channel_title').sum().sort_values(by='comment_count', ascending=False)[['comment_count']].head(10))


# How to print tag numbers into new column named tag_count?
def tag_counter(tag):
    return len(tag.split('|'))
# on this csv document, because tags column includes pipe symbols, we created a function enables us to split all pipes.


def tag_splitter(tag) -> str:
    split_tag = tag.split('|')
    return ', '.join(split_tag)


df['tag_count'] = df['tags'].apply(tag_counter)
print(df[['title', 'tag_count']])

df['new_tag_column'] = df['tags'].apply(tag_splitter)
print(df[['new_tag_column']])


df['new_tag_column_2'] = df['tags'].apply(tag_splitter2)
print(df[['new_tag_column_2']])


# How to find average of like and dislike ?
# Let's print this result on a new column named 'like_avg'.

def average_like_and_dislike(dataset) -> list:
    like_list = list(dataset['likes'])
    dislike_list = list(dataset['dislikes'])

    combined_list = list(zip(like_list, dislike_list))
    # we are converting both lists index index.

    average_list = []

    for like, dislike in combined_list:
        if like + dislike == 0:
            average_list.append(0)
        else:
            average_list.append(like / like + dislike)

    return average_list


df['like_avg'] = average_like_and_dislike(df)

print(df.sort_values('like_avg', ascending=False)[['title', 'likes', 'dislikes', 'like_avg']])


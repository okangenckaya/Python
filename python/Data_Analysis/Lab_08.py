import pandas as pd
import numpy as np

df = pd.read_csv('data/auto.csv')
print(df)


#Reminder: Because there is no column title for our data set, we have added titles for the data set we read here.

df.columns = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style",
              "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight",
              "engine-type", "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio",
              "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price"]


# How to detect missing or wrong values ?

df.replace('?', np.nan, inplace=True)

missing_values_df = df.isnull()
print(missing_values_df)

for i in missing_values_df.columns.values.tolist():
    print(f'Column Name: {i}\n{missing_values_df[i].value_counts()}')

#Shortly here, we converted '?' values into True, and normal values into False.
#We counted '?' values and normal values.

#Handling missing values

#First Method: Changing missing values into average value

df['normalized-losses'].replace(np.nan, df['normalized-losses'].astype(float).mean(), inplace=True)
# We calculated mean values inside each columns and assigned them to nan values.

#Second Method: Changing missing values into frequency of sequence

df['num-of-doors'].replace(np.nan, df['num-of-doors'].value_counts().idxmax())
#We found the maximum values of each column and replaced them with null values.


#Data Standardization

df['city_L/KM'] = 235 / df['city-mpg']
df['highway_L/KM'] = 235 / df['highway-mpg']

#We turned mpg into KM here.


#Data Normalization

df['length'] = df['length'] / df['length'].max()
df['width'] = df['width'] / df['width'].max()
df['height'] = df['height'] / df['height'].max()

print(df[['length', 'width', 'height']])

#We turned values suchas length, width, height into values between 0 and 1.

#Dummy Variable

dummy_variable = pd.get_dummies(df['fuel-type'], dtype='float')
print(dummy_variable.head(20))

#we transfered dummy values into values between 0 and 1 through get_dummies() function. here string values has been turned into values between 0 and 1.


#How to type new datas onto new excel ?
df.to_csv('clean_auto.csv')


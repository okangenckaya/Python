import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# How to read .xlsx extension and its sheet ?
df_canada = pd.read_excel(io='data/canada.xlsx', sheet_name='Canada by Citizenship', skiprows=range(20), skipfooter=2, engine='openpyxl')
print(df_canada.head(20))


#How to delete Columns?

df_canada.drop(columns=['AREA', 'REG', 'Type', 'Coverage', 'DevName', 'DEV'],
               axis=1,
               inplace=True)

print(df_canada.shape)
# shape returns data sets' shape. In short, it returns how many columns and index there are.
# axis: typing 0 ----> row, typing 1----> column


# How to rename columns' name ?

# OdName => Country
# AreaName => Continent
# RegName => Region

df_canada.rename(columns={'OdName': 'Country',
                          'AreaName': 'Continent',
                          'RegName': 'Region'},
                 inplace=True)

print(df_canada.head())

# How to print type of columns' title?

for column in df_canada.columns:
    print(type(column))


# How to convert int values into str ?

df_canada.columns = list(map(str, df_canada.columns))
for column in df_canada.columns:
    print(type(column))


# How to make Country column into index ?

df_canada.set_index(keys='Country', inplace=True)
print(df_canada)
#We've replaced index values with country here.


# Let's try to sum immigrant numbers according to years?

df_canada['total'] = df_canada.sum(axis=1, numeric_only=True)
print(df_canada['total'])
#in pandas' sum function, numeric_only argument enables us to sum only numeric expressions.


# I created a list independent of data set and including string expressions based on years between 1980 and 2014.
years = list(map(str, range(1980, 2014)))
print(years)


# Let's find top 5 countries which emigrate most?

#First way
df_top_five_country = df_canada.total.sort_values(ascending=False)
print(df_top_five_country)

#Second way
df_canada.sort_values(by='total', axis=0, inplace=True, ascending=False)
df_top_five_country = df_canada.head()
print(df_top_five_country)

# How to transfer Country column into index by using df_top_five_country argument and years list?

df_top_five_country = df_top_five_country[years].transpose()
print(df_top_five_country.head())

# # How to visualise this data set as area plot?

df_top_five_country.plot(
    kind='area',
    stacked=False,
    figsize=(5, 4),
    alpha=0.5
)
#Because we are trying to create area plot here, kind has to be 'area'. if stacked bar is necessary, it could be true. if not, false. figsize enables us to detect the size of graph.
#alpha is tranparency shortly.


plt.title(label='Immigrant Trend of Top 5 Countries', color='blue')
# We have detected a title for our graph. In addition, we can type color type by abridging such as 'r', 'g' so on.

plt.ylabel('Number of Immigrant', color='r')
plt.xlabel('Years', color='r')

# We have just indicated what x and y labels will be.

plt.show()


# How to show immigrant mobility on histogram graph for 2013 ?

count, bin_edges = np.histogram(df_canada['2013'])
print(count)
print(bin_edges)
#We calculated frequency rates by numpy histogram function. Here, Bin edges is the number of observation for each range of the numeric feature's values.

df_canada['2013'].plot(
    kind='hist',
    stacked=False,
    figsize=(7, 4),
    xticks=bin_edges,
    #We located frequency rates that will be participated in x label through xticks.
    color='blue'
)

plt.title(label='Trend of immigrant mobility from 195 Countries in 2013')
plt.ylabel('Number of country')
plt.xlabel('Immigrant mobility')
plt.grid(True)
#grid prints lines back side of histogram graph.
plt.show()


# Let's print baltic states' immigrant rates.

df_baltic_countries = df_canada.loc[['Denmark', 'Norway', 'Sweden'], years].transpose()
print(df_baltic_countries)
# Through loc, we selected countries. While countries will be index, years will be column.

count, bin_edges = np.histogram(df_baltic_countries, bins=10)
# bins parameter will find 10 frequency.

print(count)
print(bin_edges)

df_baltic_countries.plot(
    kind='hist',
    stacked=False,
    figsize=(8, 5),
    xticks=bin_edges,
    color=['green', 'darkblue', 'red']
)

plt.title(label='Trend of immigrant mobility of Balic States')
plt.ylabel('Distribution by years')
plt.xlabel('Immigrant mobility')
plt.grid(True)
plt.show()

# According to concinents, immigrant distribution by pie chart.

df_continents = df_canada.groupby('Continent').sum(numeric_only=True)
print(df_continents)
#Owing to frequency of Continent, groupby is needed to use here. For instance; China, Pakistan, India are asia countries.

df_continents['total'].plot(
    kind='pie',
    figsize=(10, 7),
    startangle=90,
    #startangle enables us to Rotate pie of every slice. We arranged it as 90 degree here.
    autopct='"%.1f"',
    #autopct enables us to show
    labels=None,
    shadow=True,
    pctdistance=1.11,
    # pctdistance is the ratio between the center of each pie slice and start of the text.
    explode=[0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
)

plt.axis('equal')
plt.legend(labels=df_continents.index,
           loc='upper left',
           #we showed distribution label for each country on upper left side.
           prop={
               'size': 8
           })
# legend function enables us to show graph elements we named.
plt.show()


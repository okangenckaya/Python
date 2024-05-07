import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import r2_score

df = pd.read_csv('Employee_Salaries.csv')

# Detecting empty values:
missing_values_df = df.isnull()

for i in missing_values_df.columns.values.tolist():
    print(f'Column Name: {i}\n{missing_values_df[i].value_counts()}')


print(df[['Division', 'Base_Salary', 'Grade']].sort_values(by='Base_Salary', ascending=False).head(25))
# Display the top 25 records sorted by Base_Salary in descending order.
# Empty grade areas can be filled randomly with EX1, EX2, or EX3 grades, as these are the highest positions for every person according to their salaries.
# This will address any NaN values identified by the following code.


def remove_nan(value):
    titles = ['EX1', 'EX2', 'EX3']
    if pd.isnull(value):
        return random.choice(titles)
    else:
        return value


df_cleaned = df.apply(lambda x: x.map(remove_nan))
# Apply the remove_nan function to each element of the DataFrame.
# This ensures that there are no NaN values remaining in the DataFrame.

new_missing_values_df = df_cleaned.isnull()

# Iterate over each column in the DataFrame to count NaN values.
# Print the column name and the count of NaN values for each column.

for i in new_missing_values_df.columns.values.tolist():
    print(f'Column Name: {i}\n{new_missing_values_df[i].value_counts()}')
# This process ensures that there are no remaining NaN values in the DataFrame.


df_cleaned.groupby(by='Department')['Base_Salary'].sum().sort_values(ascending=False)
# Summ salaries according to Departments


grouped = df.groupby(by='Department_Name')
for i in grouped.groups.keys():
    print(i)
# First Way: Print the list of department

df_cleaned['Department_Name'].unique()
# Second Way: Print the list of department (Type: list)

df_cleaned['Department_Name'].value_counts()
# Detect how many employees work in a department.

df_cleaned['Department_Name'].nunique()
# Detect the number of departments

df_cleaned['Division'].value_counts()
# How many employees do work in divisions?

df_cleaned.groupby(by='Department_Name')['Division'].value_counts()
# Detect division numbers according to departments

df_cleaned['Division'].nunique()
# Number of divisions

df_cleaned['Base_Salary'].describe()

average_base_salary_of_top_5_departments = df_cleaned.groupby(by='Department_Name')['Base_Salary'].mean().sort_values(ascending=False).head()
# Calculate average of Base_Salary according to Department_Name

df_cleaned.groupby(['Department_Name', 'Division'])['Base_Salary'].mean().sort_values(ascending=False)
# Calculate average of Base_Salary according to Division for each department

df_cleaned.groupby(['Department_Name', 'Gender'])['Gender'].count()
# Calculate the number of gender according to departments

df_cleaned.groupby(['Department_Name', 'Grade'])['Base_Salary'].sum().sort_values(ascending=False)
# Calculate the base_salary according to grades.

df_top_five_most_paid_grade = df_cleaned.set_index('Grade')
print(df_top_five_most_paid_grade[['Base_Salary', 'Department_Name']]
      .sort_values(by='Base_Salary', ascending=False).head())
# Calculate the top 5 highest-paid positions based on base salary


# Many calculations are made according to specific factors.

df_cleaned.groupby('Gender')['Base_Salary'].sum()

df_cleaned.groupby(['Department_Name', 'Gender'])['Base_Salary'].sum()

# Visualization

average_base_salary_of_top_5_departments.plot(
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

)

plt.axis('equal')
plt.legend(labels=average_base_salary_of_top_5_departments.index,
           loc='upper left',
           #we showed distribution label for each country on upper left side.
           prop={
               'size': 8
           })
# legend function enables us to show graph elements we named.
plt.show()















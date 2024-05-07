import pandas as pd

users = {
    'employee': ['Okan', 'Bukan', 'Sukan', 'Kukan', 'Nukan'],
    'occupation': ['Auditor', 'System Specialist', 'Construction Technician', 'Construction Technician', 'Volleyball Player'],
    'neighborhood': ['Sarıyer', 'Besiktas', 'Nisantasi', 'Kadikoy', 'Umraniye'],
    'income': [16000, 16000, 15000, 14000, 20000],
    'age': [24, 27, 35, 29, 20]
}

df = pd.DataFrame(users)
print(df)

# How to classify the data set according to occupation?

print(df.groupby('occupation').groups)

# Which person does live in which neighborhood?
for name, group in df.groupby('neighborhood'):
    print(name)
    print(group)

# How many employees are in which neighborhood?

result_employees = df.groupby('neighborhood')['employee'].count()
df_group_neighbor = pd.DataFrame(result_employees)
print(df_group_neighbor)

# How to sum all salaries according to occupations?

result_salaries = df.groupby('occupation')['income'].sum()
df_sum_employees = pd.DataFrame(result_salaries)
print(df_sum_employees)

# how to find age average according to occupations?

result_2 = df.groupby('occupation')['age'].mean()
df_group_mean = pd.DataFrame(result_2)
print(df_group_mean)





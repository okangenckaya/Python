
import pandas as pd

df = pd.read_csv('data/nba.csv')
print(df)

#which player does earn the highest salary?

print(df[df['Salary'] == df['Salary'].max()][['Name', 'Salary']])

#How to detect the players' age between 20 and 35 and print their name, age, team information. Sort age values largest to smaller.

print(df[(df['Age'] >= 20) & (df['Age'] <= 35)][['Name', 'Age', 'Team']].sort_values(by='Age', ascending=False))
#If ascending is False, it prints the values largest to smaller. On the other hand, if ascending is true, it prints the values smaller to largest.


#Which team are James young in ?

print(df[df['Name'] == 'James Young'][['Name', 'Team']])

# Mean of teams according to Salary.

print(df.groupby('Team')['Salary'].mean())


#How to print teams and team number?

print(df['Team'].unique())
print(df['Team'].nunique())


#Function that enables us to print list of players' name including 'and'.

def finding_str(name: str) -> bool:
    if 'and' in name:
        return True
    else:
        return False


print(df[df['Name'].apply(finding_str)])


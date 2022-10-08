import pandas as pd


# Read the data
df = pd.read_csv('log.csv')
type(df)
crime = df.iloc[::40]
print(df['description'])
find most common description
print(df['description'].value_counts())

#find most common description for each location
print(df.groupby('location')['description'].value_counts())
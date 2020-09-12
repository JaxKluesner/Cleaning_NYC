import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt

# df = pd.read_csv(r'C:\Users\Suno\Downloads\Sales_Tax_Rates.csv')
# print(df)
df = pd.read_csv(r'C:\Users\Suno\Documents\property_data.csv')

# Standard
# print(df['ST_NUM'])
# print(df['ST_NUM'].isnull())

# Non-Standard
# print(df['NUM_BEDROOMS'])
# print(df['NUM_BEDROOMS'].isnull())
missing_values = ["na", "n/a", "--"]
df = pd.read_csv(r'C:\Users\Suno\Documents\property_data.csv', na_values=missing_values)
# print(df['NUM_BEDROOMS'])
# print(df['NUM_BEDROOMS'].isnull())

# Unexpected type differences
# Printing the isnull() for OWN_OCCUPIED misses the 12.
count = 0
for row in df['OWN_OCCUPIED']:
    try:
        int(row)
        df.loc[count, 'OWN_OCCUPIED']= np.nan
    except ValueError:
        pass
    count += 1
#print(df['OWN_OCCUPIED'])
#print(df['OWN_OCCUPIED'].isnull())

# Some basic data summarizing
print(df.isnull().sum())

print(df.isnull().values.any())

print(df.isnull().sum().sum())

# To replace values we can try these.

# df['ST_NUM'].fillna(125, inplace=true)

# df.loc(2, 'ST_NUM') = 125

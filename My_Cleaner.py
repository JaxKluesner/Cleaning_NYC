import numpy as np
import pandas as pd
from datetime import datetime

# df = pd.read_csv(r'C:\Users\Suno\Downloads\1_county_level_confirmed_cases.csv')
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# alabama_data = df[df['state'] == "Alabama"]
# alabama_data_descending = alabama_data.sort_values(by='confirmed_per_100000', ascending=False)
# Only uncomment next line if you want to reset index after sort.
# alabama_data_descending = alabama_data_descending.reset_index(drop=True)
# print(alabama_data_descending)

# Various things setting up basic dataframe.
df = pd.read_csv(r'C:\Users\Suno\Downloads\URBAN_PARK_RANGER_ANIMAL_CONDITION_RESPONSE.csv')
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
# df['Response Time'] = df['Date and Time of initial call'] - df['Date and time of Ranger response']
# print(df['Response Time'])
# df['Start Time'] = datetime.timestamp(df['Date and Time of initial call'])
ACC_intake_only = df[df['ACC Intake Number'].isnull() == False]
ACC_intake_only = ACC_intake_only.reset_index(drop=True)
print(len(ACC_intake_only.index))
print(len(df.index))

# Data frame for specifically location information.
location_df = df[["Borough", "Property"]]
print(location_df)
unique_loc = location_df['Borough'].unique()
print(unique_loc)
unique_loc_num = location_df.groupby(['Borough']).count()
print(unique_loc_num)

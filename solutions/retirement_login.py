import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np
# By Christopher Boon

# In this dataset, some people are hired and others retire. 
# There is no log letting you know that someone has retired.
# However, retired people should never log in again.

# Creates full path for dataset_name.csv
headers = ['date','time','user','status']
path = os.path.join(os.getcwd(),'logins.txt')
df = pd.read_csv(path , sep='\t', names=headers)
# print(df.head())
# Strategy:
    # notice people who have had a gap in logins
    # sort by date
    # Fore every person, and for each IN record. Calculate days between last IN
df['date'] = pd.to_datetime(df['date'])
# print(df['date'].min())
# print(df['date'].max())

# Function to calculate days since last 'IN' for each user
def days_since_last_in(group):
    group['days_since_last_in'] = group['date'].diff().dt.days
    group['days_since_last_in'] = group['days_since_last_in'].where(group['status'] == 'IN')
    return group

# Apply the function within each user group
df = df.sort_values(by=['user', 'date'])
# print('sorted values')
# print(df.head(3))
# print('')
df = df.groupby('user').apply(days_since_last_in)

df_in = df.loc[df['status']=='IN']
# df['date_diff_from_last_date_in_dataset'] =  df['days_since_last_in'].apply(lambda x : max_dt - x)
# df['date_diff_from_last_date_in_dataset'] =  ( df['date'].max() - df['days_since_last_in']) / np.timedelta64(1,'D')
# print(df_in.groupby(['days_since_last_in','date_diff_from_last_date_in_dataset']).count())
print(df_in[df_in['days_since_last_in'] >= 18])

# NEW FILTER: Check if the person has never logged in again
# get date difference with their max personal logout date

# max logout date


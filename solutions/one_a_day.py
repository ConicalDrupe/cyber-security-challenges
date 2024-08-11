import pandas as pd
import matplotlib.pyplot as plt
import os
headers = ['date','time','user','status']
path = os.path.join(os.getcwd(),'logins.txt')
df = pd.read_csv(path , sep='\t', names=headers)

df['date'] = pd.to_datetime(df['date']).dt.date
df['datetime'] = pd.to_datetime(df['date'].astype(str) + ' ' + df['time'].astype(str))
df['hour_of_the_day'] = pd.to_datetime(df['datetime']).dt.hour

print(df.head())
## Count number of logins, per day, by user
    # filter of those that logged in twice in a day
logon = df[df['status']=='IN']
logins_per_day = logon.groupby(['user','date'],as_index=False)['status'].count()

# Print list of those who logged in twice in a day (could be true for multiple days)
print(logins_per_day[logins_per_day['status'] > 1]['user'].unique())



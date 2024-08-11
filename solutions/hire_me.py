import pandas as pd
import datetime
import matplotlib.pyplot as plt
import os
headers = ['date','time','user','status']
path = os.path.join(os.getcwd(),'logins.txt')
df = pd.read_csv(path , sep='\t', names=headers)

df['date'] = pd.to_datetime(df['date']).dt.date
df['datetime'] = pd.to_datetime(df['date'].astype(str) + ' ' + df['time'].astype(str))
df['hour_of_the_day'] = pd.to_datetime(df['datetime']).dt.hour
print(df.head())
print(df.shape)

print('min date: ', df['date'].min())
print('max date: ',df['date'].max())

# count the number of first logins
# get the minimum date of Status=IN for each user
    # can be filtered within a daterange

first_login_date = df[df['status']=='IN'].groupby(['user'],as_index=False)['date'].min()
# print(first_login_date.head())
result=first_login_date['user'].nunique()
print(result)


# new count the number of new logins from 2022-01-01 to 2022-03-23

last_year_first_logins = first_login_date[(first_login_date['date']>=datetime.date(2022,1,1)) & (first_login_date['date']<=datetime.date(2022,3,23))]
print(last_year_first_logins.head())


# current employees 
#

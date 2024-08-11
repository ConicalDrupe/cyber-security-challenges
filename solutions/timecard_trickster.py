import matplotlib.pyplot as plt
import pandas as pd
import os
# By Christopher Boon

# Creates full path for dataset_name.csv
headers = ['date','time','user','status']
path = os.path.join(os.getcwd(),'logins.txt')
df = pd.read_csv(path , sep='\t', names=headers)
df['date'] = pd.to_datetime(df['date'])

# Create datetime column, with date and time concatenated
df['datetime'] = pd.to_datetime(df['date'].astype(str) + ' ' + df['time'].astype(str))
# Pull out hour of the day in 24 hour format
df['hour_of_the_day'] = pd.to_datetime(df['datetime']).dt.hour
print(df.head())

# Filter to July
df = df[df['date'].dt.month == 7]

# Convert 'time' column to datetime
df['time'] = pd.to_datetime(df['time'], format='%H:%M:%S')

# Combine 'date' and 'time' columns
# df['datetime'] = pd.to_datetime(df['date'].astype(str) + ' ' + df['time'].astype(str))

print(df.groupby('user')['time'].head())
df_mean = df.groupby('user')['time'].mean().reset_index()
df_mode = df.groupby('user')['time'].mode().reset_index()
print(df_mean.head())
print('')
print(df_mode.head())

# plt.figure(0)
# plt.scatter(df_mean


# Plot scatter plot
# plt.figure(figsize=(10, 6))
# colors = {'IN': 'blue', 'OUT': 'red'}
# plt.scatter(df['datetime'], df['user'], c=df['status'].map(colors), s=100)
# plt.xlabel('Datetime')
# plt.ylabel('User')
# plt.title('Scatter Plot of User Activity')
# plt.legend(['IN', 'OUT'])
# plt.show()

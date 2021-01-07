import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.options.display.max_rows = 299
pd.options.display.max_columns = 99
# sns.set_theme(color_codes=True)
sns.set(style="white", palette="muted", color_codes=True)

df = pd.read_csv('dohromady_2ses.csv', sep=';')
df2 = df[df['DoW'].isin(['1.5', '2.5', '3.5', '4.5', '5.5'])]
df3 = df[df['DoW'].isin(['1', '2', '3', '4', '5'])]

print(df2.head(15))

sns.displot(data=df2, x="prcnt")
sns.displot(data=df3, x="prcnt")
plt.show()

"""
weekly_limits = df.groupby(['Y', 'W']).agg({'BOTH_H': 'max', 'BOTH_L': 'min'}).reset_index()
weely_limits.to_csv('weekly_2ses.csv')

df_with_weekly_limits = pd.merge(df, weekly_limits, on=['Y', 'W'])
df_with_weekly_limits.to_csv('dohromady_2ses.csv')
"""

# df = df.drop_duplicates('Strategy')
# df2 = pd.read_csv('tos_day_rth_settlement_adjusted.csv', sep=';')
# df3 = pd.merge(df1, df2, left_on='Date', right_on='Date', how='left')

# df2 = df.groupby(['Year', 'Week_Number']).head(3).reset_index(drop=True)
# df3 = df.loc[df['DoW'] == 5]

# df3.to_csv('es_data_test_ZZZ.csv')
# print(df.head(20))

"""
df['24_RNG'] = df['24_H'] - df['24_L']
df['p24_RNG'] = df['24_RNG'].shift(+1)
print(df.head(10))
print(df.describe())

x = sns.lmplot(data=df, x='p24_RNG', y='RTH_RNG', col='DoW', hue="OOR", height=5)
plt.show()
"""
"""
df['DATUM'] = pd.to_datetime(df['DATUM'])
df['Week_Day'] = df['DATUM'].dt.dayofweek
df['Week_Number'] = df['DATUM'].dt.isocalendar().week
df['Month_Number'] = df['DATUM'].dt.month
df['Year'] = df['DATUM'].dt.isocalendar().year

df2 = df.groupby(['Year', 'Month_Number']).tail(10).reset_index(drop=True)
# df2 = df.groupby(['Year', 'Month_Number']).agg({'24_H': 'max', '24_L': 'min'})
df2.to_csv('M_vs_last_10.csv')

df3 = df.groupby(['Year', 'Month_Number']).agg({'RTH_O': 'first', 'RTH_H': 'max', 'RTH_L': 'min', 'RTH_C': 'last'})
df3.to_csv('RTH_Monthly_OHLC.csv')

df4 = df.groupby(['Year', 'Week_Number', 'Week_Day']).agg({'RTH_O': 'first', 'RTH_H': 'max', 'RTH_L': 'min', 'RTH_C': 'last'})
df4.to_csv('RTH_PoUtSt_OHLC.csv')
"""
"""
es_data = pd.read_csv('es_data_final.csv', sep=';')
es_data2 = pd.read_csv('es_data_test2.csv', sep=';')
# check NULL columns null_columns = es_data.isnull().sum()

es_data2 = es_data[['MNTH', 'RTH_RNG']]
grouped = es_data2.groupby(['MNTH']).mean()
grouped = grouped.reset_index()
print(grouped.head(100))

print(es_data2.head())

x = sns.lmplot(data=es_data2, x='ON_RNG', y='p24_RTH', col='DoW', hue="OOR", height=5)
plt.show()
"""

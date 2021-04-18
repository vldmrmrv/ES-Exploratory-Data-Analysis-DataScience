import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

pd.options.display.max_rows = 299
pd.options.display.max_columns = 99

df = pd.read_csv('plot_cme_1997-2021_24H_futures.csv', sep=';')

df['CMLTV'] = df.groupby(['Y'])['WW'].cumsum()
df['P3'] = df['P2'].cumsum()
df = df[df['Y_CUM'].isin(range(0, 120))]

df[['24_H', 'p_HL']].plot(subplots=True, figsize=(12, 6))
plt.locator_params(axis="x", nbins=20)
plt.show()

# Generate a custom diverging colormap
cmap = sns.diverging_palette(10, 133, as_cmap=True)
df = df.pivot("TDoM", "M", "p_HL")
sns.heatmap(df, annot=True, cmap="YlGnBu", fmt='.3g')
# sns.heatmap(df, mask=df > 0.8, cbar=False)
plt.suptitle("heatmap_p_abs_HighLow")
plt.show()

df2 = df.groupby(['DATE', 'SESS']).agg({'O': 'first', 'H': 'max', 'L': 'min', 'C': 'last',
                                        'D_O': 'first', 'D_H': 'max', 'D_L': 'min', 'D_C': 'last'})
df2 = df.groupby(['M', 'TDoM']).agg({'p_absGAP': 'mean'})
df2.to_csv('big_heat_gaps2.csv')


df['signal'] = [1 if s >= 1 else 0 for s in df['Pabs']]

markers = [mr for mr, close in enumerate(df['H']) if df['signal'][mr] == 1]
plt.suptitle(">1% moves & 1 2 5 10 % lines from ATH")
plt.plot(df['ATH_H_1P'])
plt.plot(df['ATH_H_2P'])
plt.plot(df['ATH_H_5P'])
plt.plot(df['ATH_H_10P'])
plt.plot(df['H'], marker='X', markerfacecolor='r', markevery=markers)
plt.show()


df['ATH_H'] = df['H'].cummax()
df['ATH'] = [1 if rng == prng else 0 for rng, prng in zip(df['H'], df['ATH_H'])]
df['PfATH'] = round(100 - (df['O'] * 100 / df['ATH_H']), 2)
df['prcRNG'] = round((df['RNG'] * 100 / df['ATH_H']), 2)

df2 = df.groupby(['M', 'DoM']).agg({'RNG': 'mean'})
df2.to_csv('big_heatRNG.csv')

sns.set_theme(style="whitegrid")
plt.plot(df['P3'], label="1962-2020")
plt.plot(df2['P3'], label="2000-2020")
plt.locator_params(axis="x", nbins=55)
plt.legend()
plt.show()

df = df.pivot("DoM", "M", "RNG")
sns.heatmap(df, annot=True, cmap="YlGnBu")
# sns.heatmap(df, mask=df > 0.8, cbar=False)
plt.show()

sns.set_theme(style="whitegrid")
sns.barplot(x="DoW", y="W_HoL", data=df, ci=None, palette="crest")
plt.show()

sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(3, 1)
sns.barplot(ax=axes[0], x="TIME", y="HorLW", data=df1, ci=None, palette="crest")
sns.barplot(ax=axes[1], x="TIME", y="HorLW", data=df2, ci=None, palette="crest")
sns.barplot(ax=axes[2], x="TIME", y="HorLW", data=df3, ci=None, palette="crest")
plt.xticks(rotation=70)
plt.tight_layout()
plt.show()

df['CNT'] = [1 if rng == 'E' or rng == 'I' else 0 for rng in df['Type']]
df['CUMSUM'] = df['CNT'].cumsum()


plt.suptitle("Study 2")
plt.plot(df['CUMSUM'])
plt.show()

df[['Close', 'PDOI']].plot(subplots=True, figsize=(12, 6))
plt.show()


def func(row):
    if row['DoW'] == 1 and row['2DoW'] == 1.5:
        return 'A'
    elif row['DoW'] == 1 and row['2DoW'] == 2:
        return 'B'
    elif row['DoW'] == 1 and row['2DoW'] == 2.5:
        return 'C'
    elif row['DoW'] == 1 and row['2DoW'] == 3:
        return 'D'
    else:
        return 'E'
df['Type'] = df.apply(func, axis=1)

df2 = df[df['DoW'].isin(['1', '1.5', '2', '2.5', '3', '3.5'])]
df2 = df.groupby(['Y', 'W']).agg({'O': 'first', 'H': 'max', 'L': 'min', 'C': 'last'})

df4 = pd.merge(df2, df3, on=['Y', 'W'])
df4.to_csv('6session_merged.csv')

df['pW_RNG'] = df['W_RNG'].shift(1)
x = df['prcnt'] = round(df['D_RNG'] / df['W_RNG'] * 100)
df['pprcnt'] = df['prcnt'].shift(1)

# plot
total = float(len(df['pprcnt']))
ax = sns.histplot(data=df, x="prcnt", kde=True, color="salmon", binwidth=1)
plt.axvline(x.max()-x.std()*2, color='k', linestyle='dashed', linewidth=1)
for p in ax.patches:
    percentage = '{:.1f}%'.format(100 * p.get_height()/total)
    x = p.get_x() + p.get_width()
    y = p.get_height()
    ax.annotate(percentage, (x, y), ha='center')
    print(percentage)
plt.show()

# signal - con1 rng>prng, con2 rth only
df['con1'] = [1 if rng > prng else 0 for rng, prng in zip(df['RNG_ses'], df['pRNG_ses'])]
df['con2'] = [1 if s == 1.5 or s == 2.5 or s == 3.5 or s == 4.5 or s == 5.5 else 0 for s in df['DoW']]
df['signal'] = [1 if c1+c2 == 2 else 0 for c1, c2 in zip(df['con1'], df['con2'])]

# plot line chart of Hi and Lo
plt.plot(df['BOTH_H'])
plt.show()
# markers
markers = [mr for mr, close in enumerate(df['BOTH_H']) if df['signal'][mr] == 1]
plt.suptitle("Buying Opportunities")
plt.plot(df['BOTH_H'], marker='X', markerfacecolor='r', markevery=markers)
plt.show()

weekly_limits = df.groupby(['Y', 'W']).agg({'BOTH_H': 'max', 'BOTH_L': 'min'}).reset_index()
weely_limits.to_csv('weekly_2ses.csv')

df_with_weekly_limits = pd.merge(df, weekly_limits, on=['Y', 'W'])
df_with_weekly_limits.to_csv('dohromady_2ses.csv')

df = df.drop_duplicates('Strategy')
df2 = pd.read_csv('tos_day_rth_settlement_adjusted.csv', sep=';')
df3 = pd.merge(df1, df2, left_on='Date', right_on='Date', how='left')

df2 = df.groupby(['Year', 'Week_Number']).head(3).reset_index(drop=True)
df3 = df.loc[df['DoW'] == 5]

df['DATUM'] = pd.to_datetime(df['DATUM'])
df['Week_Day'] = df['DATUM'].dt.dayofweek
df['Week_Number'] = df['DATUM'].dt.isocalendar().week
df['Month_Number'] = df['DATUM'].dt.month
df['Year'] = df['DATUM'].dt.isocalendar().year


df = pd.read_csv('zz_1962-2020rth.csv', sep=';')
df = df.set_index(pd.DatetimeIndex(df['Date'].values))

df['Date2'] = pd.to_datetime(df['Date'])
df['Y'] = df['Date2'].dt.isocalendar().year
df['DoW'] = df['Date2'].dt.dayofweek
df = df[df['Y'].isin([1985])]

mpf.plot(df, type='candle', show_nontrading=True)


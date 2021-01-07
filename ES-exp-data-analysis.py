import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(color_codes=True)
pd.set_option('display.max_columns', 500)

df = pd.read_csv('es_data_final.csv', sep=';')

df['index1'] = df.index
on_high = df['ON_H']
on_low = df['ON_L']
ib_high = df['IB_H']
ib_low = df['IB_L']
rth_high = df['RTH_H']
rth_low = df['RTH_L']
on_range = df['ON_RNG']
ib_range = df['IB_RNG']
rth_range = df['RTH_RNG']
on_0az12rng = df['ON_RNG'] < 12  # true/false

ib_rng_arr = ib_range.to_numpy()
rth_rng_arr = rth_range.to_numpy()
on_rng_arr = on_range.to_numpy()

# 000 describe dataframe all_no_plot
print(df.shape)
print(df.describe())
print(df.head(4))

# 001 Correlation matrix ON vs RTH vs IB ranges
cdf = df[['ON_RNG', 'RTH_RNG', 'IB_RNG']]
corr_matrix = cdf.corr()
print(corr_matrix)

# 002 Exp data analysis distribution ranges all combined
plt.hist(rth_range, 250, color='black', alpha=0.5)
plt.hist(on_range, 250, color='coral', alpha=0.5)
plt.hist(ib_range, 250, color='blue', alpha=0.5)
plt.show()

# 003 RTH range - ON range _ outliers
rth_vs_on_arr = (rth_rng_arr - on_rng_arr)
plt.plot([df.index], [rth_vs_on_arr], 'ro')
plt.axis([0, 1050, -30, 50])
plt.show()

# 004 Expectancy - Liner regression ON vs RTH ranges
ax = sns.regplot(x="ON_RNG", y="RTH_RNG", data=df)
plt.show()

# 005 scatter IBr vs RTHr
plt.scatter(df['IB_RNG'], df['RTH_RNG'])  
plt.show()

# 006 all ranges line charts
df['RTH_RNG'].plot()  
df['ON_RNG'].plot()
df['IB_RNG'].plot()
plt.legend()
plt.grid()
plt.show()

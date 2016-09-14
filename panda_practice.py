import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df_high = pd.read_csv('data/xa_high_food.csv', comment='#', header=None)
df_low = pd.read_csv('data/xa_low_food.csv', comment='#', header=None)

df = pd.concat((df_low, df_high), axis=1)
df.columns = ['low', 'high']
df.to_csv('data/xa_combined.csv', index=False)

df_tidy = pd.melt(df, var_name='food density', value_name='cross-sectional area (sq.micron)').dropna()

low_over_2100 = df_tidy.loc[(df_tidy['food density']=='low') & (df_tidy['cross-sectional area (sq.micron)'] > 2100), :]

df_frog = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')

df_big_force = df_frog.loc[df_frog['impact force (mN)'] > 1000, :]

df_frog.loc[(df_frog['date']=='2013_05_27') & (df_frog['trial number']==3) & (df_frog['ID']=='III'), :]

plt.plot(df_frog.loc[:, 'impact force (mN)'], df_frog.loc[:, 'adhesive force (mN)'], marker='.', linestyle='none')
plt.show()
plt.close()

df_frog_renamed = df_frog.rename(columns={'impact force (mN)': 'impf', 'adhesive force (mN)': 'adf'})

# We only want ID's and impact forces, so slice those out
df_impf = df_frog_renamed.loc[:, ['ID', 'impf']]

# Make a GroupBy object
grouped = df_impf.groupby('ID')

# Apply the np.mean function to the grouped object
df_mean_impf = grouped.apply(np.mean)

# Look at the new DataFrame
df_mean_impf

def coeff_of_var(data):
    df_std = data.apply(np.std)
    df_mean = data.apply(np.mean)
    coeff = df_std / abs(df_mean)
    return coeff

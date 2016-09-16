import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import pandas as pd
import scipy
import seaborn as sns
sns.set()

df = pd.read_csv('data/bcd_gradient.csv', comment='#')
df = df.rename(columns={'fractional distance from anterior': 'x', '[bcd] (a.u.)': 'I_bcd'})

def gradient_model(x, I_0, a, lam):
    """
    Model for Bcd gradient: exponential decay plus background.
    """
    if np.any(np.array(x) < 0):
        raise RuntimeError('x must be positive.')
    if np.any(np.array([I_0, a, lam]) < 0):
        raise RuntimeError('all params must be positive.')
    return a + I_0 * np.exp(-x / lam)

a_guess = 0.2
I_0_guess = 0.9 - 0.2
lam_guess = 0.25

p0 = np.array([I_0_guess, a_guess, lam_guess])
popt, _ = scipy.optimize.curve_fit(gradient_model, df['x'], df['I_bcd'], p0=p0)

x_smooth = np.linspace(0, 1, 200)
I_smooth = gradient_model(x_smooth, *tuple(popt))

plt.plot(x_smooth, I_smooth, color='gray')
plt.plot(df['x'], df['I_bcd'], linestyle='none', marker = '.', markersize=15)

plt.show()
plt.close()

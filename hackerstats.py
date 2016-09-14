import numpy as np
import matplotlib.pyplot as pyplot
import seaborn as sns
from bootcamp_utils import *
sns.set()

bd_1975 = np.loadtxt('data/beak_depth_scandens_1975.csv')
bd_2012 = np.loadtxt('data/beak_depth_scandens_2012.csv')

x_1975, y_1975 = ecdf(bd_1975)
x_2012, y_2012 = ecdf(bd_2012)

# plt.plot(x_1975, y_1975, marker='.', linestyle='none', markersize=15, alpha=0.5)
# plt.plot(x_2012, y_2012, marker='.', linestyle='none', markersize=15, alpha=0.5)
# plt.xlabel('beak depth (mm)')
# plt.ylabel('ECDF')
# plt.legend(('1975', '2012'), loc='lower right')
# plt.show()
# plt.close()

mean_1975 = np.mean(bd_1975)
mean_2012 = np.mean(bd_2012)

std_1975 = np.std(bd_1975)
std_1975 = np.std(bd_2012)

bs_sample = np.random.choice(bd_1975, replace=True, size=len(bd_1975))

x_1975_bs, y_1975_bs = ecdf(bs_sample)

plt.plot(x_1975, y_1975, marker='.', linestyle='none', markersize=15, alpha=0.5)
plt.plot(x_1975_bs, y_1975_bs, marker='.', linestyle='none', markersize=15, alpha=0.5)
plt.show()
plt.close()

def draw_bs_reps(data, func, size=1):
    """
    return bootstrap statistic specified by func for array data
    """
    # Initialize inputs
    n = len(data)
    n_reps = 10000
    reps = np.empty(n_reps, float)

    # Compute bootstrap samples and fill array with statistic specified by func
    for i in range(n_reps):
        bs_sample = np.random.choice(data, replace=True, size=n)
        reps[i] = func(bs_sample)

    return reps

print(draw_bs_reps(x_1975, np.mean))

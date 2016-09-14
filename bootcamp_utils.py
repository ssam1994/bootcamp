'''
A collection of statistical functions.
'''

import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import seaborn as sns

rc = {'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

def ecdf(data):
    '''
    Compute x, y values for an empirical distribution function
    '''
    x = np.sort(data)
    y = np.arange(0, 1, 1/len(x))

    return x, y
    
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

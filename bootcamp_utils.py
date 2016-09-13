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

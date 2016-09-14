import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import seaborn as sns
from bootcamp_utils import *
sns.set()

# Parameters
# Number of generations
n_gen = 16

# Chance of beneficial mutation
r = 1e-5

# Total number of cells
n_cells = 2**(n_gen - 1)

# Adaptive immunity: binomial distribution
ai_samples = np.random.binomial(n_cells, r, size=100000)
print('AI mean:', np.mean(ai_samples))
print('AI std:', np.std(ai_samples))
print('AI Fano:', np.var(ai_samples) / np.mean(ai_samples))

# Random mutation: binomial distribution

# Function to draw out of random mutation hypothesis
def draw_random_mutation(n_gen, r):
    """
    Draw sample under random mutation hypothesis.
    """
    # Initialize number of mutations
    n_mut = 0

    for g in range(n_gen):
        n_mut = 2*n_mut + np.random.binomial(2**g - 2*n_mut, r)

    return n_mut

def sample_random_mutation(n_gen, r, size=1):
    # Initialize samples
    samples = np.empty(size)

    # Draw the samples
    for i in range(size):
        samples[i] = draw_random_mutation(n_gen, r)

rm_samples = sample_random_mutation(n_gen, r, size=100000)
print('rm_samples', rm_samples)

x_ai, y_ai = ecdf(ai_samples)
x_rm, y_rm = ecdf(rm_samples)

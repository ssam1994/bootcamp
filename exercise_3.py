import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import seaborn as sns

rc = {'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

"""
3.2
"""
wt = np.loadtxt('data/wt_lac.csv', delimiter=',', skiprows=3)
q18m = np.loadtxt('data/q18m_lac.csv', delimiter=',', skiprows=3)
q18a = np.loadtxt('data/q18a_lac.csv', delimiter=',', skiprows=3)

wt_x = wt[:,0]
wt_y = wt[:,1]

q18m_x = q18m[:,0]
q18m_y = q18m[:,1]

q18a_x = q18a[:,0]
q18a_y = q18a[:,1]

plt.semilogx(wt_x, wt_y, marker='.', linestyle='none', markersize=15)
plt.semilogx(q18m_x, q18m_y, marker='.', linestyle='none', markersize=15)
plt.semilogx(q18a_x, q18a_y, marker='.', linestyle='none', markersize=15)

plt.legend(('Wild Type', 'Q18M', 'Q18A'), loc='upper left')

plt.xlabel('IPTG conc (mM)')
plt.ylabel('fold change')


def fold_change(c, RK, KdA=0.017, KdI=0.002, Kswitch=5.8):
    """
    Compute fold change
    """
    num = RK * (1 + (c/KdA))**2
    denom = (1 + c/KdA)**2 + Kswitch * (1 + c/KdI)**2
    fold_change = (1 + num/denom)**(-1)
    return fold_change

spaces = np.logspace(-5, 2, 20)
wt_theo_y = fold_change(spaces, 141.5)
q18a_theo_y = fold_change(spaces, 16.56)
q18m_theo_y = fold_change(spaces, 1328)

plt.semilogx(spaces, wt_theo_y, color='gray')
plt.semilogx(spaces, q18a_theo_y, color='gray')
plt.semilogx(spaces, q18m_theo_y, color='gray')
plt.show()
plt.close()

def fold_change_bohr(bohr_parameter):
    fold_change = 1 / (1 + np.e**((-1)*bohr_parameter))
    return fold_change

wt_bohr = fold_change_bohr(wt_x)
q18a_bohr = fold_change_bohr(q18a_x)
q18m_bohr = fold_change_bohr(q18m_x)

plt.semilogx(wt_bohr, wt_y, marker='.', linestyle='none', markersize=15)
plt.semilogx(q18m_bohr, q18m_y, marker='.', linestyle='none', markersize=15)
plt.semilogx(q18a_bohr, q18a_y, marker='.', linestyle='none', markersize=15)

x = np.linspace(-6, 6, 200)
plt.plot(x, fold_change_bohr(x), color='black')
plt.ylim(0.4, 1.1)
plt.xlabel('Bohr Parameter')
plt.ylabel('Fold Change')

plt.legend(('Wild Type', 'Q18M', 'Q18A'), loc='upper left')

plt.savefig('data-collapse.svg', bbox_inches='tight')
plt.show()
plt.close()

"""
3.3
"""
def solve_ode():
    alpha = 1
    beta = 0.2
    delta = 0.3
    gamma = 0.8
    dt = 0.01
    t = np.arange(0, 60, dt)
    r[0] = 10
    f[0] = 1
    # Specify parameter
    k = 1

    # Specify my little time step
    delta_t = 0.01

    # Make an array of time points, evenly spaced up to 10
    t = np.arange(0, 10, delta_t)

    # Make an array to store the number of bacteria
    n = np.empty_like(t)

    # Set the initial number of bacteria
    n[0] = 1

    # Write a for loop to keep updating n as time goes on
    for i in range(1, len(t)):
        n[i] = n[i-1] + delta_t * k * n[i-1]

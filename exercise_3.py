import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import seaborn as sns

rc = {'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

wt = np.loadtxt('data/wt_lac.csv', delimiter=',', skiprows=3)
q18m = np.loadtxt('data/q18m_lac.csv', delimiter=',', skiprows=3)
q18a = np.loadtxt('data/q18a_lac.csv', delimiter=',', skiprows=3)

wt_x = wt[:,0]
wt_y = wt[:,1]

q18m_x = q18m[:,0]
q18m_y = q18m[:,1]

q18a_x = q18a[:,0]
q18a_y = q18a[:,1]

plt.semilogx(wt_x, wt_y, marker='.', linestyle='none')
plt.semilogx(q18m_x, q18m_y, marker='.', linestyle='none')
plt.semilogx(q18a_x, q18a_y, marker='.', linestyle='none')

plt.legend(('Wild Type', 'Q18M', 'Q18A'), loc='lower right')

plt.xlabel('$log_10$ IPTG (mM)')
plt.ylabel('$log_2$ fold change')


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

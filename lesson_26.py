import numpy as np
import matplotlib.pyplot as plt
import bootcamp_utils
import seaborn as sns

sns.set()

#print(np.random.random())
x = np.random.random(size=20)
x_ecdf, y_ecdf = bootcamp_utils.ecdf(x)

plt.plot(x_ecdf[::1000], y_ecdf[::1000], marker='.', linestyle='none', markersize=10)
#plt.show()
plt.close()

heads = x <= 0.5
print(np.sum(heads))

reversals = x <= 9/36

print('reversals: ', np.sum(reversals))

x = np.random.normal(7, 1, size=100000)
_ = plt.hist(x, bins=100)
plt.show()
plt.close()

bases = 'ATGC'

x = np.random.randint(0, 4, size=50)

seq_list = [None]*50
for i, b in enumerate(x):
    seq_list[i] = bases[b]

print(''.join(seq_list))

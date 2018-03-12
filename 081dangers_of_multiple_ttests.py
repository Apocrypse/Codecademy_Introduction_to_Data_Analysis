from scipy.stats import ttest_ind
import numpy as np

a = np.genfromtxt("store_a.csv",  delimiter=",")
b = np.genfromtxt("store_b.csv",  delimiter=",")
c = np.genfromtxt("store_c.csv",  delimiter=",")

a_mean = np.mean(a)
b_mean = np.mean(b)
c_mean = np.mean(c)

a_std = np.std(a)
b_std = np.std(b)
c_std = np.std(c)

print(a_mean, a_std)
print(b_mean, b_std)
print(c_mean, c_std)

a_b_tstat, a_b_pval =  ttest_ind(a, b)
a_c_tstat, a_c_pval =  ttest_ind(a, c)
b_c_tstat, b_c_pval =  ttest_ind(b, c)

error_prob = 1 - 0.95 ** 3
print(error_prob)

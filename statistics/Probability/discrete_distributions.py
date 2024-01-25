import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

# Binomial Distribution Example
n, p = 10, 0.5  # number of trials and probability of success
binom_dist = stats.binom(n, p)
x = np.arange(0, n+1)
pmf_binom = binom_dist.pmf(x)

plt.figure(figsize=(8, 4))
plt.bar(x, pmf_binom)
plt.title('Binomial Distribution (n=10, p=0.5)')
plt.xlabel('Number of Successes')
plt.ylabel('Probability')
plt.grid()
plt.show()

# Poisson Distribution Example
lambda_ = 3  # average rate (events per interval)
poisson_dist = stats.poisson(lambda_)
x = np.arange(0, 10)
pmf_poisson = poisson_dist.pmf(x)

plt.figure(figsize=(8, 4))
plt.bar(x, pmf_poisson)
plt.title('Poisson Distribution (lambda=3)')
plt.xlabel('Number of Events')
plt.ylabel('Probability')
plt.grid()
plt.show()

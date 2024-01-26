import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set the style of seaborn for better visuals
sns.set_style("darkgrid")

# Binomial Distribution
n, p = 10, 0.5  # number of trials, probability of each trial
binomial_data = np.random.binomial(n, p, 1000)
plt.subplot(5, 1, 1)  # 5 rows, 1 column, 1st subplot
sns.histplot(binomial_data, kde=False, color='blue', discrete=True)
plt.title("Binomial Distribution (n=10, p=0.5)")

# Poisson Distribution
lambda_ = 4  # rate or known number of occurrences
poisson_data = np.random.poisson(lambda_, 1000)
plt.subplot(5, 1, 2)  # 5 rows, 1 column, 2nd subplot
sns.histplot(poisson_data, kde=False, color='green', discrete=True)
plt.title("Poisson Distribution (lambda=4)")

# Geometric Distribution
p = 0.2  # probability of success
geometric_data = np.random.geometric(p, 1000)
plt.subplot(5, 1, 3)  # 5 rows, 1 column, 3rd subplot
sns.histplot(geometric_data, kde=False, color='red', discrete=True)
plt.title("Geometric Distribution (p=0.2)")

# Negative Binomial Distribution
r, p = 5, 0.5  # number of successes, probability of each trial
neg_binomial_data = np.random.negative_binomial(r, p, 1000)
plt.subplot(5, 1, 4)  # 5 rows, 1 column, 4th subplot
sns.histplot(neg_binomial_data, kde=False, color='purple', discrete=True)
plt.title("Negative Binomial Distribution (r=5, p=0.5)")

# Hypergeometric Distribution
M, n, N = 20, 7, 12  # population size, number of successes in population, sample size
hypergeom_data = np.random.hypergeometric(M, n, N, 1000)
plt.subplot(5, 1, 5)  # 5 rows, 1 column, 5th subplot
sns.histplot(hypergeom_data, kde=False, color='orange', discrete=True)
plt.title("Hypergeometric Distribution (M=20, n=7, N=12)")

# Adjust layout and show plot
plt.tight_layout()
plt.show()

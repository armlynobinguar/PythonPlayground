import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set the style of seaborn for better visuals
sns.set_style("darkgrid")

# Binomial Distribution
n, p = 10, 0.5  # number of trials, probability of each trial
binomial_data = np.random.binomial(n, p, 1000)
plt.subplot(3, 1, 1)  # 3 rows, 1 column, 1st subplot
sns.histplot(binomial_data, kde=False, color='blue', discrete=True)
plt.title("Binomial Distribution (n=10, p=0.5)")

# Poisson Distribution
lambda_ = 4  # rate or known number of occurrences
poisson_data = np.random.poisson(lambda_, 1000)
plt.subplot(3, 1, 2)  # 3 rows, 1 column, 2nd subplot
sns.histplot(poisson_data, kde=False, color='green', discrete=True)
plt.title("Poisson Distribution (lambda=4)")

# Geometric Distribution
p = 0.2  # probability of success
geometric_data = np.random.geometric(p, 1000)
plt.subplot(3, 1, 3)  # 3 rows, 1 column, 3rd subplot
sns.histplot(geometric_data, kde=False, color='red', discrete=True)
plt.title("Geometric Distribution (p=0.2)")

# Adjust layout and show plot
plt.tight_layout()
plt.show()

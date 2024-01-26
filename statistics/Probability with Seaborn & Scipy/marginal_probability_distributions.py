import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import multivariate_normal

# Example 1: Marginal Probability Distribution from a Discrete Joint Probability Distribution
# Consider a joint distribution of two discrete random variables X and Y
joint_probs = {('A', 'X'): 0.1, ('A', 'Y'): 0.3, ('B', 'X'): 0.2, ('B', 'Y'): 0.4}
marginal_probs_X = {}
marginal_probs_Y = {}

# Calculate marginal probabilities
for (a, b), p in joint_probs.items():
    marginal_probs_X[a] = marginal_probs_X.get(a, 0) + p
    marginal_probs_Y[b] = marginal_probs_Y.get(b, 0) + p

# Display marginal probabilities
print("Marginal Probabilities of X:", marginal_probs_X)
print("Marginal Probabilities of Y:", marginal_probs_Y)

# Example 2: Marginal Probability Distribution from a Continuous Joint Probability Distribution
# Consider a bivariate normal distribution
mean = [0, 0]
cov = [[1, 0.5], [0.5, 1]]  # covariance matrix
x, y = np.random.multivariate_normal(mean, cov, 5000).T

# Plotting the joint distribution and its marginals
fig, ax = plt.subplots(2, 2, figsize=(10, 10), gridspec_kw={"height_ratios": (.15, .85),
                                                            "width_ratios": (.85, .15),
                                                            "wspace": 0.1, "hspace": 0.1})

# Joint distribution
sns.kdeplot(x=x, y=y, ax=ax[1][0], cmap="Reds", shade=True, bw_adjust=0.5)

# Marginal X
sns.kdeplot(x=x, ax=ax[0][0], color="r", fill=True)
ax[0][0].set_xlim(ax[1][0].get_xlim())
ax[0][0].axis('off')

# Marginal Y
sns.kdeplot(y=y, ax=ax[1][1], color="r", fill=True, vertical=True)
ax[1][1].set_ylim(ax[1][0].get_ylim())
ax[1][1].axis('off')

ax[1][0].set_xlabel("X")
ax[1][0].set_ylabel("Y")
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import multivariate_normal

# Discrete Joint Probability Distribution Example
# Consider two dice rolls (each die can take values from 1 to 6)
dice_rolls = [(i, j) for i in range(1, 7) for j in range(1, 7)]
prob_each_roll = 1 / 36  # Since each outcome is equally likely

# Print some outcomes and their probabilities
print("Some outcomes and their probabilities:")
for outcome in dice_rolls[:5]:  # Display first 5 for brevity
    print(f"Outcome: {outcome}, Probability: {prob_each_roll}")

# Continuous Joint Probability Distribution Example - Bivariate Normal Distribution
mean = [0, 0]  # Mean values of two normally distributed variables
cov = [[1, 0.5], [0.5, 1]]  # Covariance matrix

# Generate random samples
x, y = np.random.multivariate_normal(mean, cov, 5000).T

# Plot the bivariate distribution
plt.figure(figsize=(8, 6))
sns.kdeplot(x=x, y=y, cmap="Blues", shade=True, bw_adjust=0.5)
plt.title("Bivariate Normal Distribution")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

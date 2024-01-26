import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import multivariate_normal, uniform

# Example 1: Two discrete random variables with different probabilities
# Let's consider a simple game scenario with two outcomes: Win or Lose
# The probability of winning for Player 1 is 0.7 and for Player 2 is 0.5

outcomes = ["Win", "Lose"]
player1_probs = {"Win": 0.7, "Lose": 0.3}
player2_probs = {"Win": 0.5, "Lose": 0.5}

# Calculate joint probabilities
joint_probs = {}
for outcome1 in outcomes:
    for outcome2 in outcomes:
        joint_probs[(outcome1, outcome2)] = player1_probs[outcome1] * player2_probs[outcome2]

# Print joint probabilities
print("Joint probabilities for two players:")
for outcome, prob in joint_probs.items():
    print(f"Outcome: {outcome}, Probability: {prob:.2f}")

# Example 2: Continuous joint probability distribution - Bivariate Uniform Distribution
# Define ranges for each variable
range_x = (0, 1)
range_y = (0, 1)

# Generate random samples for X and Y
x = uniform.rvs(range_x[0], range_x[1] - range_x[0], size=1000)
y = uniform.rvs(range_y[0], range_y[1] - range_y[0], size=1000)

# Plot the bivariate uniform distribution
plt.figure(figsize=(8, 6))
plt.scatter(x, y, alpha=0.5)
plt.title("Bivariate Uniform Distribution")
plt.xlabel("X")
plt.ylabel("Y")
plt.xlim(range_x)
plt.ylim(range_y)
plt.show()

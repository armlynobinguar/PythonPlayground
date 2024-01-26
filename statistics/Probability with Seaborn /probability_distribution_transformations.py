import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set the style for better visuals
sns.set_style("darkgrid")

# Original Distribution (Normal Distribution)
mu, sigma = 0, 1  # mean and standard deviation
data = np.random.normal(mu, sigma, 1000)
plt.figure(figsize=(12, 8))

# Original Distribution
plt.subplot(2, 2, 1)
sns.histplot(data, kde=True)
plt.title("Original Distribution (Normal)")

# Scaling the Distribution
scaled_data = data * 2
plt.subplot(2, 2, 2)
sns.histplot(scaled_data, kde=True)
plt.title("Scaled Distribution (x2)")

# Shifting the Distribution
shifted_data = data + 3
plt.subplot(2, 2, 3)
sns.histplot(shifted_data, kde=True)
plt.title("Shifted Distribution (+3)")

# More Complex Transformation (Square)
squared_data = data**2
plt.subplot(2, 2, 4)
sns.histplot(squared_data, kde=True)
plt.title("Squared Distribution")

# Adjust layout and show plot
plt.tight_layout()
plt.show()

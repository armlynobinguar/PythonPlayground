import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set the style for better visuals
sns.set_style("darkgrid")

# Generating an original distribution
# In this case, we use a normal distribution as a base example.
mu, sigma = 0, 1  # mean and standard deviation for the normal distribution
data = np.random.normal(mu, sigma, 1000)

# Preparing to plot multiple subplots for comparison
plt.figure(figsize=(12, 8))

# Plotting the Original Distribution
# This subplot shows the normal distribution without any transformations.
plt.subplot(2, 2, 1)
sns.histplot(data, kde=True)
plt.title("Original Distribution (Normal)")
# Histogram is used for plotting the frequency of score occurrences in a continuous data set.

# Scaling the Distribution
# Here, we multiply the data by a factor (2 in this case) to stretch the distribution.
scaled_data = data * 2
plt.subplot(2, 2, 2)
sns.histplot(scaled_data, kde=True)
plt.title("Scaled Distribution (x2)")
# Scaling changes the spread of the data without altering its shape.

# Shifting the Distribution
# We add a constant (3 here) to every data point, shifting the distribution.
shifted_data = data + 3
plt.subplot(2, 2, 3)
sns.histplot(shifted_data, kde=True)
plt.title("Shifted Distribution (+3)")
# Shifting translates the distribution along the x-axis.

# Complex Transformation: Squaring
# Applying a non-linear transformation by squaring each data point.
# This can significantly change the shape of the distribution.
squared_data = data**2
plt.subplot(2, 2, 4)
sns.histplot(squared_data, kde=True)
plt.title("Squared Distribution")
# Non-linear transformations can lead to more dramatic changes in distribution shape.

# Adjust layout and show the combined plot
plt.tight_layout()
plt.show()


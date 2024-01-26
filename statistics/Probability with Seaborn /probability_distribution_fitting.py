import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm, expon

# Generate sample data
# For this example, we create some artificial data that roughly follows a normal distribution.
data = np.random.normal(loc=0, scale=1, size=1000)

# Fit distributions to the data
# We use MLE to estimate the parameters of the normal and exponential distributions.
norm_params = norm.fit(data)  # Fitting a normal distribution
expon_params = expon.fit(data)  # Fitting an exponential distribution

# Plotting the original data and fitted distributions
plt.figure(figsize=(12, 6))
sns.histplot(data, kde=False, norm_hist=True, color="skyblue", label="Data Histogram")
x = np.linspace(min(data), max(data), 100)

# Plot the fitted normal distribution
plt.plot(x, norm.pdf(x, *norm_params), 'r-', lw=2, label='Fitted Normal Dist.')

# Plot the fitted exponential distribution
plt.plot(x, expon.pdf(x, *expon_params), 'g-', lw=2, label='Fitted Exponential Dist.')

plt.title("Probability Distribution Fitting")
plt.legend()
plt.show()

# Output the estimated parameters
print("Estimated Parameters for Normal Distribution: mean = {:.2f}, std = {:.2f}".format(*norm_params))
print("Estimated Parameters for Exponential Distribution: lambda = {:.2f}".format(expon_params[1]))

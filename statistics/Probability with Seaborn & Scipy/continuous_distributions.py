import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set the style of seaborn for better visuals
sns.set_style("darkgrid")

# Normal Distribution
mu, sigma = 0, 0.1  # mean and standard deviation
normal_data = np.random.normal(mu, sigma, 1000)
plt.subplot(5, 1, 1)  # 5 rows, 1 column, 1st subplot
sns.histplot(normal_data, kde=True, color='blue')
plt.title("Normal Distribution (mu=0, sigma=0.1)")

# Exponential Distribution
lambda_ = 1.0  # rate parameter
exponential_data = np.random.exponential(1/lambda_, 1000)
plt.subplot(5, 1, 2)  # 5 rows, 1 column, 2nd subplot
sns.histplot(exponential_data, kde=True, color='green')
plt.title("Exponential Distribution (lambda=1.0)")

# Uniform Distribution
a, b = 0, 1  # lower and upper boundary
uniform_data = np.random.uniform(a, b, 1000)
plt.subplot(5, 1, 3)  # 5 rows, 1 column, 3rd subplot
sns.histplot(uniform_data, kde=True, color='red')
plt.title("Uniform Distribution (a=0, b=1)")

# Beta Distribution
alpha, beta = 2, 5  # shape parameters
beta_data = np.random.beta(alpha, beta, 1000)
plt.subplot(5, 1, 4)  # 5 rows, 1 column, 4th subplot
sns.histplot(beta_data, kde=True, color='purple')
plt.title("Beta Distribution (alpha=2, beta=5)")

# Gamma Distribution
shape, scale = 2., 2.  # shape and scale
gamma_data = np.random.gamma(shape, scale, 1000)
plt.subplot(5, 1, 5)  # 5 rows, 1 column, 5th subplot
sns.histplot(gamma_data, kde=True, color='orange')
plt.title("Gamma Distribution (shape=2, scale=2)")

# Adjust layout and show plot
plt.tight_layout()
plt.show()

import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

# Normal Distribution Example
mu, sigma = 0, 1  # mean and standard deviation
normal_dist = stats.norm(mu, sigma)
x = np.linspace(-3, 3, 1000)
pdf_normal = normal_dist.pdf(x)

plt.figure(figsize=(8, 4))
plt.plot(x, pdf_normal)
plt.title('Normal Distribution (mu=0, sigma=1)')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.grid()
plt.show()

# Exponential Distribution Example
lambda_ = 1  # rate parameter
exponential_dist = stats.expon(scale=1/lambda_)
x = np.linspace(0, 10, 1000)
pdf_exponential = exponential_dist.pdf(x)

plt.figure(figsize=(8, 4))
plt.plot(x, pdf_exponential)
plt.title('Exponential Distribution (lambda=1)')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.grid()
plt.show()

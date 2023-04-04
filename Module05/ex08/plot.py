import numpy as np
import matplotlib.pyplot as plt
import pylab

def add_intercept(x):
	if x.ndim == 1:
		return [[1, elem] for elem in x]
	else:
		return np.insert(x, 0, 1, 1)

def loss(y, y_hat):
	cost = y - y_hat
	return np.dot(cost, cost) / cost.shape[0]

def plot_with_loss(x, y, theta):
	y_hat = np.matmul(add_intercept(x), theta)
	cost = loss(y, y_hat)

	plt.plot(x, x * theta[1] + theta[0])
	for n in range(x.shape[0]):
		plt.vlines(x[n], y[n], y_hat[n], colors = 'red', linestyles='dotted')
	plt.plot(x, y, 'o')
	plt.title(f"Cost : {cost:.6f}")
	pylab.show()

x = np.arange(1,6)
y = np.array([11.52434424, 10.62589482, 13.14755699, 18.60682298, 14.14329568])
# Example 1:
theta1= np.array([18,-1])
plot_with_loss(x, y, theta1)

# Example 2:
# theta2 = np.array([14, 0])
# plot_with_loss(x, y, theta2)
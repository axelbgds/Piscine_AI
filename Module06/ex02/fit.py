import numpy as np

def gradient(x, y, theta):
	x_prime = np.insert(x, 0, 1, 1)
	return np.array(x_prime.T @ (x_prime @ theta - y) / y.shape[0])

def fit_(x, y, theta, alpha, max_iter):
	for n in range(max_iter):
		res_gradient = gradient(x, y, theta)
		theta = theta - alpha * res_gradient
	return theta

x = np.array([[12.4956442], [21.5007972], [31.5527382], [48.9145838], [57.5088733]])
y = np.array([[37.4013816], [36.1473236], [45.7655287], [46.6793434], [59.5585554]])
theta= np.array([1, 1]).reshape((-1, 1))
print(fit_(x, y, theta, alpha=5e-8, max_iter=1500000))
# Output:
# array([[1.40709365],
# [1.1150909 ]])
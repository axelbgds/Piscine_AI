import numpy as np
from sklearn.metrics import mean_squared_error

def add_intercept(x):
	if x.ndim == 1:
		return [[1, elem] for elem in x]
	else:
		return np.insert(x, 0, 1, 1)

def loss(y, y_hat):
	cost = y - y_hat
	return np.dot(cost, cost) / cost.shape[0]

def predict(x, theta):
	return np.matmul(add_intercept(x), theta)

def simple_gradient(x, y, theta):
	y_hat = np.matmul(add_intercept(x), theta)
	return np.array([np.sum(y_hat - y) / y.shape[0], ((y_hat - y).T @ x).item(0) / y.shape[0]])

x = np.array([12.4956442, 21.5007972, 31.5527382, 48.9145838, 57.5088733]).reshape((-1, 1))
y = np.array([37.4013816, 36.1473236, 45.7655287, 46.6793434, 59.5585554]).reshape((-1, 1))
# Example 0:
theta1 = np.array([2, 0.7]).reshape((-1, 1))
print(simple_gradient(x, y, theta1))
# # Output:
# array([[-19.0342574], [-586.66875564]])
# # Example 1:
theta2 = np.array([1, -0.4]).reshape((-1, 1))
print(simple_gradient(x, y, theta2))
# # Output:
# array([[-57.86823748], [-2230.12297889]])
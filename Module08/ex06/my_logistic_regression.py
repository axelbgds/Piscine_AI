import numpy as np
import math

class MyLogisticRegression():
	def __init__(self, theta, alpha=0.001, max_iter=10000):
		self.alpha = alpha
		self.max_iter = max_iter
		self.theta = theta
		# print("theta: ", theta)
	
	def predict_(self, x):
		x_prime = np.insert(x, 0, 1, 1)
		y_hat = x_prime @ self.theta
		vfunc = np.vectorize(lambda n : 1 / (1 + math.exp(-n)))
		return vfunc(y_hat)

	def loss_elem_(self, y, y_hat):
		return (np.array([(y_hat[n] - y[n]) ** 2 for n in range(y.shape[0])]))

	def loss_(self, y, y_hat, eps=1e-15):
		y_hat[y_hat == 0] = eps
		y_hat[y_hat == 1] = 1 - eps
		return (-sum(y[n] * math.log(y_hat[n]) + (1 - y[n]) * math.log(1 - y_hat[n]) for n in range(y.shape[0])) / y.shape[0]).item(0) #TODO find a better way

	def log_gradient(self, x, y):
		x_prime = np.insert(x, 0, 1, 1)
		y_hat = self.predict_(x)
		return x_prime.T @ (y_hat - y) / y.shape[0]

	def fit_(self, x, y):
		for n in range(self.max_iter):
			self.theta = self.theta - self.alpha * self.log_gradient(x, y)


X = np.array([[1., 1., 2., 3.], [5., 8., 13., 21.], [3., 5., 9., 14.]])
Y = np.array([[1], [0], [1]])
mylr = MyLogisticRegression(np.array([2, 0.5, 7.1, -4.3, 2.09]).reshape(-1, 1))
# Example 0:
# print(mylr.predict_(X))
# Output:
# array([[0.99930437],
# [1. ],
# [1. ]])
# # Example 1:
# print(mylr.loss_(Y, mylr.predict_(X)))
# # # Output:
# # 11.513157421577004
# # # Example 2:
mylr.fit_(X, Y)
print(mylr.theta)
# # # Output:
# array([[ 1.04565272],
# [ 0.62555148],
# [ 0.38387466],
# [ 0.15622435],
# [-0.45990099]])
# # Example 3:
print(mylr.predict_(X))
# # Output:
# array([[0.72865802],
# [0.40550072],
# [0.45241588]])
# # Example 4:
print(mylr.loss_(Y,mylr.predict_(X)))
# # Output:
# 0.5432466580663214
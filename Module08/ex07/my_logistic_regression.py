import numpy as np
import matplotlib.pyplot as plt
import math

class MyLogisticRegression():
	def __init__(self, theta, alpha=0.001, max_iter=100000):
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

	def plot_(self, x, y):
		plt.scatter(x, y)
		plt.show()
import numpy as np
import matplotlib.pyplot as plt
import math

class MyLogisticRegression():
	supported_penalties = ['l2']

	def __init__(self, theta, alpha=0.001, max_iter=100000, penalty="l2", lambda_=0.5):
		self.alpha = alpha
		self.max_iter = max_iter
		self.theta = theta
		self.penalty = penalty
		self.lambda_ = lambda_ if penalty in self.supported_penalties else 0

	
	def predict_(self, x):
		x_prime = np.insert(x, 0, 1, 1)
		y_hat = x_prime @ self.theta
		vfunc = np.vectorize(lambda n : 1 / (1 + math.exp(-n)))
		return vfunc(y_hat)

	def loss_elem_(self, y, y_hat):
		return (np.array([(y_hat[n] - y[n]) ** 2 for n in range(y.shape[0])]))

	def loss_without_penalty(self, y, y_hat, eps=1e-15):
		y_hat[y_hat == 0] = eps
		y_hat[y_hat == 1] = 1 - eps
		return (-sum(y[n] * math.log(y_hat[n]) + (1 - y[n]) * math.log(1 - y_hat[n]) for n in range(y.shape[0])) / y.shape[0]).item(0) #TODO find a better way

	def loss_(self, y, y_hat, eps=1e-15):
		return (self.loss_without_lambda(y, y_hat, eps) \
			+ self.lambda_ * self.l2(self.thetas) / (y.shape[0] * 2)).item(0)

	def log_gradient(self, x, y):
		x_prime = np.insert(x, 0, 1, 1)
		y_hat = self.predict_(x, self.thetas)
		theta_prime = np.copy(self.thetas)
		theta_prime[0] = 0
		return (x_prime.T @ (y_hat - y) + self.lambda_ * theta_prime) / y.shape[0]

	def fit_(self, x, y):
		for n in range(self.max_iter):
			self.thetas = self.thetas - self.alpha * self.log_gradient(x, y)

	def l2(self):
		v = np.array(self.thetas)
		v[0] = 0
		return np.dot(v.T, v)

	def plot_(self, x, y):
		plt.scatter(x, y)
		plt.show()

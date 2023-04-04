import numpy as np
from mylinearregression import MyLinearRegression as MyLR

class MyRidge(MyLR):
	def __init__(self, thetas, alpha=0.001, max_iter=1000, lambda_=0.5):
		self.thetas = thetas
		self.alpha = alpha
		self.max_iter = max_iter
		self.lambda_ = lambda_

	def get_params_(self):
		return self.__dict__

	def set_params_(self, **kwargs):
		self.__dict__.update(kwargs)

	def loss_elem_(self, y, y_hat): # Je suis pas sur
		return (np.array([(y_hat[n] - y[n]) ** 2 + self.lambda_ * self.l2(self.thetas) for n in range(y.shape[0])]))

	def loss_(self, y, y_hat):
		cost = y_hat - y
		return ((np.dot(cost.T, cost) + self.lambda_ * self.l2(self.thetas)) / (y_hat.shape[0] * 2)).item(0)
	
	def gradient_(self, x, y):
		x_prime = np.insert(x, 0, 1, 1)
		theta_prime = np.copy(self.thetas)
		theta_prime[0] = 0
		return (x_prime.T @ (x_prime @ self.thetas - y) + self.lambda_ * theta_prime) / y.shape[0]

	def fit_(self, x, y):
		for n in range(self.max_iter):
			res = self.gradient(x, y, self.thetas)
			self.thetas = self.thetas - self.alpha * res

	def l2(theta):
		v = np.array(theta)
		v[0] = 0
		return np.dot(v.T, v)
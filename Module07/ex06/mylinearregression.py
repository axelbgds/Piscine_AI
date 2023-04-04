import numpy as np
import matplotlib.pyplot as plt

class MyLinearRegression():
	def __init__(self, thetas, alpha=0.001, max_iter=100000):
		self.alpha = alpha
		self.max_iter = max_iter
		self.thetas = thetas

	def fit_(self, x, y):
		neoX = np.insert(x, 0, 1, 1)
		for n in range(self.max_iter):
			res = (neoX.T @ (neoX @ self.thetas - y)) / y.shape[0]
			self.thetas = self.thetas - self.alpha * res

	def predict(self, x):
		return np.insert(x, 0, 1, 1) @ self.thetas

	def mse(self, x, y):
		cost = self.predict(x) - y
		return np.dot(cost.T, cost).item(0) / y.shape[0]

	def plot(self, x, y):
		print("predict result: ", self.thetas)
		y_hat = self.predict(x)
		plt.plot(x, y_hat, 'o', color="blue")
		plt.plot(x, y, 'o')
		plt.grid()
		plt.show()
		# pylab.show()

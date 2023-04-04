import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import pylab

class MyLinearRegression():
	def __init__(self, path, thetas, alpha=0.001, max_iter=1000):
		self.data = pd.read_csv(path)
		self.x = np.array(self.data["Micrograms"]).reshape(-1,1)
		self.y = np.array(self.data["Score"]).reshape(-1,1)

		self.alpha = alpha
		self.max_iter = max_iter
		self.thetas = thetas

	def gradient(self, theta1):
		test = np.full((20, 1), -8) + (np.arange(-10, 10) / 10).reshape(-1, 1)
		x_prime = np.insert(test, 0, 1, 1)
		new_thetas = np.copy(self.thetas)
		new_thetas[1] += theta1
		print("compare: ", self.thetas, new_thetas)
		res_gradient = np.array(x_prime.T @ (x_prime @ new_thetas - self.y) / self.y.shape[0])
		print("gradient result: ", res_gradient)
		
	def predict_(self):
		return np.insert(self.x, 0, 1, 1) @ self.thetas

	def loss_elem_(self, y_hat):
		return (np.array([(y_hat[n] - self.y[n]) ** 2 for n in range(self.y.shape[0])]))

	def loss_(self, y_hat):
		cost = y_hat - self.y
		return np.dot(cost.T, cost).item(0) / (self.y.shape[0] * 2)

	def plot_predict(self):
		plt.plot(self.x, np.insert(self.x, 0, 1, 1) @ self.thetas, color="green", linestyle="--")
		# for n in range(x.shape[0]):
		# 	plt.vlines(x[n], y[n], y_hat[n], colors = 'red', linestyles='dotted')
		plt.plot(self.x, self.y, 'o', color="blue")
		plt.plot(self.x, self.predict_(), 'o', color="orange")
		plt.xlabel("Qunatity of blue pills (in micrograms)")
		plt.ylabel("Space driving score")
		plt.grid()
		# plt.title(f"Cost : {cost:.6f}")
		pylab.show()

	def plot_loss(self, y_hat):
		loss = self.loss_elem_(y_hat)
		plt.plot(self.y, loss, 'b-', color="blue")
		pylab.show()
		

	def mse_(self, y_hat):
		cost = y_hat - self.y
		return np.dot(cost.T, cost).item(0) / self.y.shape[0]


model1 = MyLinearRegression("../assets/are_blue_pills_magic.csv", np.array([[89.0], [-8]]))
model2 = MyLinearRegression("../assets/are_blue_pills_magic.csv", np.array([[89.0], [-6]]))
Y_model1 = model1.predict_()
Y_model2 = model2.predict_()
# print(model1.mse_(Y_model1), mean_squared_error(model1.y, Y_model1))
# print(model2.mse_(Y_model2), mean_squared_error(model2.y, Y_model2))

# model1.plot()

test = np.full((20, 1), -8) + (np.arange(-10, 10) / 10).reshape(-1, 1)
model1.gradient(-8)
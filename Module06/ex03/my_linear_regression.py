import numpy as np

class MyLinearRegression():
	def __init__(self, thetas, alpha=0.001, max_iter=1000):
		self.alpha = alpha
		self.max_iter = max_iter
		self.thetas = thetas

	def fit_(self, x, y):
		x_prime = np.insert(x, 0, 1, 1)
		for n in range(self.max_iter):
			res_gradient = np.array(x_prime.T @ (x_prime @ self.thetas - y) / y.shape[0])
			self.thetas = self.thetas - self.alpha * res_gradient
		return self.thetas

	def predict_(self, x):
		return np.insert(x, 0, 1, 1) @ self.thetas

	def loss_elem_(self, y, y_hat):
		return (np.array([(y_hat[n] - y[n]) ** 2 for n in range(y.shape[0])]))

	def loss_(self, y, y_hat):
		cost = y_hat - y
		return np.dot(cost.T, cost).item(0) / (y.shape[0] * 2)

x = np.array([[12.4956442], [21.5007972], [31.5527382], [48.9145838], [57.5088733]])
y = np.array([[37.4013816], [36.1473236], [45.7655287], [46.6793434], [59.5585554]])
lr1 = MyLinearRegression(np.array([2, 0.7]).reshape(-1, 1))
# Example 0.0:
print("lr1 predict:", lr1.predict_(x))
# Output:
# array([[10.74695094],
# [17.05055804],
# [24.08691674],
# [36.24020866],
# [42.25621131]])
# Example 0.1:
print("lr1 loss_elem:", lr1.loss_elem_(y, lr1.predict_(x)))
# Output:
# array([[710.45867381],
# [364.68645485],
# [469.96221651],
# [108.97553412],
# [299.37111101]])
# Example 0.2:
print("lr1 loss: ", lr1.loss_(y, lr1.predict_(x)))
# Output:
# 195.34539903032385
# Example 1.0:
lr2 = MyLinearRegression(np.array([1, 1]).reshape(-1, 1), 5e-8, 1500000)
lr2.fit_(x, y)
print("lr2 theta after fit: ", lr2.thetas)
# Output:
# array([[1.40709365],
# [1.1150909 ]])
# Example 1.1:
print("lr2 predict: ", lr2.predict_(x))
# Output:
# array([[15.3408728 ],
# [25.38243697],
# [36.59126492],
# [55.95130097],
# [65.53471499]])
# Example 1.2:
print("lr2 loss_elem: ", lr2.loss_elem_(y, lr2.predict_(x)))
# Output:
# array([[486.66604863],
# [115.88278416],
# [ 84.16711596],
# [ 85.96919719],
# [ 35.71448348]])
# Example 1.3:
print("lr2 loss: ", lr2.loss_(y, lr2.predict_(x)))
# Output:
# 80.83996294128525
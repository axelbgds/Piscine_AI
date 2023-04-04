import numpy as np

class MyLinearRegression():
	def __init__(self, thetas, alpha=0.001, max_iter=1000):
		self.alpha = alpha
		self.max_iter = max_iter
		self.thetas = thetas

	def fit_(self, x, y):
		for n in range(self.max_iter):
			res = self.gradient(x, y, self.thetas)
			self.thetas = self.thetas - self.alpha * res

	def predict_(self, x):
		return np.insert(x, 0, 1, 1) @ self.thetas

	def gradient(self, x, y, theta):
		neoX = np.insert(x, 0, 1, 1)
		return (neoX.T @ (neoX @ theta - y)) / y.shape[0]

	def loss_elem_(self, y, y_hat):
		return (np.array([(y_hat[n] - y[n]) ** 2 for n in range(y.shape[0])]))

	def loss_(self, y, y_hat):
		cost = y_hat - y
		return np.dot(cost.T, cost).item(0) / (y.shape[0] * 2)

X = np.array([[1., 1., 2., 3.], [5., 8., 13., 21.], [34., 55., 89., 144.]])
Y = np.array([[23.], [48.], [218.]])
mylr = MyLinearRegression([[1.], [1.], [1.], [1.], [1]])
# Example 0:
y_hat = mylr.predict_(X)
print(y_hat)
# Output:
# array([[8.], [48.], [323.]])
# Example 1:
print(mylr.loss_elem_(Y, y_hat))
# Output:
# array([[225.], [0.], [11025.]])
# Example 2:
print(mylr.loss_(Y, y_hat))
# Output:
# 1875.0
# Example 3:
mylr.alpha = 1.6e-4
mylr.max_iter = 200000
mylr.fit_(X, Y)
print(mylr.thetas)
# Output:
# array([[18.188..], [2.767..], [-0.374..], [1.392..], [0.017..]])
# Example 4:
y_hat = mylr.predict_(X)
print(y_hat)
# Output:
# array([[23.417..], [47.489..], [218.065...]])
# Example 5:
print(mylr.loss_elem_(Y, y_hat))
# Output:
# array([[0.174..], [0.260..], [0.004..]])
# Example 6:
print(mylr.loss_(Y, y_hat))
# Output:
# 0.0732...
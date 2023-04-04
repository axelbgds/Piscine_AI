import numpy as np

def gradient(x, y, theta):
	neoX = np.insert(x, 0, 1, 1)
	return (neoX.T @ (neoX @ theta - y)) / y.shape[0]

def predict_(x, theta):
	return np.insert(x, 0, 1, 1) @ theta

def fit_(x, y, theta, alpha, max_iter):
	for n in range(max_iter):
		res = gradient(x, y, theta)
		theta = theta - alpha * res
	return theta

x = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8., 80.]])
y = np.array([[19.6], [-2.8], [-25.2], [-47.6]])
theta = np.array([[42.], [1.], [1.], [1.]])
# Example 0:
theta2 = fit_(x, y, theta, alpha = 0.0005, max_iter=42000)
print(theta2)
# Output:
# array([[41.99..],[0.97..], [0.77..], [-1.20..]])
# Example 1:
print(predict_(x, theta2))
# Output:
# array([[19.5992..], [-2.8003..], [-25.1999..], [-47.5996..]])
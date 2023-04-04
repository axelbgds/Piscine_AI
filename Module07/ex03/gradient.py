import numpy as np

def gradient(x, y, theta):
	neoX = np.insert(x, 0, 1, 1)
	return (neoX.T @ (neoX @ theta - y)) / y.shape[0]

x = np.array([
	[ -6, -7, -9],
	[ 13, -2, 14],
	[ -7, 14, -1],
	[ -8, -4, 6],
	[ -5, -9, 6],
	[ 1, -5, 11],
	[ 9, -11, 8]
])
y = np.array([2, 14, -13, 5, 12, 4, -19]).reshape((-1, 1))
theta1 = np.array([3, 1, 2, -6]).reshape((-1, 1))
print(gradient(x, y, theta1))

theta2 = np.array([0, 0, 0, 0]).reshape((-1, 1))
print(gradient(x, y, theta2))
# Output:
# array([[ -0.71428571], [ 0.85714286], [23.28571429], [-26.42857143]])
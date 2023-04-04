import numpy as np

def add_intercept(x):
	if x.ndim == 1:
		return [[1, elem] for elem in x]
	else:
		return np.insert(x, 0, 1, 1)

def predict_(x, theta):
	# if x.size == 0 or x.shape[1] != 1 or theta.shape != (2, 1):
	# 	return None
	return np.matmul(add_intercept(x), theta)
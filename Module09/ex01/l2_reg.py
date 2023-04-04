import numpy as np

def iterative_l2(theta):
	return sum(theta[n] ** 2 for n in range(1, theta.size))

def l2(theta):
	v = np.array(theta)
	v[0] = 0
	return np.dot(v.T, v)
import numpy as np

def l2(theta):
	v = np.array(theta)
	v[0] = 0
	return np.dot(v.T, v)

def reg_loss_(y, y_hat, theta, lambda_):
	cost = y_hat - y
	return ((np.dot(cost.T, cost) + lambda_ * l2(theta)) / (y_hat.shape[0] * 2)).item(0)
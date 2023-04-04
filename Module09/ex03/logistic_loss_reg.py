import numpy as np

def l2(theta):
	v = np.array(theta)
	v[0] = 0
	return np.dot(v.T, v)

def log_loss(y, y_hat, eps=1e-15):
	y_hat[y_hat == 0] = eps
	y_hat[y_hat == 1] = 1 - eps
	return (-(np.dot(y.T, np.log(y_hat)) + np.dot((np.ones(y.shape) - y).T, np.log(np.ones(y.shape) - y_hat))) / y.shape[0]).item(0)

def reg_log_loss_(y, y_hat, theta, lambda_):
	return (log_loss(y, y_hat) + lambda_ * l2(theta) / (y.shape[0] * 2)).item(0)
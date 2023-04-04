import numpy as np
import math

def logistic_predict(x, theta):
	x_prime = np.insert(x, 0, 1, 1)
	y_hat = x_prime @ theta
	vfunc = np.vectorize(lambda n : 1 / (1 + math.exp(-n)))
	return vfunc(y_hat)

def log_loss(y, y_hat, eps=1e-15):
	y_hat[y_hat == 0] = eps
	y_hat[y_hat == 1] = 1 - eps
	return (-(np.dot(y.T, np.log(y_hat)) + np.dot((np.ones(y.shape) - y).T, np.log(np.ones(y.shape) - y_hat))) / y.shape[0]).item(0)

def vec_log_gradient(x, y, theta):
	x_prime = np.insert(x, 0, 1, 1)
	y_hat = logistic_predict(x, theta)
	return np.dot(x_prime.T, (y_hat - y)) / y.shape[0]
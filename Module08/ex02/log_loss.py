import numpy as np
import math

def logistic_predict(x, theta):
	x_prime = np.insert(x, 0, 1, 1)
	y_hat = x_prime @ theta
	vfunc = np.vectorize(lambda n : 1 / (1 + math.exp(-n)))
	return vfunc(y_hat)

def log_loss_(y, y_hat, eps=1e-15):
	y_hat[y_hat == 0] = eps
	y_hat[y_hat == 1] = 1 - eps
	return (-sum(y[n] * math.log(y_hat[n]) + (1 - y[n]) * math.log(1 - y_hat[n]) for n in range(y.shape[0])) / y.shape[0]).item(0) #TODO find a better way
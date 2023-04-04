import numpy as np
import math

# def reg_logistic_grad(y, x, theta, lambda_):
# 	for i in range(y.shape[0]):
# 		for j in range(y.shape[0]):
			
# 	pass

def logistic_predict(x, theta):
	x_prime = np.insert(x, 0, 1, 1)
	y_hat = x_prime @ theta
	vfunc = np.vectorize(lambda n : 1 / (1 + math.exp(-n)))
	return vfunc(y_hat)

def vec_reg_logistic_grad(y, x, theta, lambda_):
	x_prime = np.insert(x, 0, 1, 1)
	y_hat = logistic_predict(x, theta)
	theta_prime = np.copy(theta)
	theta_prime[0] = 0
	return (x_prime.T @ (y_hat - y) + lambda_ * theta_prime) / y.shape[0]
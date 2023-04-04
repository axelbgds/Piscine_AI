import numpy as np

# def reg_linear_grad(y, x, theta, lambda_):
# 	for i in range(y.shape[0]):
# 		for j in range(y.shape[0]):
			
# 	pass

def vec_reg_linear_grad(y, x, theta, lambda_):
	x_prime = np.insert(x, 0, 1, 1)
	y_hat = x_prime @ theta
	theta_prime = np.copy(theta)
	theta_prime[0] = 0
	return (x_prime.T @ (y_hat - y) + lambda_ * theta_prime) / y.shape[0]
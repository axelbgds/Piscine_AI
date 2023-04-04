import math
import numpy as np

def logistic_predict(x, theta):
	x_prime = np.insert(x, 0, 1, 1)
	y_hat = x_prime @ theta
	vfunc = np.vectorize(lambda n : 1 / (1 + math.exp(-n)))
	return vfunc(y_hat)
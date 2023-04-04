import numpy as np

def predict_(x, theta):
	return np.insert(x, 0, 1, 1) @ theta
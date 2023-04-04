import numpy as np

def add_intercept(x):
	if x.ndim == 1:
		return [[1, elem] for elem in x]
	else:
		return np.insert(x, 0, 1, 1)
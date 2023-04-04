import numpy as np

def minmax(x):
	min_elem = np.min(x)
	max_elem = np.max(x)
	vfunc = np.vectorize(lambda x : (x - min_elem) / (max_elem - min_elem))
	return vfunc(x)
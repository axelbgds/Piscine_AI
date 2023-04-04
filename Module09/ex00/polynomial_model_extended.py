import numpy as np

def add_polynomial_features(x, power):
	vfunc = np.vectorize(lambda e, n : e ** n)
	res = np.copy(x)
	if power < 2: # I will not take into account the cases for pow < 1
		return res
	for n in range(2, power + 1):
		res = np.append(res, vfunc(x, n), axis=1)
	return res
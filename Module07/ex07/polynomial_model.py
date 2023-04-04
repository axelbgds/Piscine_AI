import numpy as np

def add_polynomial_features(x, power):
	for n in range(power - 1):
		x = np.append(x, (x[:,0] * x[:,-1]).reshape(-1, 1), axis=1)
	return x

x = np.arange(1, 6).reshape(-1, 1)
X = add_polynomial_features(x, 6)
print(X)
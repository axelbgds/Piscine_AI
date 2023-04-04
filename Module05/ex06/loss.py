import numpy as np

def loss_elem_(y, y_hat):
	if isinstance(y, np.ndarray) == False or isinstance(y_hat, np.ndarray) or y.shape[0] != y_hat.shape[0]: 
		return None
	return np.array([(y_hat[n] - y[n]) ** 2 for n in range(np.size)])

def loss_(y, y_hat): 
	if isinstance(y, np.ndarray) == False or isinstance(y_hat, np.ndarray) or y.shape[0] != y_hat.shape[0]: 
		return None
	loss = loss_elem_(y, y_hat)
	return sum(s for s in loss) / (y.shape[0] * 2)
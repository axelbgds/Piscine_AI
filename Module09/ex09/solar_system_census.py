import numpy as np
import pandas
import sys
from my_logistic_regression import MyLogisticRegression as MyLR

def unison_shuffled_copies(a, b):
	p = np.random.permutation(len(a))
	return a[p], b[p]

def data_spliter(x, y, proportion):
	shuffled = unison_shuffled_copies(x, y)
	testNb = int(x.shape[0] * proportion)
	splitX = np.vsplit(shuffled[0], [testNb, x.shape[0]])
	splitY = np.vsplit(shuffled[1], [testNb, x.shape[0]])
	return splitX[0], splitX[1], splitY[0], splitY[1]

if __name__ == "__main__":
	pass
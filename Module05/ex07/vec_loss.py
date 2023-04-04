import numpy as np

def loss_(y, y_hat):
	cost = y_hat - y
	return cost.T @ cost / (2 * cost.size)
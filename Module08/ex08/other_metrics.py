import numpy as np

#   pred / real
# tn = 0 / 0
# tp = 1 / 1
# fn = 0 / 1
# fp = 1 / 0

def accuracy_score_(y, y_hat):
	return np.where(y == y_hat)[0].size / y.size

def precision_score_(y, y_hat, pos_label=1):
	return np.where(np.logical_and(y == pos_label, y == y_hat))[0].size / (y_hat == pos_label).sum()

def recall_score_(y, y_hat, pos_label=1):
	return np.where(np.logical_and(y == pos_label, y == y_hat))[0].size / (y == pos_label).sum()

def f1_score_(y, y_hat, pos_label=1):
	precision = precision_score_(y, y_hat, pos_label)
	recall = recall_score_(y, y_hat, pos_label)
	return (2 * precision * recall) / (precision + recall)
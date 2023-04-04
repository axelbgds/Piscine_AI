import numpy as np
import pandas

def confusion_matrix_(y_true, y_hat, labels=None, df_option=False):
	if labels == None:
		labels = np.unique(np.append(y_true, y_hat))
	res = np.zeros((len(labels), len(labels)))
	for m in range(len(labels)): #TODO find a better way
		for n in range(len(labels)):
			res[m, n] = np.where(np.logical_and(y_true == labels[m], y_hat == labels[n]))[0].size
	if df_option == True:
		return pandas.DataFrame(np.int_(res), labels, labels)
	return np.int_(res)
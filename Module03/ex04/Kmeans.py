import numpy as np

class KmeansClustering:
	def __init__(self, max_iter=20, ncentroid=5):
		self.ncentroid = ncentroid
		self.max_iter = max_iter
		self.centroids = []

	def fit(self, X):
		if not isinstance(X, np.ndarray):
			return None
		pass

	def predict(self, X):
		if not isinstance(X, np.ndarray):
			return None
		"""
		Predict from wich cluster each datapoint belongs to.
		Args:
		-----
		X: has to be an numpy.ndarray, a matrice of dimension m * n.
		Return:
		-------
		the prediction has a numpy.ndarray, a vector of dimension m * 1.
		Raises:
		-------
		This function should not raise any Exception.
		"""
		pass
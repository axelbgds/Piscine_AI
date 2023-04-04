import matplotlib.pyplot as plt
import numpy as np
import os

class ImageProcessor:
	def __init__(self):
		pass

	def load(self, path):
		if not (path.endswith('.png') and os.path.exists(path)):
			print("Error: Please put a path for a valid existing png file")
			return None
		try:
			res = plt.imread(path)
		except:
			print("Error while reading image file")
		print("Dimension info: {} x {}".format(res.shape[0], res.shape[1]))
		return res

	def display(self, array):
		if not type(array) == np.ndarray:
			print("Error: Not valid image data")
			return
		try:
			plt.imshow(array)
			plt.show()
		except:
			print("Error while displaying image data")
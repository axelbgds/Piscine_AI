import numpy as np

class ColorFilter:
	def __init__(self):
		pass

	def invert(self, array):
		res = np.copy(array)
		for row in res:
			for col in row:
				for i in range(3):
					col[i] = 1 - col[i]
		return res
			
	def to_blue(self, array):
		res = np.zeros((array.shape[0], array.shape[1], 2))
		print(array.shape)
		print(res.shape)
		for n in range(res.shape[0]):
			wait = np.copy(array[n][:,2:])
			print("wait", res[n].shape, wait.shape)
			check = np.dstack((res[n], wait))
			print(check.shape, array[n].shape)
		return res
		
	def to_green(self, array):
		pass

	def to_red(self, array):
		pass

	def to_celluloid(self, array):
		pass

	def to_grayscale(self, array, filter, **kwargs):
		pass
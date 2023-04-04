import numpy as np

class ScrapBooker:
	def __init__(self):
		pass

	def crop(self, array, dim, position=(0,0)):
		if not isinstance(array, np.ndarray):
			return None
		if not (isinstance(dim, tuple) and isinstance(dim[0], int) and isinstance(dim[1], int) and len(dim) == 2):
			return None
		if not (isinstance(position, tuple) and isinstance(position[0], int) and isinstance(position[1], int) and len(position) == 2):
			return None 

		return array[position[0] : position[0] + dim[0], position[1] : position[1] + dim[1]]

	def thin(self, array, n, axis):
		if not (isinstance(array, np.ndarray) and \
			isinstance(n, int) and -1 < n < array.shape[0 if axis == 0 else 1] and \
			axis in [0, 1]):
			return None
		return np.delete(array, n, axis)

	def juxtapose(self, array, n, axis):
		if not (isinstance(array, np.ndarray) and isinstance(n, int) and n  > 0 and axis in [0, 1]):
			return None
		res = np.copy(array)
		for _ in range(n - 1):
			res = np.concatenate((res, array), axis)
		return res

	def mosaic(self, array, dim): #TODO should be faster (check hstack, vstack, tile...)
		res = self.juxtapose(array, dim[0], 0)
		return self.juxtapose(res, dim[1], 1)
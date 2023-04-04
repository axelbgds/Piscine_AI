import numpy as np

class NumPyCreator:
	def __init__(self):
		pass

	def from_list(self, lst):
		return np.array(lst) if isinstance(lst, list) else None #and all(len(elem) == len(elem[0]) for elem in lst)  

	def from_tuple(self, tpl):
		return np.array(tpl) if isinstance(tpl, tuple) else None

	def from_iterable(self, itr):
		return np.array(itr) if hasattr(itr, "__iter__") else None

	def from_shape(self, shape, value=0):
		return np.full(shape, value)

	def random(self, shape):
		return np.random.rand(shape[0], shape[1])

	def identity(self, n):
		return np.identity(n)
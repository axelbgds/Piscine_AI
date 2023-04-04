class Matrix:
	def __init__(self, init):
		if isinstance(init, list):
			self.data = init
			self.shape = (len(init), len(init[0]))
		elif isinstance(init, tuple) and len(init) == 2:
			self.data = [[0] * init[1]] * init[0]
			self.shape = init
		else:
			print("Wrong argument for initialization")

	def T(self):
		# return [[self.data[row][col] for row in range(self.shape[0])] for col in range(self.shape[1])]
		return Matrix([[self.data[row][col] for row in range(self.shape[0])] for col in range(self.shape[1])])

	def __add__(self, other):
		if self.shape != other.shape:
			return None
		return [[self.data[row][col] + other.data[row][col] for col in range(self.shape[1])] for row in range(self.shape[0])]

	def __radd__(self, other):
		return self.__add__(other)

	def __sub__(self, other):
		if self.shape != other.shape:
			return None
		return [[self.data[row][col] - other.data[row][col] for col in range(self.shape[1])] for row in range(self.shape[0])]

	def __rsub__(self, other):
		if self.shape != other.shape:
			return None
		return [[other.data[row][col] - self.data[row][col] for col in range(self.shape[1])] for row in range(self.shape[0])]

	def __truediv__(self, other):
		pass

	def __rtruediv__(self, other):
		pass

	def __mul__(self, other):
		if isinstance(other, float) or isinstance(other, int):
			return [[self.data[row][col] * other for col in range(self.shape[1])] for row in range(self.shape[0])]
		elif isinstance(other, Matrix) or isinstance(other, Vector):
			print("hello")
			if self.shape[1] != other.shape[0]:
				return None
			return [[sum([self.data[m][x] * other.data[x][n] for x in range(self.shape[1])])
				for n in range(other.shape[1])] for m in range(self.shape[0])]
		else:
			return None

	def __rmul__(self, other):
		pass

	def __str__(self):
		pass

	def __repr__(self):
		pass

class Vector(Matrix):
	def __init__(self):
		pass

	def dot(self, v):
		if self.shape[1] != v.shape[0]:
			print("Dot func error: vector shape doesn't match")
			exit()
		return sum(self.data[0][n] * v.data[n][0] for n in range(self.shape[1]))

xx = Matrix([[1, 1, 1, 9, 11], [7, 7, 7, 3, 4]])
yy = Matrix([[2, 5, 8], [1, 9 ,13], [2, 5, 8], [7, 7, 7], [1, 5, 5]])

print(xx.data, xx.shape)
print(yy.data, yy.shape)
print(xx * yy)
print(xx.T().data, xx.T().shape)

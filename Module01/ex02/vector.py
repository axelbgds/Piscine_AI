import sys

class Vector:
	def __init__(self, arg):
		if not (isinstance(arg, list) or isinstance(arg, int) or isinstance(arg, tuple)):
			sys.exit("Error! Wrong type for class init parameter")
		
		if isinstance(arg, list):
			if not len(arg):
				sys.exit("Error! Check your vector")
			if len(arg) > 1:
				if not all(isinstance(elem, list) and len(elem) == 1 and isinstance(elem[0], float) for elem in arg):
					sys.exit("Error! Check your vector")
				self.values = arg
				self.shape = (len(arg), 1)
			else:
				if not (all(isinstance(elem, float) for elem in arg[0]) and len(arg[0])):
					sys.exit("Error! Check your vector")
				self.values = arg
				self.shape = (1, len(arg[0]))
		elif isinstance(arg, int):
			if arg < 2:
				sys.exit("Error! Check your vector size")
			self.values = [[float(n)] for n in range(arg)]
			self.shape = (arg, 1)
		else:
			if not (len(arg) == 2 and isinstance(arg[0], int) and isinstance(arg[1], int) and arg[0] <= arg[1]):
				sys.exit("Error! Check your vector range")
			self.values = [[float(n) for n in range(arg[0], arg[1])]]			
			self.shape = (len(self.value), 1)

	def dot(self, other):
		if self.shape != other.shape:
			return
		return sum(self.values[0][n] * other.values[0][n] for n in range(self.shape[1])) \
			if self.shape[0] == 1 \
			else sum(self.values[n][0] * other.values[n][0] for n in range(self.shape[0]))

	def T(self):
		return Vector([[vec] for vec in self.values[0]] \
			if self.shape[0] == 1 \
			else [[vec[0] for vec in self.values]])

	def __add__(self, other):
		if self.shape != other.shape:
			return
		return Vector([self.values[0][n] + other.values[0][n] for n in range(self.shape[1])] \
			if self.shape[0] == 1 \
			else [[self.values[n][0] + other.values[n][0] for n in range(self.shape[0])]])		

	def __radd__(self, other):
		if self.shape != other.shape:
			return
		return Vector([other.values[0][n] + self.values[0][n] for n in range(self.shape[1])] \
			if self.shape[0] == 1 \
			else [[other.values[n][0] + self.values[n][0] for n in range(self.shape[0])]])

	def __sub__(self, other):
		if self.shape != other.shape:
			return
		return Vector([self.values[0][n] - other.values[0][n] for n in range(self.shape[1])] \
			if self.shape[0] == 1 \
			else [[self.values[n][0] - other.values[n][0] for n in range(self.shape[0])]])

	def __rsub__(self, other):
		if self.shape != other.shape:
			return
		return Vector([other.values[0][n] - self.values[0][n] for n in range(self.shape[1])] \
			if self.shape[0] == 1 \
			else [[other.values[n][0] - self.values[n][0] for n in range(self.shape[0])]])

	def __mul__(self, scalar):
		if not (isinstance(scalar, int) or isinstance(scalar, float)):
			print("NotImplementedError")
			return
		return Vector([self.values[0][n] * scalar for n in range(self.shape[1])] \
			if self.shape[0] == 1 \
			else [[self.values[n][0] * scalar for n in range(self.shape[0])]])

	def __rmul__(self, scalar):
		if not (isinstance(scalar, int) or isinstance(scalar, float)):
			print("NotImplementedError")
			return
		return Vector([scalar * self.values[0][n] for n in range(self.shape[1])] \
			if self.shape[0] == 1 \
			else [[scalar * self.values[n][0] for n in range(self.shape[0])]])

	def __truediv__(self, scalar):
		if not (isinstance(scalar, int) or isinstance(scalar, float)):
			return print("NotImplementedError")
		if scalar == 0:
			return print("DivisionByZero")
		return Vector([self.values[0][n] / scalar for n in range(self.shape[1])] \
			if self.shape[0] == 1 \
			else [[self.values[n][0] / scalar for n in range(self.shape[0])]])
	
	def __rtruediv__(self, scalar):
		return print("NotImplementedError (Division of a scalar by a Vector is not defined here.)")

	def __str__(self):
		return "\n".join(["Vector Type: " + ("column" if self.shape[0] == 1 else "row"),
			"Vector Size: " + (str(self.shape[1]) if self.shape[0] == 1 else str(self.shape[0])),
			"Vector: " + str(self.values)])

	def __repr__(self):
		return "\n".join(["Vector Type: " + ("column" if self.shape[0] == 1 else "row"),
			"Vector Size: " + (str(self.shape[1]) if self.shape[0] == 1 else str(self.shape[0])),
			"Vector: " + str(self.values)])

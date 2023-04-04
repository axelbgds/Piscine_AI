def simple_predict(x, theta):
	print(x.shape)
	print(len(x.shape))
	if x.size == 0 or x.shape[1] != 1 or theta.shape != (2, 1):
		return None
	return [theta[0] + theta[1] * v for v in x]


import numpy as np
x = np.arange(1,6)
print(x)
# Example 1:
theta1 = np.array([5, 0])
simple_predict(x, theta1)
# Ouput:
# array([5., 5., 5., 5., 5.])
# Do you understand why y_hat contains only 5’s here?
# Example 2:
theta2 = np.array([0, 1])
simple_predict(x, theta2)
# Output:
# array([1., 2., 3., 4., 5.])
# Do you understand why y_hat == x here?
# Example 3:
theta3 = np.array([5, 3])
simple_predict(x, theta3)
# Output:
# array([ 8., 11., 14., 17., 20.])
# Example 4:
theta4 = np.array([-3, 1])
simple_predict(x, theta4)
# Output:
# array([-2., -1., 0., 1., 2.])
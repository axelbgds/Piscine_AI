import numpy as np
import matplotlib.pyplot as plt
import pylab

def plot(x, y, theta):
	# if x.ndim() != 1 or y.ndim() != 1 or theta.shape() != (2, 1):
	# 	return
	plt.plot(x, y, 'o')
	plt.plot(x, x * theta[1] + theta[0])
	pylab.show()

x = np.arange(1,6)
y = np.array([3.74013816, 3.61473236, 4.57655287, 4.66793434, 5.95585554])

theta1 = np.array([[4.5],[-0.2]])

plot(x, y, theta1)
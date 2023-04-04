import numpy as np
import pandas
from ridge import MyRidge

def unison_shuffled_copies(a, b):
	p = np.random.permutation(len(a))
	return a[p], b[p]

def data_spliter(x, y, proportion):
	shuffled = unison_shuffled_copies(x, y)
	testNb = int(x.shape[0] * proportion)
	splitX = np.vsplit(shuffled[0], [testNb, x.shape[0]])
	splitY = np.vsplit(shuffled[1], [testNb, x.shape[0]])
	return splitX[0], splitX[1], splitY[0], splitY[1]

def add_polynomial_features(x, power):
	if power < 2:
		return x
	vfunc = np.vectorize(lambda e, n : e ** n)
	res = np.copy(x)
	for n in range(2, power + 1):
		res = np.append(res, vfunc(x, n), axis=1)
	return res

if __name__ == "__main__":
	data_csv = np.array(pandas.read_csv("../assets/space_avocado.csv"))
	X = data_csv[:,1:4]
	Y = data_csv[:,4].reshape(-1, 1)
	trainX, testX, trainY, testY = data_spliter(X, Y, 0.8)

	thetas1 = np.array([150000, 4800, 160, 10000]).reshape(-1, 1)
	thetas2 = add_polynomial_features(thetas1, 3)
	
	test1 = MyRidge(thetas1)
	print("thetas1 before training ", test1.thetas)
	print("test1 loss at the beginning:", test1.loss_(testY, test1.predict(testX)))
	test1.fit_(trainX, trainY)
	print("thetas1 after training", test1.thetas)
	print("test1 loss aftr training", test1.loss_(testY, test1.predict(testX)))

	test2 = MyRidge(thetas1)
	print("test2 mse at the beginning:", test2.mse(testX, testY))
	test2.fit_(trainX, trainY)
	print("test2 mse aftr training", test2.mse(testX, testY))

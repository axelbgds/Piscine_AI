import numpy as np
import pandas
import sys
from my_logistic_regression import MyLogisticRegression as MyLR

def unison_shuffled_copies(a, b):
	p = np.random.permutation(len(a))
	return a[p], b[p]

def data_spliter(x, y, proportion):
	shuffled = unison_shuffled_copies(x, y)
	testNb = int(x.shape[0] * proportion)
	splitX = np.vsplit(shuffled[0], [testNb, x.shape[0]])
	splitY = np.vsplit(shuffled[1], [testNb, x.shape[0]])
	return splitX[0], splitX[1], splitY[0], splitY[1]

if __name__ == "__main__":
	if len(sys.argv) != 2:
		sys.exit("usage: python3 mono_log.py -zipcode=<put zip code here (between 0-3)>" if len(sys.argv) == 1 else "accepts only one argument")
	if sys.argv[1].startswith("-zipcode=") == False or len(sys.argv[1]) < 10 or \
		sys.argv[1].split('=')[1].isdigit() == False or \
		(0 <= int(sys.argv[1].split('=')[1]) <= 3) == False:
		sys.exit("Error: wrong format of argument")
	
	planet_type = sys.argv[1].split('=')[1]
	
	X = np.array(pandas.read_csv("../assets/solar_system_census.csv"))[:,1:]
	Y = np.array(pandas.read_csv("../assets/solar_system_census_planets.csv"))[:,1:]
	
	# labelling again according to only one chosen class
	vfunc = np.vectorize(lambda x : 1 if x == planet_type else 0)
	neoY = vfunc(Y)
	# print(np.concatenate((Y, neoY), axis=1))

	# shuffle and split the dataset
	trainX, testX, trainY, testY = data_spliter(X, neoY, 0.8)

	# train my logistic model
	mylr = MyLR(np.array([1, 1, 1, 1]).reshape(-1, 1))
	mylr.fit_(testX, testY)

	# result of the training
	print(mylr.theta)
	# vfunc_round = np.vectorize(lambda x : round(x))
	# print(vfunc_round(mylr.predict_(testX)))
	print(mylr.loss_(testY, mylr.predict_(testX)))

	# plot the result
	mylr.plot_(testX[:,1], testY)

	#TODO visualization
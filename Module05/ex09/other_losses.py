import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from math import sqrt

def add_intercept(x):
	if x.ndim == 1:
		return [[1, elem] for elem in x]
	else:
		return np.insert(x, 0, 1, 1)

def loss(y, y_hat):
	cost = y - y_hat
	return np.dot(cost, cost) / cost.shape[0]

# Mean Squared Error
def mse_(y, y_hat):
	cost = y - y_hat
	return np.dot(cost, cost) / cost.shape[0]

# Root Mean Squared Error
def rmse_(y, y_hat):
	return sqrt(mse_(y, y_hat))

# Mean Absolute Error
def mae_(y, y_hat):
	return sum(x for x in np.absolute(y - y_hat)) / y.shape[0]

# R-squared / Coefficient Determination
def r2score_(y, y_hat):
	cost = y - y_hat
	diff_mean = y - np.mean(y)
	
	return 1 - (np.dot(cost, cost) / np.dot(diff_mean, diff_mean))

x = np.array([0, 15, -9, 7, 12, 3, -21])
y = np.array([2, 14, -13, 5, 12, 4, -19])
print(mse_(x,y), mean_squared_error(x,y))
print(rmse_(x,y), sqrt(mean_squared_error(x,y)))
print(mae_(x,y), mean_absolute_error(x,y))
print(r2score_(x,y), r2_score(x,y))
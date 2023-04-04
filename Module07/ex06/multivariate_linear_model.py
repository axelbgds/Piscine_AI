import pandas as pd
import numpy as np
from mylinearregression import MyLinearRegression as MyLR

data = pd.read_csv("../assets/spacecraft_data.csv")
X_Age = np.array(data[['Age']])
X_TPwr = np.array(data[['Thrust_power']]).reshape(-1, 1)
X_Teram = np.array(data['Terameters']).reshape(-1, 1)
X = np.array(data[['Age', 'Thrust_power', 'Terameters']])
Y = np.array(data[['Sell_price']])

# Univariate
# # Age column
# myLR_age = MyLR(thetas = [[1000.0], [-1.0]], alpha = 4.5e-5, max_iter = 500000)
# myLR_age.fit_(X_Age, Y)
# print(myLR_age.mse(X_Age, Y))
# myLR_age.plot(X_Age, Y)

# # Thrust Power column
# myLR_tpwr = MyLR(thetas = [[600.0], [10.0]], alpha = 2.5e-5, max_iter = 100000)
# myLR_tpwr.fit_(X_TPwr, Y)
# print(myLR_tpwr.mse(X_TPwr, Y))
# myLR_tpwr.plot(X_TPwr, Y)

# # Terameters column
# myLR_teram = MyLR(thetas = [[1000.0], [-25.0]], alpha = 2.5e-5, max_iter = 100000)
# myLR_teram.fit_(X_Teram, Y)
# print(myLR_teram.mse(X_Teram, Y))
# myLR_teram.plot(X_Teram, Y)

# Multivariate Model
myLR_xx = MyLR(thetas=np.array([[1.0], [1.0], [1.0], [1.0]]), alpha=6e-5, max_iter=600000)
print(myLR_xx.mse(X, Y))

myLR_xx.fit_(X, Y)
print(myLR_xx.thetas)
print(myLR_xx.mse(X, Y))
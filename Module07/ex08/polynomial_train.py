import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from mylinearregression import MyLinearRegression as MyLR

def add_polynomial_features(x, power):
	for n in range(power - 1):
		x = np.append(x, (x[:,0] * x[:,-1]).reshape(-1, 1), axis=1)
	return x


data = pd.read_csv("../assets/are_blue_pills_magics.csv")
X = np.array(data[["Micrograms"]])
Y = np.array(data[["Score"]])
continuous_x = np.arange(1, 10.01, 0.01).reshape(-1,1)
print(add_polynomial_features(X, 3))

lr_poly1 = MyLR(np.ones(2).reshape(-1, 1), alpha=8e-5, max_iter=300000)
lr_poly1.fit(X, Y)
mse1 = lr_poly1.mse(X, Y)
print("mse1: ", mse1)

lr_poly2 = MyLR(np.ones(3).reshape(-1, 1), alpha=8e-5, max_iter=300000)
X2 = add_polynomial_features(X, 2)
lr_poly2.fit(X2, Y)
mse2 = lr_poly2.mse(X2, Y)
print("mse2: ", mse2)

lr_poly3 = MyLR(np.ones(4).reshape(-1, 1), alpha=8e-5, max_iter=300000)
X3 = add_polynomial_features(X, 3)
lr_poly3.fit(X3, Y)
mse3 = lr_poly3.mse(X3, Y)
y_hat = lr_poly3.predict(X3)
print("mse3: ", mse3)

plt.scatter(X, Y)
plt.plot(X, y_hat, color="orange")
plt.show()

# lr_poly4 = MyLR(np.ones(5).reshape(-1, 1), alpha=2e-7)
# X4 = add_polynomial_features(X, 4)
# lr_poly4.fit(add_polynomial_features(X, 4), Y)
# mse4 = lr_poly4.mse(X4, Y)

# lr_poly5 = MyLR(np.ones(6).reshape(-1, 1), alpha=8e-5)
# X5 = add_polynomial_features(X, 5)
# lr_poly5.fit(add_polynomial_features(X, 5), Y)
# mse5 = lr_poly5.mse(X5, Y)

# lr_poly6 = MyLR(np.ones(7).reshape(-1, 1), alpha=8e-5)
# X6 = add_polynomial_features(X, 6)
# lr_poly6.fit(add_polynomial_features(X, 6), Y)
# mse6 = lr_poly6.mse(X6, Y)

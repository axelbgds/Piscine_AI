import numpy as np

def zscore(x):
	vfunc = np.vectorize(lambda e : (e - np.mean(x)) / np.std(x))
	return vfunc(x)

# Example 1:
X = np.array([0, 15, -9, 7, 12, 3, -21])
print(zscore(X))
# Output:
# array([-0.08620324, 1.2068453 , -0.86203236, 0.51721942, 0.94823559,
# 0.17240647, -1.89647119])
Y = np.array([2, 14, -13, 5, 12, 4, -19]).reshape((-1, 1))
print(zscore(Y))
# Output:
# array([ 0.11267619, 1.16432067, -1.20187941,
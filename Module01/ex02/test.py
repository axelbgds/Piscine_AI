from vector import Vector

test1 = Vector([[5., 5., 5.]])
test2 = Vector([[3.], [6.], [9.]])
test3 = Vector([[4.], [8.], [12.]])

print(str(test2))
print(test1 + test2)
print(test1.T() + test2)
print(test3 * 4)
print(test3 / 4)
print(test2.dot(test3))
3 / test2
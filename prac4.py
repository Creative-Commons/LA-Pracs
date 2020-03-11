import numpy as np

a = np.array([0, 4, 6])
b = np.array([[1, 2], [4, 9], [-1, -10]])
print(np.dot(a, b))

x = np.array([[3, 2, 2], [4, 2, 5], [7, 2, 7]])
y = np.array([[5, 3, 1, 2], [1, 7, 3, 0], [2, 5, 2, 1]])
mul = np.array([[0,0,0,0] for x in range(len(y))])

for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            mul[i][j] += x[i][k] * y[k][j]

print(mul)


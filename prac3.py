import numpy as np

m = np.array([[1, 2, 3], [4, 3, 2], [6, 9, 7]])
print(m)

print("Column: \n")
for i in range(1, 4):
    print(m[:,0:i])

print("Rows: \n")
for i in range(1, 4):
    print(m[0:i])

print("Scalar Multiplication: \n", 5 * m)




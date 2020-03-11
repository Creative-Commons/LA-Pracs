import numpy as np

A = np.mat("3 -2; 1 0")

print("A\n", A)
print("Eigen Values ", np.linalg.eigvals(A))
print("\n")
eigenValues, eigenVectors = np.linalg.eig(A)
print("First tuple of Eigen values: ", eigenValues)
print("Second tuple of Eigen Vectors: ", eigenVectors)
print("\n")
u = eigenVectors[:,0]
print("u: ",u)
lam = eigenValues[0]
print("lam: ", lam, "\n")

print("np.dot(A, u): \n", np.dot(A, u), "\n")
print("lam * u: \n",lam * u)


print(eigenVectors)
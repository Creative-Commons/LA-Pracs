import numpy as np

u, v = np.array([3, 4, 5]), np.array([1, 2, 7])
print("u:\n", u, "\nv:\n", v)

a, b = int(input()), int(input())
d = (a * u) + (b * v)
print("au+bv: ",d)

p = np.dot(u, v)
print("Dot product: ", p)


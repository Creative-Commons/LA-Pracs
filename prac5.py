import numpy as np

m = np.array([[1,2,3],[2,1,3],[3,2,1]])
print(m)

if np.linalg.det(m) == 0:
    print("Non invertible matrix")
else:
    print(np.linalg.inv(m))
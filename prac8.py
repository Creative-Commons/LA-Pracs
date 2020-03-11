import numpy as np

def projection(of_vect, on_vect):
    v1, v2 = np.array(of_vect), np.array(on_vect)
    scal = np.dot(v1, v2) / np.dot(v1, v1)
    vec = scal * v1
    return round(scal, 10), np.around(vec, decimals=10)

print(projection([4.0, 4.0], [1.0, 0.0]))
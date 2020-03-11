import matplotlib.pyplot as plt

# 1
x, p = int(input("Enter real part of 1st complex no: ")), int(input("Enter imag part of 1st complex no: "))
y, q = int(input("Enter real part of 2st complex no: ")), int(input("Enter imag part of 2st complex no: "))

result = complex(x, p) + complex(y, q)
print(result)

# 2
print(complex(x,y).conjugate())

# 3
'''
a = [-2+4j, -1+2j, 0+2j, 1+2j, 2+2j, -1+4j, 0+4j, 1+4j]
x, y = [x.real for x in a], [y.real for y in a]
plt.scatter(x, y, color="red")
plt.show()
'''

# 4
a = 2 + 4j; b = 1j

plt.scatter(x.real, x.imag, color="blue")
e = a * b
plt.scatter(e.real, e.imag)
plt.show()

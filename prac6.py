import numpy as np

# Find GCD using Euclid's Algorithm

def gcd(a, b):
    if b > a:
        if b % a == 0:
            return a
        else:
            return gcd(b % a, a)
    else:
        if a % b == 0:
            return b
        else:
            return gcd(a % b, b)

print(gcd(512, 256))


# Enter N. find a & b such that a^2 - b^2 = N
N = 36; a = 77; b = 4
x = (a + b)/2; y = (a -b)/2
a2 = x**2; b2 = y**2

if N == (a2 - b2):
    print("Satisfied")
else:
    print("Not Satisfied")
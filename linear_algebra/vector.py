import numpy as np

u = list(map(int, input("Enter values: ").split()))
v = list(map(int, input("Enter values: ").split()))

a = np.array(u)
b = np.array(v)

# Dot Product
print(np.dot(a, b))

# Cross Product
print(np.cross(a, b))

# Scaler multiplication
print(3*a)

# Vector Addition
print(a + b)

# Vecor Substarction
print(a - b)

import numpy as np

u = np.array(list(map(int, input("Enter first vector: ").split())))
v = np.array(list(map(int, input("Enter second vector: ").split())))

# Dot product
dot = np.dot(u, v)

# Magnitudes
mag_u = np.linalg.norm(u)
mag_v = np.linalg.norm(v)

# Angle in radians
angle_rad = np.arccos(dot / (mag_u * mag_v))

# Convert to degrees
angle_deg = np.degrees(angle_rad)

print("Dot Product =", dot)
print("Magnitude of u =", mag_u)
print("Magnitude of v =", mag_v)
print("Angle (Radians) =", angle_rad)
print("Angle (Degrees) =", angle_deg)
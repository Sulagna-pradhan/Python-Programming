import math


# CONSTANTS
print(math.pi)        # 3.141592653589793 - Value of π
print(math.e)         # 2.718281828... - Euler's number
print(math.tau)       # 6.283185307... - 2 × π
print(math.inf)       # Infinity
print(math.nan)       # Not a Number (NaN)

# ROUNDING FUNCTIONS
print(math.ceil(4.2))      # 5 - Round UP
print(math.floor(4.8))     # 4 - Round DOWN
print(math.trunc(4.9))     # 4 - Remove decimal part
print(math.fabs(-5.6))     # 5.6 - Absolute value (always float)

# POWER & ROOT
print(math.sqrt(25))       # 5.0 - Square root
print(math.pow(2, 5))      # 32.0 - 2 raised to power 5
print(math.isqrt(17))      # 4 - Integer square root
print(math.cbrt(27))       # 3.0 - Cube root (Python 3.11+)

# LOGARITHMS & EXPONENTIAL
print(math.exp(2))         # e²
print(math.log(100, 10))   # Log base 10 of 100
print(math.log10(1000))    # Base-10 logarithm
print(math.log2(16))       # Base-2 logarithm

# NUMBER THEORY
print(math.factorial(5))   # 120 - 5!
print(math.gcd(24, 36))    # 12 - Greatest Common Divisor
print(math.lcm(12, 18))    # 36 - Least Common Multiple
print(math.comb(5, 2))     # 10 - nCr (Combination)
print(math.perm(5, 2))     # 20 - nPr (Permutation)

# TRIGONOMETRY
# (All angles must be in radians)
angle = math.radians(60)   # Convert 60° to radians
print(math.sin(angle))     # Sine
print(math.cos(angle))     # Cosine
print(math.tan(angle))     # Tangent

# INVERSE TRIGONOMETRY
# (Result is in radians)
print(math.asin(1))        # sin⁻¹(1)
print(math.acos(1))        # cos⁻¹(1)
print(math.atan(1))        # tan⁻¹(1)

# ANGLE CONVERSION
print(math.radians(180))   # Convert degrees - radians
print(math.degrees(math.pi))  # Convert radians - degrees

# HYPERBOLIC FUNCTIONS
print(math.sinh(1))        # Hyperbolic sine
print(math.cosh(1))        # Hyperbolic cosine
print(math.tanh(1))        # Hyperbolic tangent

# DISTANCE & GEOMETRY
print(math.hypot(3, 4))          # 5.0 - Hypotenuse
print(math.dist([0, 0], [3, 4])) # 5.0 - Distance between two points


# FLOATING-POINT UTILITIES
print(math.fmod(17, 5))          # Floating-point remainder
print(math.remainder(17, 5))     # IEEE remainder
print(math.modf(4.75))           # (0.75, 4.0) - Fractional & Integer parts
print(math.copysign(5, -2))      # -5.0 - Copy sign of second number

# CHECKING NUMBERS
print(math.isfinite(10))         # True - Is finite?
print(math.isinf(math.inf))      # True - Is infinity?
print(math.isnan(math.nan))      # True - Is NaN?
print(math.isclose(0.1 + 0.2, 0.3))  # True - Compare floating-point numbers

# PRODUCT & ACCURATE SUM
print(math.prod([2, 3, 4]))      # 24 - Multiply all elements
print(math.fsum([0.1, 0.2, 0.3]))# Accurate floating-point sum

# EXTRA USEFUL FUNCTIONS
print(math.frexp(16))
# Returns (0.5, 5)
# Number represented as: 0.5 × 2^5

print(math.ldexp(0.5, 5))
# Returns 16.0
# Opposite of frexp()

print(math.nextafter(1.0, 2.0))
# Next representable float after 1.0 towards 2.0

print(math.ulp(5.0))
# Smallest possible increment at 5.0


# EXAMPLES

radius = 7
area = math.pi * radius ** 2
print(area)                     # Area of circle

a = 3
b = 4
print(math.hypot(a, b))         # Hypotenuse

print(math.factorial(6))        # 720

print(math.gcd(100, 80))        # 20

print(math.lcm(8, 12))          # 24

print(math.sqrt(144))           # 12.0

print(math.pow(3, 4))           # 81.0

print(math.log2(64))            # 6.0

print(math.sin(math.radians(90)))   # 1.0

print(math.cos(math.radians(180)))  # -1.0
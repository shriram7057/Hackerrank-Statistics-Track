import math

# Read inputs
n = int(input())
mean = float(input())
std = float(input())
confidence = float(input())
z = float(input())

# Standard error
standard_error = std / math.sqrt(n)

# Confidence interval
lower = mean - z * standard_error
upper = mean + z * standard_error

# Output
print(round(lower, 2))
print(round(upper, 2))

import math

# Read input
mean, std = map(float, input().split())
x1 = float(input())
x2 = float(input())

# Normal CDF function
def normal_cdf(x, mean, std):
    return 0.5 * (1 + math.erf((x - mean) / (std * math.sqrt(2))))

# Calculations
greater_than_80 = (1 - normal_cdf(x1, mean, std)) * 100
passed = (1 - normal_cdf(x2, mean, std)) * 100
failed = normal_cdf(x2, mean, std) * 100

# Output
print(f"{greater_than_80:.2f}")
print(f"{passed:.2f}")
print(f"{failed:.2f}")

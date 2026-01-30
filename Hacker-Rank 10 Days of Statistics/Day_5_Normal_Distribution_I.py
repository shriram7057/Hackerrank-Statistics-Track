import math

# Read inputs
mean, std = map(float, input().split())
x1 = float(input())
x2, x3 = map(float, input().split())

# Normal distribution CDF
def normal_cdf(x, mean, std):
    return 0.5 * (1 + math.erf((x - mean) / (std * math.sqrt(2))))

# Calculations
p1 = normal_cdf(x1, mean, std)
p2 = normal_cdf(x3, mean, std) - normal_cdf(x2, mean, std)

# Output results
print(f"{p1:.3f}")
print(f"{p2:.3f}")

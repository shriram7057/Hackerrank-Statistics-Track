import math

# Read inputs
max_weight = float(input())
n = int(input())
mean = float(input())
std = float(input())

# Mean and standard deviation of the total weight
total_mean = n * mean
total_std = math.sqrt(n) * std

# Z-score
z = (max_weight - total_mean) / total_std

# CDF of standard normal distribution
probability = 0.5 * (1 + math.erf(z / math.sqrt(2)))

# Output rounded to 4 decimal places
print(round(probability, 4))

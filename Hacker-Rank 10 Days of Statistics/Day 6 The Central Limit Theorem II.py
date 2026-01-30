import math

# Read inputs
tickets = float(input())
students = int(input())
mean = float(input())
std = float(input())

# Mean and standard deviation of total demand
total_mean = students * mean
total_std = math.sqrt(students) * std

# Z-score
z = (tickets - total_mean) / total_std

# Standard normal CDF
probability = 0.5 * (1 + math.erf(z / math.sqrt(2)))

# Output rounded to 4 decimal places
print(round(probability, 4))

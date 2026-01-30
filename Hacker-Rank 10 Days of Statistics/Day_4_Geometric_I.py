# Given values
numerator, denominator = 1, 3
p = numerator / denominator
k = 5

# Geometric distribution formula
probability = ((1 - p) ** (k - 1)) * p

# Print result rounded to 3 decimal places
print(f"{probability:.3f}")

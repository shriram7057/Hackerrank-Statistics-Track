# Given values
numerator, denominator = 1, 3
p = numerator / denominator
k = 5

# Cumulative geometric probability
probability = 1 - ((1 - p) ** k)

# Print result rounded to 3 decimal places
print(f"{probability:.3f}")

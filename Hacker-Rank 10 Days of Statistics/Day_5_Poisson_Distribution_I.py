import math

# Read inputs
lam = float(input().strip())
k = int(input().strip())

# Poisson probability formula
probability = (lam ** k) * math.exp(-lam) / math.factorial(k)

# Print result rounded to 3 decimal places
print(f"{probability:.3f}")

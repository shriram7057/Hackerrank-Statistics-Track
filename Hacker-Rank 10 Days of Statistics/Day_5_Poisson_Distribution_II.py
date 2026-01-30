# Read input
a, b = map(float, input().split())

# Expected cost calculations
cost_A = 160 + 40 * (a + a**2)
cost_B = 128 + 40 * (b + b**2)

# Print results rounded to 3 decimal places
print(f"{cost_A:.3f}")
print(f"{cost_B:.3f}")

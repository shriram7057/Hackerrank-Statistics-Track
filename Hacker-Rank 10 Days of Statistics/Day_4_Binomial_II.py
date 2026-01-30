import math

# Given values
p = 0.12   # probability of reject
q = 1 - p
n = 10

# Binomial probability function
def binomial(n, k, p):
    return math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

# No more than 2 rejects
prob_no_more_than_2 = sum(binomial(n, k, p) for k in range(0, 3))

# At least 2 rejects
prob_at_least_2 = 1 - sum(binomial(n, k, p) for k in range(0, 2))

# Print results rounded to 3 decimal places
print(f"{prob_no_more_than_2:.3f}")
print(f"{prob_at_least_2:.3f}")

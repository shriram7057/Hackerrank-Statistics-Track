import math

# Given ratio
boys_ratio = 1.09
girls_ratio = 1.0

# Probability of boy and girl
p = boys_ratio / (boys_ratio + girls_ratio)
q = 1 - p

# Number of children
n = 6

# Binomial probability function
def binomial_prob(n, k, p):
    return math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

# Probability of at least 3 boys
probability = sum(binomial_prob(n, k, p) for k in range(3, n + 1))

# Print result rounded to 3 decimal places
print(f"{probability:.3f}")

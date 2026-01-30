n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

# Assign ranks
rank_x = {value: rank + 1 for rank, value in enumerate(sorted(X))}
rank_y = {value: rank + 1 for rank, value in enumerate(sorted(Y))}

# Calculate sum of squared rank differences
d_squared_sum = 0
for i in range(n):
    d = rank_x[X[i]] - rank_y[Y[i]]
    d_squared_sum += d ** 2

# Spearman's rank correlation coefficient
rho = 1 - (6 * d_squared_sum) / (n * (n**2 - 1))

print(f"{rho:.3f}")

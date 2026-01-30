# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

mean_x = sum(X) / n
mean_y = sum(Y) / n

numerator = 0
denom_x = 0
denom_y = 0

for i in range(n):
    dx = X[i] - mean_x
    dy = Y[i] - mean_y
    numerator += dx * dy
    denom_x += dx ** 2
    denom_y += dy ** 2

r = numerator / math.sqrt(denom_x * denom_y)

print(f"{r:.3f}")

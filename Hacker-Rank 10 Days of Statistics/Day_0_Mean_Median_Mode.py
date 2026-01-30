# Read input
n = int(input().strip())
arr = list(map(int, input().split()))

# Mean
mean = sum(arr) / n

# Median
arr.sort()
if n % 2 == 0:
    median = (arr[n // 2 - 1] + arr[n // 2]) / 2
else:
    median = arr[n // 2]

# Mode
frequency = {}
for num in arr:
    frequency[num] = frequency.get(num, 0) + 1

max_freq = max(frequency.values())
mode = min([key for key, value in frequency.items() if value == max_freq])

# Print results
print(f"{mean:.1f}")
print(f"{median:.1f}")
print(mode)

x = [1, 2, 2, 5, 6, 8, 9]
n = len(x)
k = 10
for i in range(n):
    for j in range(i + 1, n):
        if (x[i] + x[j]) == k:
            print(x[i], x[j])
# pairs
# 1 9
# 2 8
# 2 8

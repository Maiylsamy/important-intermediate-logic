x = [43, 23, 56, 7, 8, 65, 45]
x1 = len(x)
for i in range(x1):
    for j in range(i + 1, x1):
        if x[i] > x[j]:
            x[i], x[j] = x[j], x[i]
print(x)

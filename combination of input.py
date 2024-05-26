x = 1
y = 2
z = 3
n = 3
l1 = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k) != n ]
print(l1)
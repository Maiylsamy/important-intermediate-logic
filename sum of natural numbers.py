n = int(input('enter a no:'))
x=0
for i in range(n+1):
    x += i
print(x)

print(n*(n+1)/2)#fromula

def sumofno(n):
    if n==0:
        return n
    return n + sumofno(n-1)
print(sumofno(n))

#while
s=0
x=1
while x<=n:
    s += x
    x +=1
print(s)
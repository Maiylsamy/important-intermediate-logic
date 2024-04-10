m = int(input('enter a no:'))
n = int(input('enter a no:'))
m1 = 0
n1 = 0
for i in range(1,m):
    if m%i==0:
        m1+=i
for j in range(1,n):
    if n%j==0:
        n1+=j
if (m%m1 == 0) == (n%n1 ==0):# m-6,n-28
    print('friendly pair numbers')
else:
    print('not a friendly pair numbers')
    

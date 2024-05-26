def feb_fun(n):
    if n <= 1:
        return n
    return feb_fun(n - 1) + feb_fun(n - 2)


n = int(input('enter a number :'))

if n <= 0:
    print('enter a positive number')

else:
    for i in range(n):
        print(feb_fun(i))

#for loop (fibonacci)
a,b= 0,1
n = int(input('enter a number :'))
l1 = [a,b]
for i in range(2,n):
    a,b = b ,a + b
    l1 += [b]
print(l1)

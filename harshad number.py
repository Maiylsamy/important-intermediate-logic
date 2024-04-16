# sum of the input value and diveded the input using sum value
n = int(input('enter a no:'))
l1=[int(i) for i in str(n)]
s = sum(l1)
if n%s==0:
    print('harshad number')
else:
    print('Not harshad number')

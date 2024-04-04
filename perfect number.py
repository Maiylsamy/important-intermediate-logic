n = int(input('enter a number:'))
divisor=[]
s =0
for i in range(1,n):
    if n%i==0:
        divisor += [i]
        s += i
print(divisor)
print(s)
if n == s:
    print('its perfect no')#28
else:
    print('its not perfect no')

def fact(n):
    if n == 0 :
        return 1
    return n * fact(n-1)
m =int(input('enter:'))
a = []
for i in str(m) :
    f = fact(int(i))
    a.append(f)
print(a)
x = sum(a)
print(x)
if m == x:
     print('strong no')#145
else:
    print('its not strong no')
n = int(input('enter a no:'))
l1 = 0
for i in range(1,n):
    if n % i == 0:
        l1 += i
if l1 >n:
    print('its abundant number')
else:
    print('its not abundant number')

# Number = 5
# Square of number = 25
# as the square of the number ends with the number itself, It's an Automorphic number.
n = int(input('enter a no:'))
square = pow(n,2)
mod = pow(10,len(str(n)))

if square%mod == n:
    print('automorphic number')
else:
    print('its not automorphic number')

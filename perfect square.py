from math import sqrt
# input value becames end of the output value eg: input 5 output 25

def sq(n):
    if n >= 0:
        s = int(sqrt(n))
        return (s * s) == n
    return False


m = int(input('enter a no:'))
if sq(m):
    print('perfect')
else:
    print('non perfect')

from math import sqrt


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

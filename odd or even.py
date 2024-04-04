n = int(input('enter a no:'))


def isEven(n):
    return not n & 1


if isEven(n):
    print('even number')
else:
    print('odd number')

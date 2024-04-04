def is_fibonacci(n):
    x, y = 0, 1
    while True:
        z = x + y
        if z == n:
            return True
        elif z > n:
            return False
        x, y = y, z

n = int(input('Enter a number: '))
if is_fibonacci(n):
    print(f"{n} is a Fibonacci number.")
else:
    print(f"{n} is not a Fibonacci number.")

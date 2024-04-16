# Number = 5
# Square of number = 25
# as the square of the number ends with the number itself, It's an Automorphic number.
i = int(input('enter a no'))
j =int( input('enter a no'))
for n in range(i,j):
    x = [int(i)**3 for i in str(n)]
    s=sum(x)
    if n == s:
        print(s)

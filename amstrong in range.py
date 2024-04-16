#  371 can also be represented as 3^3 + 7^3 + 1^3 therefore it's an Armstrong Number.
i = int(input('enter a no'))
j =int( input('enter a no'))
for n in range(i,j):
    x = [int(i)**3 for i in str(n)]
    s=sum(x)
    if n == s:
        print(s)

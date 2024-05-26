n=int(input('enter a number :'))
x = 2
count = 1
while count<=n:
    v= True
    if 1<x:
        for i in range(2,x):
            if x%i == 0 :
                v = False
                break
    else:
        print('its not prime')
    if v:

        count +=1

    x += 1
print(x-1)
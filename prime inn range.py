o = int(input('enter a m:'))
k= int(input('enter a m:'))
l1 = []
for m in range(o,k+1):
    v =1
    if m<2:
        v = 0
    else:
        for i in range(2,m):
            if m%i == 0:
                v = 0
                break;
    if v==1:
        l1 += [m]
print(l1)
x = [12,13,14,16,18,19,22]
# take first and last index
FI = x [0]
LI = x[-1]
#we need to create a list for store value create by range using  index
list1 = []
for i in range(FI,LI+1):
    list1 += [i]
#we go to check using conditional block
mis = []
for j in list1:
    if j not in x:
        mis += [j]
print('missed number is :',mis)

n = int(input('enter a no:'))
if n>=0:
    if n==0 :
        print('zero')
    else:
        print('positive')
else:
    print('negative')

print( 'positive ' if n>=0 else 'negative')
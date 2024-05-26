# key word short in dict
dict1 = {34: 'veult 9034', 42: 'vault 9042', 20: 'voult 9020'}
d = sorted(dict1.keys())
dict2 = {}
for i in d:
    dict2[i] = dict1[i]  # 34 = 'vault 9034'
print(dict2)

# alternative
# key word short in dict
for x, y in sorted(dict1.items()):
    print(x, y, end=' ')

# value based short in dict
val = {key: value for key, value in sorted(dict1.items(), key=lambda x: x[1])}
print(val)

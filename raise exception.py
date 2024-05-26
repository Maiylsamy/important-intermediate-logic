list1 = [2, 3, 4, 1, 5, 6]
for i in list1:
    if i == 1:
        raise Exception('expception : 1 is found')
    else:
        print(i, end=' ')
#   File "D:\PY\rough1.py", line 4, in <module>
#      raise Exception('expception : 1 is found')
# Exception: expception : 1 is found

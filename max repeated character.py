s = "manasawariimans"
ch = {}
for i in s:
    if i in ch:
        ch[i] += 1
    else:
        ch[i] = 1
max_char = max(ch, key=ch.get)
print(ch)
# {'m': 2, 'a': 5, 'n': 2, 's': 2, 'w': 1, 'r': 1, 'i': 2}
print(max_char)

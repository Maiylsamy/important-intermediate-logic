# remove special characters from string
str = " %i $$love$$ --you-- @maDlY!"
s = ''
for i in str:
    if ((i >= "A" and i <= "Z") | (i >= "a" and i <= "z") | (i == ' ') ):
        s += i
print(s)

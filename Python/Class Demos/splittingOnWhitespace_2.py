import string

ws = string.whitespace
s = 'abc def\tghi\njkl'

tmp = ''
for c in s:
    if c not in ws:
        tmp += c
    else:
        print (tmp)
        tmp = ''
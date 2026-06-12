from re import *

f = open('/Users/elizavetakulesova/Downloads/24_1255.txt').read()
pat = r'(?:((XY)*(ZZX)*)*)'
res = findall(pat, f)
s = []
for el in res:
    st = ''.join(el)
    s.append(len(st))
print(max(s))

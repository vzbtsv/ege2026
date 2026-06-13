from re import *

f = open('/Users/elizavetakulesova/Downloads/24_1255.txt').read()
pat = r'(?:XY|ZZX)*'
res = findall(pat, f)
print(max([len(x) for x in res]))

from re import *

f = open('/Users/elizavetakulesova/Downloads/24_7981.txt').read()
cnt = 0
ss = ['AA', 'AB', 'AC', 'BC', 'BA', 'BB', 'CC', 'CA', 'CB']
for i in range(len(f)):
    for j in range(i + 1, len(f)):
        if f[i] == f[j] and ('AA' not in f[i:j + 1] and 'AB' not in f[i:j + 1] and 'AC' not in f[i:j + 1] and 'BB' not in f[i:j + 1] and 'BA' not in f[i:j + 1] and 'BC' not in f[i:j + 1] and 'CC' not in f[i:j + 1] and 'CA' not in f[i:j + 1] and 'CA' not in f):
            cnt += 1
        if 'AA' in f[i:j + 1] or 'AB' in f[i:j + 1] or 'AC' in f[i:j + 1] or 'BB' in f[i:j + 1] or 'BA' in f[i:j + 1] or 'BC' in f[i:j + 1] or 'CC' in f[i:j + 1] or 'CA' in f[i:j + 1] or 'CA' in f:
            break

print(cnt)

f = open('/Users/elizavetakulesova/Downloads/26_2254.txt')
n, m = map(int, f.readline().split())
s = []
q = []
z = []
for line in f:
    cost, type = line.split()
    cost = int(cost)
    s.append([cost, type])
    if type == 'Q':
        q.append(cost)
    else:
        z.append(cost)
q.sort()
z.sort()
s.sort(key=lambda x: x[0])
suma = 0
i = 0
while suma < m:
    if suma + s[i][0] <= m:
        i += 1
        suma += s[i][0]
    else:
        break
k = i #k = 95
for i in range(k, 0, -1):
    # print(len(q[:i]) + len(z[:(k - i)]))
    itogsum = sum(q[:i]) + sum(z[:(k - i)])
    if itogsum <= m:
        print(i, m - itogsum)
        break

f = open('/Users/elizavetakulesova/Downloads/26_13292.txt')
n, k = map(int, f.readline().split())
s = []
for line in f:
    s.append(int(line))
s.sort()
spc = [0] * k
r = 0
l = k - 1
last = 0
print(n, k)
for i in range(k):
    if s[i] % 2 == 0:
        spc[r] = s[i]
        last = r + 1
        r += 1
    else:
        spc[l] = s[i]
        last = l + 1
        l -= 1
print(last)
last -= 1
flag = False
ans = 0
for i in range(len(spc)):
    if flag and spc[i] % 2 == 1:
        ans += spc[i]
    if i == last:
        flag = True
print(ans)
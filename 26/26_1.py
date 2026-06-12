



f = open("26_6056.txt").readlines()

n = int(f[0])

data = sorted([int(x) for x in f[1:]])[::-1]


res = []
res.append(data[0])

for x in data[1:]:
    if res[-1] - x >= 56:
        res.append(x)


print(data)
print(res)
print(len(res))


# 134 - 52 = 82





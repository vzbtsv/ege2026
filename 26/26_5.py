f = open("26_2717.txt").readlines()

n = int(f[0])

data = sorted([list(map(int, x.split())) for x in f[1:]])
d = {}

for x in data:
    row, seat = x

    if row in d.keys():
        d[row].append(seat)

    else:
        d[row] = [seat]


def p1(x):
    for i in range(len(x) - 1):
        x1 = x[i]
        x2 = x[i + 1]
        if (x2 - x1 - 1) >= 3:
            return False

    return True


for x in d:
    r = sorted(d[x])
    if len(r) >= 5:
        if p1(r):
            print(x, r)



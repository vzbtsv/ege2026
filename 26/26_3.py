

f = open("26_17643.txt").readlines()


n = int(f[0])


data = [list(map(int, x.split())) for x in f[1:]]

mid_price = sum([x[1] for x in data]) / n
print(mid_price)

d = {}

for x in data:
    article, price, status = x
    if price > mid_price:
        if article not in d.keys():
            d[article] = [price, status, (1 - status)]

        else:
            d[article][1] += status
            d[article][2] += (1 - status)




d = d.items()

res = sorted(d, key=lambda x: (x[1][2], x[1][0], -x[1][1]))[-1]

print(res[1][0] * res[1][2], res[1][1])
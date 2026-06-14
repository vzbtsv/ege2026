

f = open("24_2508.txt").readlines()

f = sorted(f, key=lambda x: x.count("Q"))
right = f[-1]
print(f[-1].count("Q"))

alp = "qwertyuiopasdfghjklzxcvbnm".upper()

res = []
for a in alp:
    res.append((right.count(a), a))


print(min(res))

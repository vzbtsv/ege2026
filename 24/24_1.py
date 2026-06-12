import re

f = open("24_12476.txt").read()


f = f.split("RO")
maxx = "0"
for i in range(len(f) - 1):
    for j in range(1, 23):
        st = "RO".join(f[i:i + j])
        if "ORO" not in st and "ROR" not in st:
            maxx = max(maxx, st, key=len)



print(maxx.count("RO"))
print(len(maxx))


import re

f = open("24_7853 (1).txt").read()

p1 = r"[^NOT]"
f = re.sub(p1, "0", f)

p2 = r"[NOT]"
f = re.sub(p2, "1", f)

# pat = r"0*(?:10{2,}|11)*0*"
#
# res = re.findall(pat, f)
#
# print(len(max(res, key=len)))
maxx = 0
for i in range(len(f)):
    for j in range(i + maxx, len(f)):
        st = f[i:j]

        if "101" not in st:
            maxx = max(len(st), maxx)
            print(maxx)

        else:
            break

print(maxx)
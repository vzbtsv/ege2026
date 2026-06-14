import re

f = open("24_7981.txt").read()
print(len(f))
p1 = r"[^ABC]"
p2 = r"[ABC]"
# f = re.sub(p1, "0", f)
# f = re.sub(p2, "1", f)

k = 0
for i in range(len(f)):
    for j in range(i + 2, len(f) + 1):
        st = f[i:j]
        if st[0] == st[-1]:
            st = re.sub(p2, "1", st)
            if "11" not in st:
                k += 1

            else:
                break

print(k)



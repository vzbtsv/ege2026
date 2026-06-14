import re

f = open("24_26491 (1).txt").read()

# number = r"(?:[1-9][0-9]*)"
#
# pat = rf"{number}(?:[+*]{number})*"
#
# res = re.findall(pat, f)
# maxx = 0
# for x in res:
#     for i in range(len(x)):
#         for j in range(len(x), i, -1):
#             st = x[i:j]
#             try:
#                 if eval(st) % 2 == 0:
#                     maxx = max(maxx, len(st))
#                     break
#
#             except Exception:
#                 pass

maxx = 0
for i in range(len(f)):
    for j in range(i + maxx, len(f)):
        st = f[i:j+1]
        if ("**" in st) or ("++" in st) or ("*+" in st) or ("*+" in st):
            break

        try:
            if eval(st) % 2 == 0:
                maxx = max(maxx, len(st))

        except Exception:
            break

print(maxx)

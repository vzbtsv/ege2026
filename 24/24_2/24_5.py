import re

f = open("24_19970.txt").read()


number = r"([1-9][0-9]*[05]|0)"

pat = rf"{number}(?:[+*]{number})*"


# res = re.findall(pat, f)
#
# print(res)
# print(len(max(res, key=len)))



res = re.finditer(pat, f)

for i in res:
    print(i.group())
    print(i.start())

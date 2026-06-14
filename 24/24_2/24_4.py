import re

f = open("24_1352.txt").read()


pat = r"[XYZ](?:XYZ)*[XYZ]"


res = re.findall(pat, f)


print(len(max(res, key=len)))
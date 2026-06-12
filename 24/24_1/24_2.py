import re

f= open("24_18937.txt").read()

number = r"(?:[1-9][0-9]*|0)"

pat = rf"{number}(?:[+*]{number})*"

res = re.findall(pat, f)

print(len(max(res, key=len)))
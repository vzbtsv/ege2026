f = open("24_1255.txt").readlines()


def r1(s):
    alp = "qwertyuiopasdfghjklzxcvbnm".upper()
    res = []

    for a in alp:
        res.append(s.rindex(a) - s.index(a) + 1)

    return res


for st in f:
    if st.count("A") < 25:
        r1(st)
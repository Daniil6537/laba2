def s(l):
    if 0 < len(l):
        return l[0] + s(l[1:])
    return 0


def m(l, mn):
    if len(l)>0:
        if mn>l[0]:
            return m(l[1:], l[0])
        return m(l[1:], mn)
    return mn
    

def mx(l, mxn):
    if len(l) > 0:
        if mxn < l[0]:
            return mx(l[1:], l[0])
        return mx(l[1:], mxn)
    return mxn


l = [10, 3, 2, 1, 4, 5]
res = m(l[1:], l[0])
res1 = mx(l[1:], l[0])
print(s(l), res, res1)



def minn (a):
    a.sort()
    return a[0]


def maxx (a):
    a.sort()
    return a[-1]


def summ(a):
    c = 0
    for i in range(len(a)):
        if a[i] == 0:
            break
        c += a[i]
    return c


def prodd(a):
    c = 1
    for i in range(len(a)):
        if a[i] == 1:
            break
        c *= a[i]
    return c


def usl(a):
    c = 3
    b = '>'
    q = []
    if b == '<':
        for i in a:
            if c < i:
                q.append(i)
    if b == '>':
        for i in a:
            if c < i:
                q.append(i)
    return q


a = [1, 2, 5, 1, 3, 7, 8, 9]
print (minn(a), maxx(a), summ(a), prodd(a), usl(a))
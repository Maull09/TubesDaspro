def rdom(depth, a, rang):
    b = a+2
    res = 100
    for i in range(depth):
        res = (a*res+b)%rang
    return res + 1

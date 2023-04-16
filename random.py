def rndom(depth, a, rang): #generate random number between 1--range
    b = a+2 #depth adalah jumlah iterasi atau berapa banyak angka diacak
    res = 100
    for i in range(depth):
        res = (a*res+b)%rang
    return res +1
for i in range(1,20):
    depth = i
    print(rndom(depth, depth*23*123457, 999999))

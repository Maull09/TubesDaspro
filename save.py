import data

def rndom(depth, a, rang): #generate random number between 1--range
    b = a+2 #depth adalah jumlah iterasi atau berapa banyak angka diacak
    res = 100
    if (a/depth==13) or (a/depth==17) or (a/depth==19) : #Khusus batch kumpul range = 0--5
        for i in range(depth):
            res = (a*res+b)%(rang+1)
        return res
    else:
        for i in range(depth): #yang lain range = 1--rang
            res = (a*res+b)%rang
        return res + 1

def hasil_kerja_jin(name,role):
    for i in range(1001) :
        if data.users[i][2] == role and data.users[i][0] ==name :
            data.users[i][3] = int(data.users[i][3]) + 1

def missing_row():
    i = 0 
    while True :
        if data.candi[i][0] == 0:
            return i
        i += 1

def sAve(type, data1):   
    if type=="bangun":
        n = missing_row()
        data.candi[n] = [data1[0]+1,data1[1],data1[2],data1[3],data1[4]] #catat bertambahnya jumlah candi
        sAve("kumpul", [-data1[2],-data1[3],-data1[4]]) #catat berkurangnya stok dengan memanggil fungsi diri sendiri sekali
    else:
        #data = [pasir, batu, air]
        data.bahan_bangunan[1] = ["pasir", "Digunakan untuk merekatkan batu",int(data.bahan_bangunan[1][2]) + data1[0]]
        data.bahan_bangunan[2] = ["batu","Digunakan sebagai fondasi dasar candi",int(data.bahan_bangunan[2][2]) +data1[1]]
        data.bahan_bangunan[3] = ["air", "Digunakan untuk memproses bahan lainnya",int(data.bahan_bangunan[3][2])+ data1[2]]

def find_nth_role(type,n):  # finding username of nth role in user.csv
    cnt = 0
    for i in range(1001):
        if data.users[i][2] == type :
            cnt += 1
        if cnt == n :
            return data.users[i][0]
        
def hitung_candi(): 
    cnt = 0
    for i in range(1,1000):
        if data.candi[i][3] != 0:
            cnt += 1
    return cnt

def hitung_jin(type):
    cnt = 0
    for i in range(1001):
        if data.users[i][2] == str(type):
            cnt += 1
    return cnt

def length(list):
    count = 0
    for items in list:
        count += 1
    return count

def strip_enter(teks):
    result = ''
    i = 0
    while i <= (len(teks)-2):
        result += teks[i]
        i += 1
    return result




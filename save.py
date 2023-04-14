import data
import F13

def hasil_kerja_jin(name,role):
    i = 0
    for i in range(1001) :
        if data.users[i][2] == role and data.users[i][0] ==name :
            data.users[i][3] = int(data.users[i][3]) + 1

def sAve(type, data1):   
    if type=="bangun":
        n = hitung_candi() #data =[id,pembuat, pasir, batu, air]
        data.candi[n+1] = [data1[0]+1,data1[1],data1[2],data1[3],data1[4]] #catat bertambahnya jumlah candi
        sAve("kumpul", [-data1[2],-data1[3],-data1[4]]) #catat berkurangnya stok dengan memanggil fungsi diri sendiri sekali
    else:
        #data = [pasir, batu, air]
        data.bahan_bangunan[1] = ["pasir", "Digunakan untuk merekatkan batu",int(data.bahan_bangunan[1][2]) + data1[0]]
        data.bahan_bangunan[2] = ["batu","Digunakan sebagai fondasi dasar candi",int(data.bahan_bangunan[2][2]) +data1[1]]
        data.bahan_bangunan[3] = ["air", "Digunakan untuk memproses bahan lainnya",int(data.bahan_bangunan[3][2])+ data1[2]]

def rndom(depth, a, rang): #generate random number between 1--range
    b = a+2 #depth adalah jumlah iterasi atau berapa banyak angka diacak
    res = 100
    for i in range(depth):
        res = (a*res+b)%rang
    return res + 1

def find_nth_role(type,n):  # finding username of nth role in user.csv
    cnt = 0
    for i in range(F13.length(data.users)):
        if data.users[i][2] == type :
            cnt += 1
        if cnt == n :
            return data.users[i][0]
        
def hitung_candi(): 
    cnt = 0
    for i in range(1,1000):
        if data.candi[i][0] == 0:
            return cnt
        else:
            cnt += 1
    return cnt

def hitung_jin(type):
    cnt = 0
    for i in range(1001):
        if data.users[i][2] == str(type):
            cnt += 1
    return cnt





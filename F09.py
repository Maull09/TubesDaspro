import data
import save

def laporanjin() :
    jumlah_pengumpul = save.hitung_jin("pengumpul") # Memanggil Fungsi hitung_candi untuk menghitung jumlah jin khususnya jin pengumpul
    jumlah_pembangun = save.hitung_jin("pembangun") # Memanggil Fungsi hitung_candi untuk menghitung jumlah jin khususnya jin pembangun
    total_jin = jumlah_pengumpul + jumlah_pembangun # Menghitung jumlah seluruh jin
    
    max_candi = 0
    min_candi = 101
    terajin = None
    termalas = None

    #cari candi terbanyak
    for i in range(3,1001) :
        if int(data.users[i][3]) >= int(max_candi) and data.users[i][0] != 0  :
            max_candi = int(data.users[i][3])

    #mencari candi tersedikit        
    for i in range(3,1001) :
        if int(data.users[i][3]) < int(min_candi) and data.users[i][2] == "pembangun" and data.users[i][0] != 0 :
            min_candi = int(data.users[i][3])

    # find the user with the max "candi" count
    for i in range(3, 1001):
        if int(data.users[i][3]) == max_candi :
            if terajin is None or str(data.users[i][0]) < str(terajin):
                terajin = str(data.users[i][0])

    # find the user with the min "candi" count
    for i in range(3, 1001):
        if int(data.users[i][3]) == min_candi :
            if termalas is None or str(data.users[i][0]) > str(termalas):
                termalas = str(data.users[i][0])

    print("Total Jin :",total_jin)
    print("Total Jin Pengumpul :", jumlah_pengumpul)
    print("Total Jin Pembangun :", jumlah_pembangun)
    if max_candi == 0:
        print("Jin Terajin : -")
        print("Jin Termalas: -")
    else:
        print("Jin Terajin :", terajin)
        print("Jin Termalas :", termalas)
    print("Jumlah Pasir :", data.bahan_bangunan[1][2])
    print("Jumlah Air :", data.bahan_bangunan[2][2])
    print("Jumlah batu :", data.bahan_bangunan[3][2])


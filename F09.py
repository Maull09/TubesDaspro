import data
import save

def laporanjin() :
    jumlah_pengumpul = save.hitung_jin("pengumpul")
    jumlah_pembangun = save.hitung_jin("pembangun")
    total = jumlah_pengumpul + jumlah_pembangun

    jumlah_candi = 0
    max_candi = 0

    for i in range(101) :
        for j in range(101) :
            if data.users[i][0] == data.candi[j][1] :
                data.users[i][3] += 1
    
    max_candi = data.users[3][3]
    min_candi = data.users[3][3]
    terajin = "null"
    termalas = "null"

    for i in range(101) :
        if data.users[i][3] > max_candi :
            max_candi = data.users[i][3]
            terajin = data.users[i][1]
        
    for i in range(101) :
        if data.users[i][3] < min_candi :
            min_candi = data.users[i][3]
            termalas = data.users[i][1]

    #handling letak alfabetis
    #print
    print(f"Total Jin : {total}")
    print(f"Total Jin Pengumpul : {jumlah_pengumpul}")
    print(f"Total Jin Pembangun : {jumlah_pembangun}")
    print(f"Jin Terajin : {terajin}")
    print(f"Jin Termalas : {termalas}")
    # print(f"Jumlah Pasir : {}")
    # print(f"Jumlah Air : {}")
    # print(f"Jumlah Batu : {}")

                

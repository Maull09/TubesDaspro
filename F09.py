import data
import save

def laporanjin() :
    jumlah_pengumpul = save.hitung_jin("pengumpul")
    jumlah_pembangun = save.hitung_jin("pembangun")
    total = jumlah_pengumpul + jumlah_pembangun

    max_candi = 0

    for i in range(1001) :
        for j in range(1001) :
            if data.users[i][0] == data.candi[j][1] :
                data.users[i][3] += 1
    
    max_candi = data.users[3][3]
    min_candi = data.users[3][3]
    terajin = data.users[3][0]
    termalas = data.users[3][0]

    #cari candi terbanyak
    for i in range(1001) :
        if data.users[i][3] >= max_candi :
            max_candi = data.users[i][3]

    #mencari jin terajin dengan candi terbanyak sesuai leksikografis
    for i in range(1001) :
        if data.users[i][3] == max_candi :
            if data.users[i][j] > terajin :
                terajin = data.users[i][3]

    #mencari candi tersedikit        
    for i in range(1001) :
        if data.users[i][3] < min_candi :
            min_candi = data.users[i][3]

    #mencari jin termalas dengan candi tersedikit sesuai leksikografis
    for i in range(1001) :
        if data.users[i][3] == min_candi :
            if data.users[i][j] < terajin :
                terajin = data.users[i][3]

    pasir = 0
    air = 0
    batu = 0

    for i in range(1001) :
        if data.candi[i][2] == terajin :
            for j in range(1001) :
                pasir += data.candi[i][3] 
            for j in range(1001) :
                air += data.candi[i][4] 
            for j in range(1001) :
                batu += data.candi[i][5]
                
    #print
    print(f"Total Jin : {total}")
    print(f"Total Jin Pengumpul : {jumlah_pengumpul}")
    print(f"Total Jin Pembangun : {jumlah_pembangun}")
    print(f"Jin Terajin : {terajin}")
    print(f"Jin Termalas : {termalas}")
    print(f"Jumlah Pasir : {pasir}")
    print(f"Jumlah Air : {air}")
    print(f"Jumlah Batu : {batu}")

                

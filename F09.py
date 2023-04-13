import data
import save

def laporanjin() :
    jumlah_pengumpul = save.hitung_jin("pengumpul") # Memanggil Fungsi hitung_candi untuk menghitung jumlah jin khususnya jin pengumpul
    jumlah_pembangun = save.hitung_jin("pembangun") # Memanggil Fungsi hitung_candi untuk menghitung jumlah jin khususnya jin pembangun
    total_jin = jumlah_pengumpul + jumlah_pembangun # Menghitung jumlah seluruh jin

    jumlah_candi = 0 # Total Jumlah Candi
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
            terajin = data.users[i][1] # Jin Terajin
        
    for i in range(101) :
        if data.users[i][3] < min_candi :
            min_candi = data.users[i][3]
            termalas = data.users[i][1] # Jin Termalas 
    
    print("Total Jin :",total_jin)
    print("Total Jin Pengumpul :", jumlah_pengumpul)
    print("Total Jin Pembangun :", jumlah_pembangun)
    print("Jin Terajin :", terajin)
    print("Jin Termalas :", termalas)
    print("Jumlah Pasir :", save.hitung_pasir( ))
    print("Jumlah Air :", save.hitung_air())
    print("Jumlah batu :", save.hitung_batu())

   
    

    #handling letak alfabetis
    #print

                

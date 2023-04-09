import data

def ubahjin() :
    username = input("Masukkan username jin : ")
    peubah = False
    ubahrolejin = False
    
    for i in range(100) :
        if data.users[i][0] == username :
            if data.users[i][2] == "pengumpul" :
                peubah = True
                ubahtipe = input("Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)? ")
                if ubahtipe == "Y" :
                    data.users[i][2] = "pembangun"
                    ubahrolejin = True
                else :
                    ubahrolejin = False
            else :
                peubah = True
                ubahtipe = input("Jin ini bertipe “Pembangun”. Yakin ingin mengubah ke tipe “Pengumpul” (Y/N)? ")
                if ubahtipe == "Y" :
                    data.users[i][2] = "pengumpul"
                    ubahrolejin = True
                else :
                    ubahrolejin = False
                
            
        


    if peubah == True and ubahrolejin == True :
        print("Jin telah berhasil diubah")
    elif peubah == True and ubahrolejin == False :
        print("Tipe jin tidak diubah")
    elif peubah == False :
        print("Tidak ada jin dengan username tersebut")


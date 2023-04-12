import data

def ubahjin() :
    username = input("Masukkan username jin : ")
    peubah = False
    ubahrolejin = False
    
    for i in range(1001) :
        if data.users[i][0] == username : #mengecek apakah ada jin dengan username tersebut
            #jika tipe jin pengumpul maka akan diubah ke pembangun
            if data.users[i][2] == "pengumpul" : 
                peubah = True
                ubahtipe = input("Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)? ")
                if ubahtipe == "Y" :
                    data.users[i][2] = "pembangun"
                    ubahrolejin = True
                else :
                    ubahrolejin = False
            #jika tipe jin pembangun maka akan diubah ke pengumpul
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


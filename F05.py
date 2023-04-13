import data

def ubahjin() :
    username = input("Masukkan username jin : ")
    peubah = False
    
    for i in range(1001) :
        if data.users[i][0] == username : #mengecek apakah ada jin dengan username tersebut
            #jika tipe jin pengumpul maka akan diubah ke pembangun
            if data.users[i][2] == "pengumpul" : 
                peubah = True
                ubahtipe = input("Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)? ")
                if ubahtipe == "Y" :
                    data.users[i][2] = "pembangun"
                    print("Jin telah berhasil diubah")
                    break
                else :
                    print("Tipe jin tidak diubah")
                    break
            #jika tipe jin pembangun maka akan diubah ke pengumpul
            else :
                peubah = True
                ubahtipe = input("Jin ini bertipe “Pembangun”. Yakin ingin mengubah ke tipe “Pengumpul” (Y/N)? ")
                if ubahtipe == "Y" :
                    data.users[i][2] = "pengumpul"
                    print("Jin telah berhasil diubah")
                    break
                else :
                    print("Tipe jin tidak diubah")
                    break
                
    if peubah == False :
        print("Tidak ada jin dengan username tersebut")


import data

def ubahjin() :
    username = input("Masukkan username jin : ")
    peubah = False
    ubahrolejin = False
    i = 1
    while data.users[i][0] != "stop" :
        if data.users[i][0] == username :
            if data.users[i][2] == "pengumpul" :
                peubah = True
                ubahtipe = input("Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)? ")
                if ubahtipe == "Y" :
                    data.users[i][2] = "pembangun"
                    ubahrolejin = True
                    break
                else :
                    ubahrolejin = False
                    break
            else :
                peubah = True
                ubahtipe = input("Jin ini bertipe “Pembangun”. Yakin ingin mengubah ke tipe “Pengumpul” (Y/N)? ")
                if ubahtipe == "Y" :
                    data.users[i][2] = "pengumpul"
                    ubahrolejin = True
                    break
                else :
                    ubahrolejin = False
                    break
            
        i += 1


    if peubah == True and ubahrolejin == True :
        print("Jin telah berhasil diubah")
    elif peubah == True and ubahrolejin == False :
        print("Tipe jin tidak diubah")
    elif peubah == False :
        print("Tidak ada jin dengan username tersebut")


import data

def hapusjin() :
    hapus = False
    username = input()

    for i in range(1,1001) :
        if data.users[i][0] == username :
            yakin = input("konfirm")
            if yakin == "Y" :
                for j in range(3) :
                    data.users[i][j] = 0
                    hapus = True

        else :
            hapus = False

    if hapus ==False :
        print("Tidak ada username tsb")
    elif hapus == True :
        print("data terhapus")

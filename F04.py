import data

def hapusjin() :
    hapus = False
    username = input("Masukkan username jin : ")

    for i in range(1,1001) :
        if data.users[i][0] == username :
            confirm = input(f"Apakah anda yakin ingin menghapus jin dengan username {username} ?")
            if confirm == "Y" or confirm == "y" :
                for j in range(3) :
                    data.users[i][j] = 0
                    hapus = True

        else :
            hapus = False

    if hapus ==False :
        print("Tidak ada jin dengan username tersebut.")
    elif hapus == True :
        print("Jin telah berhasil dihapus dari alam gaib.")

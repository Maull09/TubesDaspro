import data

def hapusjin() :
    username = input("Masukkan username jin : ") #
    username_ada = False
    for i in range(1,1001) :
        if data.users[i][0] == username : # Melakukan cek apakah username yang di input sesuai 
            confirm = input(f"Apakah anda yakin ingin menghapus jin dengan username {username} ?")
            if confirm == "Y" or confirm == "y" :
                for j in range(4) :
                    data.users[i][j] = 0
                print("Jin telah berhasil dihapus dari alam gaib.")
                username_ada = True
                break
            else :
                print("Jin tidak terhapus")
                username_ada = True
                break
        else :
            username_ada = False

    if username_ada == False :
        print("Tidak ada jin dengan username tersebut.")

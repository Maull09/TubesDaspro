import data

def hapusjin() :
    username = input("Masukkan username jin : ") #
    username_ada = False
    for i in range(1,1001) :
        if data.users[i][0] == username : # Melakukan cek apakah username yang di input sesuai 
            confirm = input(f"Apakah anda yakin ingin menghapus jin dengan username {username} ?")
            if confirm == "Y" or confirm == "y" :
                for k in range(1001) : #karena jin terhapus maka candi terhapus
                    if data.users[i][0] == data.candi[k][1] :
                       data.candi[k][0] = 0 ; data.candi[k][1] = 0 ; data.candi[k][2] = 0 ; data.candi[k][3] = 0 ; data.candi[k][4] = 0 
                for j in range(5) : #menghapus jin dengan mengembalikan ke nilai default
                    data.users[i][j] = 0
                print("Jin telah berhasil dihapus dari alam gaib.")
                username_ada = True
                break
            else : #jin tidak jadi dihapus
                print("Jin tidak terhapus")
                username_ada = True
                break
        else : #tidak ada username jin tsb
            username_ada = False

    if username_ada == False :
        print("Tidak ada jin dengan username tersebut.")

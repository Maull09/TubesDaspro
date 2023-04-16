import data

def hancurkancandi():
    candi_ketemu = True
    id = input("Masukkan ID candi: ") # meminta input id candi dari user
    for x in range (1001):
        if data.candi[x][0] == id: # jika ada data id sesuai inputan user
            yakin = input(f"Apakah anda yakin ingin menghancurkan candi ID: {id} (Y/N)?") # meminta input apakah user mau menghancurkan candi atau tidak
            if yakin == "Y" or yakin == "y": # jika user ingin menghancurkan candi
                for i in range(1001) :
                    if data.candi[x][1] == data.users[i][0] :
                        data.users[i][3] = int(data.users[i][3]) - 1
                data.candi[x][0] = 0 ; data.candi[x][1] = 0 ; data.candi[x][2] = 0 ; data.candi[x][3] = 0 ; data.candi[x][4] = 0 # semua data diubah menjadi 0 sesuai data awal
                print("Candi telah berhasil dihancurkan.")
                candi_ketemu = True
                break
            else : 
                print("Candi tidak terhapus")
                candi_ketemu = True
                break
        else:
            candi_ketemu = False
            
    if candi_ketemu == False :
        print("Tidak ada candi dengan ID tersebut.") # jika tidak ada data id sesuai input user
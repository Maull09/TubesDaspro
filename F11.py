import data

def hancurkancandi(): 
    id = input("Masukkan ID candi: ") # meminta input id candi dari user
    for x in range (1001):
        if data[x][0] == id: # jika ada data id sesuai inputan user
            yakin = input(f"Apakah anda yakin ingin menghancurkan candi ID: {id} (Y/N)?") # meminta input apakah user mau menghancurkan candi atau tidak
            if yakin == "Y" or yakin == "y": # jika user ingin menghancurkan candi
                 data[x][0] = 0 ; data[x][1] = 0 ; data[x][2] = 0 ; data[x][3] = 0 ; data[x][4] = 0 # semua data diubah menjadi 0 sesuai data awal
                 print("Candi telah berhasil dihancurkan.")
        else:
            print("Tidak ada candi dengan ID tersebut.") # jika tidak ada data id sesuai input user
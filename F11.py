import data


def hancurkancandi():
    id = input("Masukkan ID candi: ")
    for x in range (1001):
        if data[x][0] == id:
            yakin = input(f"Apakah anda yakin ingin menghancurkan candi ID: {id} (Y/N)?")
            if yakin == "Y" or yakin == "y":
                 data[x][0] = 0 ; data[x][1] = 0 ; data[x][2] = 0 ; data[x][3] = 0 ; data[x][4] = 0   
                 print("Candi telah berhasil dihancurkan.") 
        else:
            print("Tidak ada candi dengan ID tersebut.")
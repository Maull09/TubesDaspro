import os
import save

def reload(folder_name,file_name, var, jk):
    file_path = os.path.join(folder_name, file_name)
<<<<<<< HEAD
    var = data.loading(file_path, var, jk)
# Menerima argumen menggunakan argparse
def load() :
    parser = argparse.ArgumentParser()
    parser.add_argument("folder_name", help="Nama folder yang berisi file penyimpanan")
    args = parser.parse_args()
    # Validasi folder
    folder_name = args.folder_name
    if not os.path.exists(folder_name): # Jika folder tidak terdapat pada os path maka menghasilkan output file tidak ditemukan
        print(f"Folder \"{folder_name}\" tidak ditemukan.") # Program keluar
    else: # Jika nama folder terdapat di os path maka file akan berhasil di load
        print("Loading...")
        # Menjalankan prosedur load data
        reload(folder_name,"candi.csv", data.candi, 5)
        reload(folder_name,"bahan_bangunan.csv", data.bahan_bangunan, 3)
        reload(folder_name,"user.csv", data.users, 4)
        print("Data telah dimuat!")
        
=======
    var = loading(file_path, var, jk)
    
def loading(file,var,jk):
    with open(file) as f :
        raw_lines = f.readlines()
        lines = []
        for i in range(save.length(raw_lines)):
            if i < save.length(raw_lines):
                lines += [save.strip_enter(raw_lines[i])]
        j = 0
        for line in lines:
            data = ""
            k = 0
            for i in range(save.length(line)):
                if line[i] == ';':
                    # jika bertemu ';' yang terdapat pada csv maka data akan ditambahkan ke arr
                    if k < jk:  # pastikan nilai k tidak melebihi jumlah kolom
                        var[j][k] = data
                        k += 1
                        data = ""
                    else:  # jika k sudah melebihi jumlah kolom, atur kembali ke 0
                        k = 0
                elif (i == save.length(line) - 1):
                    # menambahkan data yang paling belakang untuk ditambahkan ke arr
                    var[j][k] = data + line[i]
                else:
                    data += line[i]
            j += 1                
        return var


>>>>>>> e692045e21978a007466a3c18f6bf871a1a9fa67

import os
import argparse
import data

def reload(folder_name,file_name, var, jk):
    file_path = os.path.join(folder_name, file_name)
    var = data.loading(file_path, var, jk)
# Menerima argumen menggunakan argparse
def load() :
    parser = argparse.ArgumentParser()
    parser.add_argument("folder_name", help="Nama folder yang berisi file penyimpanan")
    args = parser.parse_args()
    # Validasi folder
    folder_name = args.folder_name
    if not os.path.exists(folder_name): # Jika folder tidak terdapat pada os path maka menghasilkan output file tidak ditemukan
        print(f"Folder \"{folder_name}\" tidak ditemukan.")
    else: # Jika nama folder terdapat di os path maka file akan berhasil di load
        print("Loading...")
        reload(folder_name,"candi.csv", data.candi, 5)
        reload(folder_name,"bahan_bangunan.csv", data.bahan_bangunan, 3)
        reload(folder_name,"user.csv", data.users, 4)
        print("Data telah dimuat!")
        
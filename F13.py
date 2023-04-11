import os
import argparse
import data

def reload(folder_name,file_name, var, jk):
    file_path = os.path.join(folder_name, file_name)
    var = data.loading(file_path, var, jk)

def load() :
    parser = argparse.ArgumentParser()
    parser.add_argument("folder_name", help="Nama folder yang berisi file penyimpanan")
    args = parser.parse_args()

    folder_name = args.folder_name
    if not os.path.exists(folder_name):
        print(f"Folder \"{folder_name}\" tidak ditemukan.")
    else:
        print("Loading...")
        reload(folder_name,"candi.csv", data.candi, 5)
        reload(folder_name,"bahan_bangunan.csv", data.bahan_bangunan, 3)
        reload(folder_name,"user.csv", data.users, 4)
        print("Data telah dimuat!")
        
import os
import argparse
import data

def load(folder_name):
    file_names = ["user.csv", "candi.csv", "bahan_bangunan.csv"]

    for file_name in file_names:
        file_path = os.path.join(folder_name, file_name)
        if file_name == "user.csv":
            data.users = data.loading(file_path, data.users, 4)
        elif file_name == "candi.csv":
            data.candi = data.loading(file_path, data.candi, 5)
        elif file_name == "bahan_bangunan.csv":
            data.bahan_bangunan = data.loading(file_path, data.bahan_bangunan, 3)

    print("Data telah dimuat!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("folder_name", help="Nama folder yang berisi file penyimpanan")
    args = parser.parse_args()

    folder_name = args.folder_name
    if not os.path.exists(folder_name):
        print(f"Folder \"{folder_name}\" tidak ditemukan.")
    else:
        print("Loading...")
        load(folder_name)
        print("Selamat datang di program \"Manajerial Candi\"")
        print("Silahkan masukkan username Anda")
        print(">>>")

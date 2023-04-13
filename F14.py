import os
import data


def save(file_name,var,k,b):
    folder_name = "save/"+ data.load_folder_name
    file_path = os.path.join(folder_name, file_name)

    if os.path.exists(folder_name):
        if os.path.exists(file_path):
            print(f"File {file_name} pada folder {folder_name} sudah ada, akan diganti dengan yang baru.")
        else:
            print(f"Folder {folder_name} sudah ada tetapi file {file_name} belum ada. Membuat file baru.")
    else:
        print(f"Folder {folder_name} belum ada. Membuat folder dan file baru.")
        os.makedirs(folder_name)
        
    with open(file_path, "w") as f:
        for i in range(b) :
            for j in range(k) :
                f.write(str(var[i][j])+";")
            f.write(str(var[i][k])+"\n")        

    print(f"Berhasil menyimpan data di folder {folder_name}!")

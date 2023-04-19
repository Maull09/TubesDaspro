import os
import data


def save(file_name,var,k,b):
    folder_name = "save/"+ data.load_folder_name #mengambil path nama folder
    file_path = os.path.join(folder_name, file_name) #menggabungkan path nama folder dan nama file

    if os.path.exists(folder_name): # jika folder dengan nama hasil input ada di database folder
        if os.path.exists(file_path): # jika file dengan nama hasil input ada di database file
            print(f"File {file_name} pada folder {folder_name} sudah ada, akan diganti dengan yang baru.") # update isi file
    else: # jika tidak ada folder dengan nama hasil input di database folder
        print(f"Folder {folder_name} belum ada. Membuat folder dan file baru.")
        os.makedirs(folder_name) # membuat direktori berdasarkan nama folder sesuai hasil input
        
    with open(file_path, "w") as f: # membuka file
        for i in range(b) :
            for j in range(k) :
                if var[i][j] != 0 :
                    f.write(str(var[i][j])+";") # menuliskan nilai dengan diakhiri titik koma
            if var[i][j] != 0 :        
                f.write(str(var[i][k])+"\n") # menuliskan nilai dengan diakhiri baris baru

    print(f"Berhasil menyimpan data di folder {folder_name}!")

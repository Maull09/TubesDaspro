from F14 import save
import data
    
def exit():
    ubah = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ") # meminta input user
    while ubah != "Y" and ubah != "y" and ubah != "N" and ubah != "n" :
        ubah = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ") # meminta input user

    if ubah == "Y" or ubah == "y": # jika user input Y/y {memilih untuk menyimpan file}
        folder_name = input("Masukkan nama folder: ")
        data.load_folder_name = folder_name
        save("user.csv", data.users, 4, 101)
        save("bahan_bangunan.csv", data.bahan_bangunan, 2, 4)
        save("candi.csv", data.candi, 4, 101)
        quit()
    elif ubah == "N" or ubah == "n": # jika user input N/n {memilih untuk tidak menyimpan file}
        quit() # langsung keluar dari program tanpa menyimpan
         


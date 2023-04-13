from F14 import save
import data
    
def exit():
    while True:
        if data.usernamee == "Bondowoso" or data.usernamee == "Roro" :
            ubah = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ") # meminta input user
            if ubah == "Y" or ubah == "y": # jika user input Y/y {memilih untuk menyimpan file}
                folder_name = input("Masukkan nama folder: ")
                data.load_folder_name = folder_name
                save("user.csv", data.users, 3, 101)
                save("bahan_bangunan.csv", data.bahan_bangunan, 2, 4)
                save("candi.csv", data.candi, 4, 101)
                break
            elif ubah == "N" or ubah == "n": # jika user input N/n {memilih untuk tidak menyimpan file}
                data.keluar = True
                break # langsung keluar dari program tanpa menyimpan
            else:
                continue # jika mengisi selain Y/y/N/n program akan meminta kembali input user
        else :
            data.keluar = True
            break
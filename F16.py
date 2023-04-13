from F14 import save
import data
def exit():
    while True:
        ubah = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ") # meminta input user
        if ubah == "Y" or ubah == "y": # jika user input Y/y {memilih untuk menyimpan file}
            save("user.csv", data.users)
            save("bahan_bangunan.csv", data.bahan_bangunan)
            save("candi.csv", data.candi)
            break
        elif ubah == "N" or ubah == "n": # jika user input N/n {memilih untuk tidak menyimpan file}
            break # langsung keluar dari program tanpa menyimpan
        else:
            continue # jika mengisi selain Y/y/N/n program akan meminta kembali input user
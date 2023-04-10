from F14 import save
import data

def exit():
    while True:
        ubah = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        if ubah == "Y" or ubah == "y":
            save("user.csv", data.users)
            save("bahan_bangunan.csv", data.bahan_bangunan)
            save("candi.csv", data.candi)
            break
        elif ubah == "N" or ubah == "n":
            break
        else:
            continue

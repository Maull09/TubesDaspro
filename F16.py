import data
import save
import sys

def exit():
    while True:
        ubah = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        if ubah == "Y" or ubah == "y":
            save()
            break
        elif ubah == "N" or ubah == "n":
            break
        else:
            continue
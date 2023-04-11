import data
import save
import F01
from F02 import logout
from F03 import summonjin
from F04 import hapusjin
from F05 import ubahjin
import F06
import F07
import F08
from F09 import laporanjin 
from F10 import laporancandi
from F11 import hancurkancandi
from F12 import ayamberkokok
import F14
import F15
from F16 import exit


def run(command : str) :
    if command == "login" :
        if data.login_status == "false":
            F01.login()
        else :
            print("Login gagal")
            print(f"Anda telah login dengan username {data.usernamee}, silahkan logout terlebih dahulu sebelum melakukan login kembali")
    elif command == "logout" :
        if data.login_status == "true" :
            logout()
        else :
            print("Logout gagal")
            print(f"Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
    elif command == "summonjin" :
        if data.role == "bandung_bondowoso" :
            if save.hitung_jin > 100 :
                print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
            else :
                summonjin()
        else :
            ("Maaf anda tidak memiliki akses")
    elif command == "hapusjin" :
        if data.role == "bandung_bondowoso" :
            hapusjin()
        else :
            ("Maaf anda tidak memiliki akses")
    elif command == "ubahjin" :
        if data.role == "bandung_bondowoso" :
            ubahjin()
        else :
            ("Maaf anda tidak memiliki akses")
    elif command == "bangun" :
        if data.role == "pembangun" :
            F06.bangun()
        else :
            ("Maaf anda tidak memiliki akses")
    elif command == "kumpul" :
        if data.role == "pengumpul" :
            F07.kumpul()
        else :
            ("Maaf anda tidak memiliki akses")
    elif command == "batchkumpul" :
        if data.role == "bandung_bondowoso" :
            F08.batchkumpul()
        else :
            ("Maaf anda tidak memiliki akses")
    elif command == "batchbangun" :
        if data.role == "bandung_bondowoso" :
            F08.batchbangun()
        else :
            ("Maaf anda tidak memiliki akses")
    elif command == "laporanjin" :
        if data.role == "bandung_bondowoso" :
            laporanjin()
        else :
            ("Maaf anda tidak memiliki akses")
    elif command == "laporancandi" :
        if data.role == "bandung_bondowoso" :
            laporancandi()
        else :
            ("Maaf anda tidak memiliki akses")
    elif command == "hancurkancandi" :
        if data.role == "roro_jonggrang" :
            hancurkancandi()
        else :
            ("Maaf anda tidak memiliki akses")
    elif command == "ayamberkokok" :
        if data.role == "roro_jonggrang" :
            ayamberkokok()
        else :
            ("Maaf anda tidak memiliki akses")
    elif command == "save" :
        if data.role == "bandung_bondowoso" or data.role == "roro_jonggrang" :
            folder_name = input("Masukkan nama folder: ")
            data.load_folder_name = folder_name
            F14.save("user.csv", data.users, 3, 101)
            F14.save("bahan_bangunan.csv", data.bahan_bangunan, 2, 4)
            F14.save("candi.csv", data.candi, 4, 101)
        else :
            ("Maaf anda tidak memiliki akses") 
    elif command == "help" :
        F15.help()
    elif command == "exit" :
        exit()
import data
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
        summonjin()
    elif command == "hapusjin" :
        hapusjin()
    elif command == "ubahjin" :
        ubahjin()
    elif command == "bangun" :
        F06.bangun()
    elif command == "kumpul" :
        F07.kumpul()
    elif command == "batchkumpul" :
        F08.batchkumpul()
    elif command == "batchbangun" :
        F08.batchbangun()
    elif command == "laporanjin" :
        laporanjin()
    elif command == "laporancandi" :
        laporancandi()
    elif command == "hancurkancandi" :
        hancurkancandi()
    elif command == "ayamberkokok" :
        ayamberkokok()
    elif command == "save" :
        folder_name = input("Masukkan nama folder: ")
        data.load_folder_name = folder_name
        F14.save("user.csv", data.users)
        F14.save("bahan_bangunan.csv", data.bahan_bangunan)
        F14.save("candi.csv", data.candi)
    elif command == "help" :
        F15.help()
    elif command == "exit" :
        exit()
import data

import F01
from F02 import logout
from F05 import ubahjin
from F15 import help


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
        None
    elif command == "hapusjin" :
        None
    elif command == "ubahjin" :
        ubahjin()
    elif command == "bangun" :
        None
    elif command == "kumpul" :
        None
    elif command == "batchkumpul" :
        None
    elif command == "batchbangun" :
        None
    elif command == "laporanjin" :
        None
    elif command == "laporancandi" :
        None
    elif command == "hancurkancandi" :
        None
    elif command == "ayamberkokok" :
        None
    elif command == "save" :
        None
    elif command == "help" :
        help()
    elif command == "exit" :
        None


import data
from F01 import login
from F02 import logout
from F05 import ubahjin
from F15 import help


def run(command : str) :
    if command == "login" :
        if data.login_status == "false":
            login()
        else :
            print("silahkan logout terlebih dahulu")

    elif command == "logout" :
        logout()
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

import data
from F01 import login
from F02 import logout

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
        None
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
        None
    elif command == "exit" :
        None

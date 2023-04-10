import data
import save

def laporancandi() :
    total_candi = save.hitung_candi()
    total_pasir = 0
    total_batu = 0
    total_air = 0
    
    for i in range (1,1001):
        if data.users[i][2] != 0:
            total_pasir += 1
    for i in range (1, 1001):
        if data.users[i][3] != 0:
            total_batu += 1
    for i in range (1, 1001):
        if data.users[i][4] != 0:
            total_air += 1

    i_termahal = 0
    i_termurah = 0
    hargacandi = 10000*data.users[1][2] + 15000*data.users[1][3] + 7500*data.users[1][4]

    for i in range (1, 1001):
        hasil_hargacandi = 10000*data.users[i][2] + 15000*data.users[i][3] + 7500*data.users[i][4]
        if hargacandi > hasil_hargacandi:
            hargacandi = hasil_hargacandi
            i_termahal = i

    for i in range (1, 1001):
        hasil_hargacandi = 10000*data.users[i][2] + 15000*data.users[i][3] + 7500*data.users[i][4]
        if hargacandi < hasil_hargacandi:
            hargacandi = hasil_hargacandi
            i_termurah = i

    print("ID Candi Termahal: ", str(i_termahal))
    print("ID Candi Termurah: ", str(i_termurah))


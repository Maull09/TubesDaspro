import data
import save
# Hanya dapat diakses oleh Bandung Bondowoso
# Menginisiasi variabel total_candi, total_pasir, total_batu, total_air
def laporancandi() :
    total_candi = save.hitung_candi()
    total_pasir = 0
    total_batu = 0
    total_air = 0
    # Menentukan total_pasir, total_batu, dan total_candi
    for i in range (1,1001):
        if data.candi[i][1] != 0:
            total_pasir += 1
    for i in range (1, 1001):
        if data.candi[i][2] != 0:
            total_batu += 1
    for i in range (1, 1001):
        if data.candi[i][3] != 0:
            total_air += 1
    # Menginisiasi variabel i_termahal, i_termurah, hargacandi sesuai dengan rumus yang terdapat di spesifikasi
    i_termahal = 0
    i_termurah = 0
    hargacandi = 10000*int(data.candi[1][2]) + 15000*int(data.candi[1][3]) + 7500*int(data.candi[1][4])
    # Menentukan ID termahal dengan membandingkan variabel hargacandi dengan hasil_hargacandi
    for i in range (1, 1001):
        hasil_hargacandi = 10000*int(data.candi[i][2]) + 15000*int(data.candi[i][3]) + 7500*int(data.candi[i][4])
        if hargacandi > hasil_hargacandi:
            hargacandi = hasil_hargacandi
            i_termahal = i
    # Menentukan ID termurah dengan membandingkan variabel hargacandi dengan hasil_hargacandi
    for i in range (1, 1001):
        hasil_hargacandi = 10000*int(data.candi[i][2]) + 15000*int(data.candi[i][3]) + 7500*int(data.candi[i][4])
        if hargacandi < hasil_hargacandi:
            hargacandi = hasil_hargacandi
            i_termurah = i
    # Menampilkan output
    print("Total Candi: ", str(total_candi))
    print("Total Pasir yang digunakan: ", str(total_pasir))
    print("Total Batu yang digunakan: ", str(total_batu))
    print("Total Air yang digunakan: ", str(total_air))
    if total_candi == 0:
        print("ID Candi Termahal: -")
        print("ID Candi Termurah: -")
    else:
        print("ID Candi Termahal: ", str(i_termahal))
        print("ID Candi Termurah: ", str(i_termurah))


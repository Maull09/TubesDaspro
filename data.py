# Anggap semua fungsi yang dipanggil merupakan fungsi yang sudah dibuat sendiri pada modul lain
users = [] # Matriks data user
candi = [] # Matriks data candi
bahan_bangunan = [] # Data bahan bangunan
login_status = "false"
role = "null"
def count(matrix):
    cnt = 0
    for i in matrix:
        cnt += 1
    return cnt

def load(filename,data):
    data = []
    with open(filename) as f:
        for line in f:
            row = []
            cell = ''
            for char in line:
                if char == ';':
                    row.append(cell)
                    cell = ''
                else:
                    cell += char
            row.append(cell[:-1]) # exclude newline character
            data.append(row)
    return data


users = load("user.csv", users)
candi = load("candi.csv", candi)
bahan_bangunan = load("bahan_bangunan.csv", bahan_bangunan)
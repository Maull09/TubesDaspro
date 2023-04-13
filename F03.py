import data
# Hanya dapat diakses oleh role Bandung Bondowoso
def summonjin():
    print('''
Jenis jin yang dapat dipanggil:
 (1) Pengumpul - Bertugas mengumpulkan bahan bangunan
 (2) Pembangun - Bertugas membangun candi
''')
    # Menerima input berupa integer untuk menentukan jenis jin yang dipanggil
    panggil_jin = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
    # Meminta inputan sampai valid (1 atau 2)
    while panggil_jin != 1 and panggil_jin != 2:
        print("Tidak ada jenis jin bernomor " , str(panggil_jin), "!")
        panggil_jin = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
    # Memanggil jin sesuai dengan inputan
    if panggil_jin == 1:
        print("Memilih jin Pengumpul.")
    else:
        print("Memilih jin Pembangun.")
    # Menerima inputan username jin yang ingin dipanggil
    username_jin = input("Masukkan username jin: ")
    # Mengecek apakah username sudah diambil atau belum dengan mengeceknya di data user
    for i in range(1000) :
        while data.users[i][0] == username_jin : # Menerima inputan username sampai username unik yang belum pernah diambil
            print("Username ", username_jin, " sudah diambil!")
            username_jin = input("Masukkan username jin: ")
    # Memasukkan password dan akan terus meminta inputan sampai panjang password berjumlah 5 - 25 karakter
    for i in range(1000) :
        if data.users[i][0] == 0:
            data.users[i][0] = username_jin
            password_jin = input("Masukkan password jin: ")
            while len(password_jin) < 5 or len(password_jin) > 25:
                print("Password panjangnya harus 5-25 karakter!")
                password_jin = input("Masukkan password jin: ")
            # Memanggil jin
            data.users[i][1] = password_jin
            print("Mengumpulkan sesajen...")
            print("Menyerahkan sesajen...")
            print("Membacakan mantra...")
            print("Jin ", username_jin, "berhasil dipanggil!")
            break

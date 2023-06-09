import data

def help() :
    if data.login_status == "false" : #help untuk yang belum login
        print('''
================Help================
silahkan pakai command berikut
1. login
    Untuk masuk menggunakan akun.
2. help
    Untuk menampilkan semua command yang dapat digunakan sesuai dengan akses yang dimiliki pemain.
3. save
    Untuk menjalankan prosedur menyimpan data yang berada di program sesuai dengan struktur data eksternal.
4. exit
    Untuk keluar dari program dan kembali ke terminal.
''')
    else : #help untuk yang sudah login
        if data.role == "bandung_bondowoso" : #help untuk role bandung bondowoso
            print('''
================Help================
1. logout
    Untuk keluar akun yang digunakan sekarang.
2. summonjin
    Untuk memanggil jin dari dunia lain.
3. hapusjin
    Untuk menghapus jin (jika jin terhapus candi yang dibuat juga ikut terhapus).
4. ubahjin
    Untuk mengubah tipe jin.
5. batchkumpul
    Untuk memerintahkan jin bertipe pengumpul untuk mengumpulkan bahan.
6. batchbangun
    Untuk memerintahkan jin bertipe pembangun untuk membangun candi.
7. laporanjin
    Untuk mengambil laporan jin untuk mengetahui kinerja dari para jin.
8. laporancandi
    Untuk mengambil laporan candi untuk mengetahui progress pembangunan candi.
9. save
    Untuk menjalankan prosedur menyimpan data yang berada di program sesuai dengan struktur data eksternal.
10.exit
    Untuk keluar dari program dan kembali ke terminal.
11.help
    Untuk menampilkan semua command yang dapat digunakan sesuai dengan akses yang dimiliki pemain.

''')
        elif data.role == "roro_jonggrang" : #help untuk role roro jonggrang
            print('''
================Help================
1. logout
    Untuk keluar dari akun sekarang.
2. hancurkancandi
    Untuk menghancurkan candi agar menggagalkan rencana Bandung Bondowoso
3. ayamberkokok
    Untuk menyelesaikan permainan dengan memalsukan pagi hari.
4. save
    Untuk menjalankan prosedur menyimpan data yang berada di program sesuai dengan struktur data eksternal.
5. exit
    Untuk keluar dari program dan kembali ke terminal.
6. help
    Untuk menampilkan semua command yang dapat digunakan sesuai dengan akses yang dimiliki pemain.
    
''')
        elif data.role == "pengumpul" : #help untuk role jin pengumpul
            print('''
================Help================
1. logout
    Untuk keluar dari akun sekarang.
2. kumpul
    Untuk mengumpulkan bahan-bahan yang diperlukan untuk membangun candi.
3. help
    Untuk menampilkan semua command yang dapat digunakan sesuai dengan akses yang dimiliki pemain.
4. save
    Untuk menjalankan prosedur menyimpan data yang berada di program sesuai dengan struktur data eksternal.
5. exit
    Untuk keluar dari program dan kembali ke terminal.
''')
        elif data.role == "pembangun" : #help untuk role jin pembangun
            print('''
================Help================
1. logout
    Untuk keluar dari akun sekarang.
2. bangun
    Untuk membangun candi.
3. help
    Untuk menampilkan semua command yang dapat digunakan sesuai dengan akses yang dimiliki pemain.
4. save
    Untuk menjalankan prosedur menyimpan data yang berada di program sesuai dengan struktur data eksternal.
5. exit
    Untuk keluar dari program dan kembali ke terminal.
''')
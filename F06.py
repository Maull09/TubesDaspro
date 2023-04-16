import data
import save
def bangun():
    depth =save.hitung_candi()+1
    pasir = save.rndom(depth, depth*3, 5) #rndm(depth,a,range)
    batu = save.rndom(depth, depth*7, 5)
    air = save.rndom(depth, depth*11, 5)
    if int(data.bahan_bangunan[1][2]) >= pasir and int(data.bahan_bangunan[2][2]) >= batu and int(data.bahan_bangunan[3][2]) >= air :
        if save.hitung_candi() < 100:
            n = data.iterasi_candi + 1
            rndom_num = save.
            save.sAve("bangun", [save.hitung_candi(), data.usernamee ,pasir,batu,air]) #candi = [id,username,pasir,batu,air]
            print("Candi berhasil dibangun.") #bahan mencukupi
            print("Sisa candi yang perlu dibangun: "+str(100-save.hitung_candi())+".")
            save.hasil_kerja_jin(data.usernamee,"pembangun")
            data.iterasi += 1
        else:
            save.sAve("kumpul",[pasir,batu,air])#data = [pasir, batu, air]
            save.hasil_kerja_jin(data.usernamee,"pembangun")
            print("Candi berhasil dibangun.")
            print("Sisa candi yang perlu dibangun: 0.")
    else: 
        print("Bahan bangunan tidak mencukupi.") #bahan tidak mencukupi
        print("Candi tidak bisa dibangun! ")

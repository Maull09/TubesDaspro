import data
import save
def bangun():
    if save.hitung_candi() != 100: #candi tidak bisa melebihi 100
        depth =save.hitung_candi()+1
        pasir = save.rndom(depth, depth*3, 5) #rndm(depth,a,range)
        batu = save.rndom(depth, depth*7, 5)
        air = save.rndom(depth, depth*11, 5)
        if int(data.bahan_bangunan[1][2]) >= pasir and int(data.bahan_bangunan[2][2]) >= batu and int(data.bahan_bangunan[3][2]) >= air :
            print("Candi berhasil dibangun.") #bahan mencukupi
            save.sAve("bangun", [save.hitung_candi(), save.find_nth_role("pembangun",1),pasir,batu,air]) #candi = [id,username,pasir,batu,air]
            print("Sisa candi yang perlu dibangun: "+str(100-save.hitung_candi())+".")
        else: 
            print("Bahan bangunan tidak mencukupi.") #bahan tidak mencukupi
            print("Candi tidak bisa dibangun! ")
    else:
        print("Candi tidak bisa dibangun! ") #candi sudah sebanyak 100
        print("Sisa candi yang perlu dibangun: "+str(100-save.hitung_candi())+".")


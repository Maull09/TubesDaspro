import data
import save

def batchkumpul():
    n = save.hitung_jin("pengumpul") #hitung_jin(type)
    if n!= 0:
        pasirT=0 #pasir total yang dibutuhkan
        batuT= 0 #batu total yang dibutuhkan
        airT = 0 #air total yang dibutuhkan
        for i in range(1,n+1):
            depth = data.iterasi +1 
            pasirT += save.rndom(depth, depth*13, 5) #rndm(depth,a,range)
            batuT += save.rndom(depth, depth*17, 5)
            airT += save.rndom(depth, depth*19, 5)
            data.iterasi += 1
        save.sAve("kumpul", [pasirT, batuT, airT])
        print(f"Mengerahkan {n} jin untuk mengumpulkan bahan.")
        print("Jin menemukan "+str(pasirT)+" pasir, "+str(batuT)+" batu, dan "+str(airT)+" air.")
    else:
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
        
def batchbangun():
    n = save.hitung_jin("pembangun")  #jumlah jin pembangun
    if n != 0:
        i = 0
        pasirT=0 #pasir total yang dibutuhkan
        batuT= 0 #batu total yang dibutuhkan
        airT = 0 #air total yang dibutuhkan
        store = [[0 for i in range(5)] for j in range(n)] #store[0] = [id, pembuat, pasir, batu, air], menyimpan record pembuatan candi
        while i<n: #iterasi pembuatan candi sebanyak n kali
            depth = data.iterasi + 1
            pasir = save.rndom(depth, depth*13, 5) #jumlah pasir, batu, dan air yang dibutuhkan oleh suatu jin (random)
            batu = save.rndom(depth, depth*17, 5)
            air = save.rndom(depth, depth*19, 5)
            pasirT += pasir
            batuT += batu
            airT += air
            depth_c = data.iterasi_candi + 1
            rndom_num = save.rndom(depth_c, depth_c*23*123457, 999999)
            store[i] = [rndom_num, save.find_nth_role("pembangun",i+1), pasir, batu, air]
            data.iterasi_candi += 1
            data.iterasi += 1
            i += 1

        print("Mengerahkan "+str(i)+" jin untuk membangun candi dengan total bahan "+str(pasirT)+" pasir, "+str(batuT)+" batu, dan "+str(airT)+" air.")
        if int(data.bahan_bangunan[1][2]) >= pasirT and int(data.bahan_bangunan[2][2]) >= batuT and int(data.bahan_bangunan[3][2]) >= airT :
            if (save.hitung_candi() + i )> 100:
                print("Jin berhasil membangun total "+str(100-save.hitung_candi())+" candi.") #bahan yang diperlukan cukup
                for j in range(0,100-save.hitung_candi()):
                    save.sAve("bangun",store[j]) #menyimpan hasil bangunan 
            else:
                print("Jin berhasil membangun total "+str(i)+" candi.") #bahan yang diperlukan cukup
                for j in range(0,i):
                    save.sAve("bangun",store[j]) #menyimpan hasil bangunan 
            
            for j in range(1,i+1):
                save.hasil_kerja_jin(save.find_nth_role("pembangun",j),"pembangun") #find_nth_role(type,n)
        else:   
            #Bahan tidak cukup
            sel_pasir = int(data.bahan_bangunan[1][2]) - pasirT
            sel_batu = int(data.bahan_bangunan[2][2])- batuT
            sel_air = int(data.bahan_bangunan[3][2]) - airT
            if sel_pasir < 0:
                if sel_batu < 0:
                    if sel_air <0:
                        print("Bangun gagal. Kurang "+str(sel_pasir*-1)+" pasir, "+str(sel_batu*-1)+" batu, dan "+str(sel_air*-1)+" air.")
                    else:
                        print("Bangun gagal. Kurang "+str(sel_pasir*-1)+" pasir dan "+str(sel_batu*-1)+" batu.")
                else:   
                    if sel_air <0:
                        print("Bangun gagal. Kurang "+str(sel_pasir*-1)+" pasir dan "+str(sel_air*-1)+" air.")
                    else:
                        print("Bangun gagal. Kurang "+str(sel_pasir*-1)+" pasir.")
            else: 
                if sel_batu < 0:
                    if sel_air <0:
                        print("Bangun gagal. Kurang "+str(sel_batu*-1)+" batu dan "+str(sel_air*-1)+" air.")
                    else:
                        print("Bangun gagal. Kurang "+str(sel_batu*-1)+" batu.")
                else:   
                    print("Bangun gagal. Kurang "+str(sel_air*-1)+" air.")
    else:
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")

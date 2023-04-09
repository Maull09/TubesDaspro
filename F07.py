import data
import save
def kumpul():
    depth = data.iterasi +1  
    pasir = save.rndom(depth, depth*13, 5) #jumlah pasir, batu, dan air yang dibutuhkan (random)
    batu = save.rndom(depth, depth*17, 5)
    air = save.rndom(depth, depth*19, 5)
    data.iterasi += 1
    print("Jin menemukan "+str(pasir)+" pasir, "+str(batu)+" batu, dan "+str(air)+" air.")
    save.sAve("kumpul", [pasir, batu, air])
